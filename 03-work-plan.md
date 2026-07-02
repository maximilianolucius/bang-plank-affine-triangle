# Work plan — full realization of the paper (Candidate B)
### "An algebraic-variational approach to Bang's affine plank conjecture"
> Owner: D. Pinasco (+ likely Galicer, Ortega-Moreno). Drafted 2026-06-27. Lives in `/opt/VS/bang-plank-euler-jacobi/`.

This plan is **gated and modular**: each phase ends in a decision gate. The paper is designed to be *publishable at M2* even if the moonshot (M3) never lands. We always have a fallback deliverable.

---

## 0. Thesis & contribution statement (what the paper claims)

> *We introduce the critical-point / Euler–Jacobi(–BKK) machinery — recently used by Martínez & Ortega-Moreno to settle the real polarization problem — into the study of Bang's affine (relative-width) plank conjecture. We (i) give a new variational proof of Ball's symmetric plank theorem, (ii) establish the sharp relative-width bound for [simplices / a structured non-symmetric class], and (iii) [improve the general lower bound beyond `2/(1+√d)` / settle the planar 3-plank case].*

Minimum viable paper = (i)+(ii). (iii) is upside.

---

## 1. Phase structure, deliverables, gates

### Phase M0 — De-risk & literature lockdown  *(≈1–2 weeks)*
**Tasks**
- T0.1 Negative novelty search (method): Scholar cite-trees of M–OM 2605.28744, BY26 2602.20290, CM16 1604.00456; keyword crosses `plank × {Euler–Jacobi, BKK, Bernstein theorem, toric residue, Morse}`.
- T0.2 Read in full + take structured notes (`refs/notes-*.md`): **Ball91**, **CM16**, **BY26**, **Verreault survey**, **M–OM** (pull 2605.28744).
- T0.3 **Confirm/kill the Ambrus → simplex reduction** (the linchpin of M2). Find the exact statement & citation.
- T0.4 Resolve **CRUX 3**: write down the precise toric/BKK Euler–Jacobi (global residue) theorem we can invoke, with hypotheses.
**Deliverable:** `notes/04-m0-findings.md` + decision memo.
**GATE G0 — proceed iff:** method niche still empty AND a usable toric-vanishing theorem exists AND (Ambrus reduction real OR an alternative structured target identified). *If Ambrus reduction is false → M2 retargets to bodies of revolution / `d=2`.*

### Phase M1 — Variational proof of Ball (symmetric)  *(≈2–4 weeks)*
**Math to develop**
- T1.1 Set up the maximization of the relevant width/penalty functional on `∂(symmetric C)`; derive the critical system (analogue of `yⱼ(Ay)ⱼ=αⱼ`).
- T1.2 Re-prove the three pillars in the symmetric setting: **reality** (CRUX 1), **one root per chamber** (Lemma 4 analogue), **simplicity** of roots.
- T1.3 Apply Euler–Jacobi with the right test polynomial `g` to force a witness ⟹ `Σ rel-width ≥ 1`. Recover sharpness/equality.
**Deliverable:** `drafts/M1-symmetric-proof.md` (self-contained proof).
**GATE G1 — proceed iff** the engine reproduces Ball's theorem. *(If not: the algebraic route is likely doomed → fall back to publishing a methods/negative note, or pivot to a purely variational (non-algebraic) attack.)*

### Phase M2 — First sharp non-symmetric case  *(≈4–8 weeks)*  ← **the real prize that's actually reachable**
**Math to develop**
- T2.1 For the **simplex** (or chosen class): write the support function / gauge, build the critical system explicitly.
- T2.2 **CRUX 2:** compute Newton polytopes & BKK mixed volume; verify 0-dim complete intersection, simple real roots in bijection with combinatorial cells.
- T2.3 **CRUX 1:** prove reality for this non-symmetric metric (limiting argument from smooth strictly-convex approximations if needed).
- T2.4 Toric Euler–Jacobi ⟹ `Σ rel-width ≥ 1` (sharp) for the class; characterize equality (feeds G6).
**Deliverable:** `drafts/M2-simplex-theorem.md`.
**GATE G2 — STOP-AND-WRITE point:** a sharp non-symmetric relative-width theorem ⟹ **minimum viable paper secured.** Decide: ship M1+M2 now, or push M3.

### Phase M3 — Stretch (choose one, time-boxed)  *(open-ended)*
- **M3a** Beat `2/(1+√d)` general bound (must out-run BY26 — read their method first to avoid collision).
- **M3b** Close `d=2, n=3` (finite critical system; rigorous case analysis).
- **M3c** Weaken Chambers–Mouille's convex-remainder hypothesis (G5) by recasting it as a non-degeneracy condition on the critical system.
**GATE G3:** any success → upgrade the paper's headline; else drop cleanly (M1+M2 still stands).

### Phase M4 — Rigidity, validation, write-up  *(≈3–5 weeks)*
- T4.1 Equality/rigidity theorem (G6) for whatever cases landed.
- T4.2 **Numerical validation** (see §3) — independent confirmation of every analytic claim.
- T4.3 Full manuscript, internal adversarial review, submission.

