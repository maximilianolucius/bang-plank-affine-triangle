# bang-plank — The affine plank problem on the triangle

Research project on **Bang's affine plank conjecture** (1951): if a convex body
`K` is covered by planks, then `Σ rw_K(P_i) ≥ 1`. Open in general; open already
for 3 planks in the plane (Bakaev–Yehudayoff 2026).

## Current manuscript

**`drafts/affine-plank-triangle.tex`** — *Transport and tiling bounds for the
affine plank problem on the triangle* (the only live manuscript; see
`drafts/BUILD.md`). Main results:

- **Median theorem with full rigidity**: three median planks satisfy `Σrw ≥ 1`,
  with equality iff each is the central third of its median.
- **Weighted-perimeter theorem**: an explicit uniform-marginal witness measure
  (edge masses `1−2p_j`) proving the sharp bound for a two-parameter family of
  generic concurrent direction triples.
- **Tightness and rigidity of the whole cyclic family**: the bound is attained
  at every member by an explicit covering, unique for its directions.
- **Three-direction characterization**: on the triangle, a uniform-marginal
  witness measure exists iff the three mid-level lines concur — settling
  Gardner's (1988) existence question for three directions on the triangle, and
  reducing the open case of the conjecture on the triangle exactly to
  non-concurrent triples.
- **A normalizer obstruction**: the chord-lemma step in Bang's sign argument is
  sharp, so that argument cannot reach any normalizer beyond the longest chord.

## Repository layout

| Directory | Contents |
|---|---|
| `drafts/` | Current manuscript + `ancillary/` (verification scripts for arXiv) + `obsolete/` (an abandoned earlier approach — do not cite) |
| `notes/` | Numbered research notes — the primary record of the work (in Spanish) |
| `auditorias/` | Audit reports and per-round work orders by the research lead (in Spanish; `00-ordenes-de-trabajo.md` is the living document) |
| `experiments/` | Load-bearing scripts (exact verification with `sympy`/`fractions`; see the notes that cite them) |
| `paper-ready/` | Material from early rounds |
| `kimi/` | Investigator/lead orchestrator infrastructure |

`refs/` (third-party PDFs: Bakaev–Yehudayoff, Ball, Ambrus, Gardner, Verreault)
is **excluded from the repository** for copyright reasons; exact citations are
in the manuscript's bibliography and in `notes/42`.

The manuscript, the ancillary files and the repository documentation are in
English. The research notes and audit records (`notes/`, `auditorias/`) are
working documents kept in Spanish.

## Rigor rules of the project

- Exact arithmetic (`fractions`/`sympy`); a numeric grid is never a proof.
- Strict labels `[PROVED] / [EVIDENCE] / [OPEN]` on every claim.
- Every statement in the manuscript is either proved in the text or cited with
  attribution.

## Building the paper

```bash
cd drafts/
pdflatex -interaction=nonstopmode affine-plank-triangle.tex
pdflatex -interaction=nonstopmode affine-plank-triangle.tex
```
