# Math-paper orchestrator with two Kimi agents

Automates the communication between two roles:
- **Mathematical investigator**: writes and revises the paper.
- **Research lead**: audits the draft and generates concrete sub-tasks.

The orchestrator alternates between the two, persists all state to disk, and stops when the lead approves or when **40 loops** are reached.

---

## Layout

```
kimi/
├── PROMPT_INICIADOR.md          # ← Edit this first (seed prompt)
├── config.json                  # ← Config (loops, model, sessions, dry-run)
├── orchestrator.py              # ← Main script
├── roles/
│   ├── investigador.md          # Investigator system prompt
│   └── jefe_research.md         # Lead/auditor system prompt
├── mailbox/
│   ├── state.json               # Loop state
│   ├── investigador_response.md # Latest investigator response
│   └── jefe_response.md         # Latest lead response
├── paper/
│   └── draft.md                 # Accumulated paper draft
└── logs/                        # Logs of every Kimi call
```

---

## Usage

### 1. Write the seed prompt

Open `PROMPT_INICIADOR.md` and fill in:
- Topic and working title
- Main objective
- Audience and rigor level
- Desired structure
- Constraints and preferences

> This is **the only file you need to edit** to start a new paper.

### 2. (Optional) Adjust the configuration

In `config.json`:

```json
{
  "max_loops": 40,
  "model": null,
  "work_dir": "/home/maxim/PycharmProjects/bang-plank-euler-jacobi/kimi",
  "yolo": true,
  "quiet": true,
  "thinking": false,
  "dry_run": false,
  "use_sessions": true,
  "session_investigador": null,
  "session_jefe": null,
  "subprocess_timeout": 600
}
```

- `max_loops`: maximum number of investigator→lead cycles.
- `model`: Kimi model (e.g. `kimi-k2-0711-preview`). `null` uses the default.
- `work_dir`: working directory the agents see. Defaults to `kimi/` so the whole project is not scanned.
- `use_sessions`: if `true`, each role uses a persistent Kimi session (`--session`), keeping its own internal history.
- `session_investigador` / `session_jefe`: session IDs. If `null`, the orchestrator generates them automatically and stores them in `config.json`.
- `dry_run`: if `true`, simulates responses without calling the API (useful for testing the flow).

### 3. Run the orchestrator

```bash
cd kimi
python3 orchestrator.py
```

### 4. Inspect the results

- Draft: `paper/draft.md`
- Loop state: `mailbox/state.json`
- Logs: `logs/`

---

## How the loop works

```
Loop 1:
  1. Investigator writes/revises the paper (saved to paper/draft.md)
  2. Lead audits and returns ANALYSIS / TASKS / VERDICT
     - If VERDICT == APPROVED → done
     - If VERDICT == REVISE   → loop 2 starts with the new tasks
```

Each loop makes **two Kimi calls** (investigator + lead), so 40 loops = up to 80 calls.

---

## Context preservation (important)

The system uses **two simultaneous mechanisms** so the agents do not lose the thread:

1. **Persistent per-role sessions**
   Each agent has its own Kimi session ID (`--session`), so besides the current prompt, Kimi keeps the internal history of each conversation. The investigator remembers what it wrote; the lead remembers what it asked for.

2. **Explicit context in every prompt**
   The orchestrator always includes in the prompt:
   - the full seed prompt,
   - the current draft (`paper/draft.md`),
   - the lead's pending tasks,
   - the last 6 turns of history.

   This guarantees that, even if a session resets or a call fails, the agent receives everything needed to continue coherently.

To force a context "reset", delete `config.json` (it will be regenerated) or change the session IDs manually.

---

## Resuming a paper

The orchestrator reads `mailbox/state.json` on startup. To resume where it left off, just run again:

```bash
python3 orchestrator.py
```

To restart from scratch, delete the state and the draft:

```bash
rm mailbox/state.json paper/draft.md mailbox/*.md
```

And for fresh sessions:

```bash
rm config.json
```

(the orchestrator regenerates it with new IDs).

---

## Notes

- The orchestrator runs `kimi --quiet --yolo --input-format text` for non-interactive operation.
- The role prompts live in `roles/`: tone, rigor and output format can be adjusted there.
- The lead must return exactly `VEREDICTO: APROBADO` or `VEREDICTO: REVISAR`; the parser detects it automatically.
- A `429 rate limit reached` error means the Kimi usage quota is exhausted. Wait for the quota to refresh or use `dry_run: true` to test the flow without consuming API.