---

## 2. The mathematics, consolidated (the actual hard core)

The whole program rises or falls on porting **three pillars** from the round sphere to a general body's boundary (full dictionary in `notes/method-abstraction.md`):

1. **Reality** of all critical solutions — replace `A=G⁻¹` (PD) by support-Hessian; energy/imaginary-part argument must survive.
2. **Counting** — replace Bézout `2ⁿ` by **BKK mixed volume**; need simple real roots ↔ combinatorial cells.
3. **Vanishing** — replace classical Euler–Jacobi by its **toric/BKK global-residue** form; force a good witness root.

Plus the **objective design**: find the functional on `∂K` whose critical points encode `Σ rel-width` exactly (the analogue of `Π⟨vⱼ,x⟩^{kⱼ}`). This is non-obvious and is itself a research sub-task (T1.1) — possibly the single most creative step.

---

## 3. Validation strategy (numerical, to backstop every proof)

Per the global setup, **heavy/long compute goes to a remote box** (R14/R15 = `172.16.0.14/.15`, usually idle, 16 cores; **never R11/.144** for heavy work). Plan:
- **V1 (M1):** numerically solve the symmetric critical system for random symmetric `C`, `n` up to ~12; confirm all roots real, count = `2ⁿ`, witness satisfies `Σ ≥ 1`. (Homotopy continuation: `HomotopyContinuation.jl`, or `phcpy`/PHCpack for BKK certification.)
- **V2 (M2):** for simplices in `d=2..8`, enumerate critical points, verify BKK count matches, and that `min Σ rel-width = 1` (sharp). **This is also how we discover the right `g` / objective empirically before proving it.**
- **V3 (M3a):** search random non-symmetric bodies for the worst-case `Σ rel-width`; check whether the variational bound beats `2/(1+√d)` numerically *before* attempting the proof.
- **V4:** interval-arithmetic / certified roots for any low-dim finite check (avoid the "approximate-decimals-in-a-table" rigor gap that weakened the n≤14 polarization paper).
- Tooling: Julia (HomotopyContinuation.jl) primary; SageMath/Macaulay2 for Newton polytopes & mixed volumes; mpmath/Arb for certified arithmetic. Keep all scripts in `experiments/`.

---

## 4. Target venues
- **Full success (M3 lands / sharp general progress):** *Inventiones* / *Duke* / *GAFA* tier (Ball91 was Inventiones — same lineage).
- **Minimum viable (M1+M2):** *IMRN*, *Israel J. Math.*, *Mathematika*, *J. Funct. Anal.*, *Adv. Math.* (depending on strength). A "first algebraic-variational attack + first sharp non-symmetric case" is a solid mid-to-high tier paper.
- **M1-only fallback (new proof of Ball):** *Proc. AMS* / *Bull. LMS* note.
- Pre-empt competition: post to **arXiv early** once M1+M2 are solid (BY26 is active in this space — priority matters).

## 5. Collaboration & roles
- **Ortega-Moreno** — co-inventor of the engine; essential for CRUX 1–3 and to avoid colliding with M–OM.
- **Galicer** — asymptotic geometric analysis & stochastic geometry; owns M3a (general bound) and the BKK/convex-geometry interface.
- **Litvak** (collaborated 2022 on volume-ratio of projections) — heavyweight on covering/John-position; natural consult for the `2/(1+√d)` frontier.
- **Pinasco** — the polarization↔plank bridge, rigidity (G6), overall synthesis.

## 6. Risk register & contingencies
| Risk | Likelihood | Mitigation / fallback |
|---|---|---|
| CRUX 1 (reality) fails for non-symmetric bodies | Med | Restrict to smooth strictly-convex + limiting; if hard, M1-only note |
| CRUX 2 (BKK count not real/simple) | Med-High | Perturbation to generic body; if structural, pivot to non-algebraic variational |
| Ambrus→simplex reduction false | Med | Retarget M2 to bodies of revolution / `d=2`; G0 catches this early |
| BY26 (or others) scoop the general bound | Med | Lock M1+M2 fast, arXiv early; M2 is independent of M3a |
| Method already tried & unpublished/folklore | Low-Med | M0 negative search; even so, *first published* + sharp new case still novel |
| Full conjecture stays out of reach | High | **Designed for:** M1+M2 is the deliverable; M3 is upside |

## 7. Timeline (indicative, research-paced)
- M0: weeks 1–2 · M1: weeks 2–6 · M2: weeks 6–14 · (M3 time-boxed ~6–10 wks if pursued) · M4: final 3–5 wks.
- **First arXiv (M1+M2): ~month 4–5.** Full version with M3 (if any): ~month 7–9.

## 8. Immediate next actions (this week)
1. T0.1 negative novelty search.  2. Pull arXiv:2605.28744 (M–OM) + read Ball91 & CM16 & BY26 & Verreault.  3. Confirm Ambrus reduction.  4. Write down the toric Euler–Jacobi statement.  → all into `notes/04-m0-findings.md`, then convene the G0 gate decision.
