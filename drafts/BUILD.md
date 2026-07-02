# Build & status — ONE LIVE MANUSCRIPT

## Current manuscript: `affine-plank-triangle.tex`

- **Title:** *Transport and tiling bounds for the affine plank problem on the triangle*.
- **Status (2026-07-02, post-R6):** compiles clean with local `pdflatex` (2 passes):
  **0 errors, 0 unresolved references, 11 pages** → `affine-plank-triangle.pdf`.
- **Proved content (all verified; audit records `43/44-46/47/48/50/52`):**
  the `1/d` theorem with *method* sharpness correctly stated (fix R6-1a); two
  non-parallel directions (cites [Gardner88, Thm 1], parallel case dispatched — R6-1b);
  facet-parallel families (Minkowski-sum/BM-1D); 3 facets + 1 arbitrary plank (fibres);
  **medians: `Σrw ≥ 1` + full rigidity** (Lemma 5.2 now with a **human proof in
  Appendix A**, the `τ=½` case of Prop. A.1 — R6-2a); concurrence characterization +
  **iff corollary for cyclic triples** (R6-1f); **Thm 6.3 weighted perimeter**
  (two-parameter family); **Thm 6.6 NEW (R6-4): tightness and rigidity of the WHOLE
  cyclic family** — explicit tight covering `I_i` with masses `α,β,γ` and uniqueness,
  medians = centroid case; **Thm 6.8 NEW (R6-5): three-direction characterization**
  (witness measure exists iff the mid-level lines concur; settles Gardner's question
  for N=3 on the triangle); normalizer no-go (now a Proposition — R6-1d).
- **Appendix A:** complete classification of edge tilings for arbitrary cyclic triples
  (Prop. A.1, 7 classes modulo symmetry, full human proof).
- **Honest scope:** the triangle as a concrete body; NOT the conjecture via the Ambrus
  reduction (Remark 1.3). Priority claims carry "to our knowledge" + support (R6-1c).

## How to build
```bash
cd drafts/
pdflatex -interaction=nonstopmode affine-plank-triangle.tex
pdflatex -interaction=nonstopmode affine-plank-triangle.tex   # 2nd pass (refs)
```

## Ancillary files (for arXiv)
`drafts/ancillary/` (copies from `experiments/`): 6 scripts + README. Cited by the text
(Lemma 5.2, Thm 6.6, Prop. A.1, Prop. 7.1).

## Pending before submission
- Author/affiliation/email block (investigator's decision; placeholder marked in the .tex).
- R6-3/R7-0: external re-audit of the 11-page version — Thm 6.3, Thm 6.6, Thm 6.8 and
  Appendix A have no external audit yet.

## Obsolete
`drafts/obsolete/` contains the manuscripts of the **toric era** (`paper.tex`,
`paper.pdf`, `bang-plank-paper.tex`), refuted and abandoned (`notes/15/22/23`; a
concurring external audit is recorded in `auditorias/49`). **Do not audit or cite** —
see `obsolete/README-OBSOLETE.md`.

(Note: the `hamilton-jacobi-*` files formerly kept in `drafts/` belong to a DIFFERENT
project, not to this plank project; they are not part of this manuscript and are
excluded from the repository.)
