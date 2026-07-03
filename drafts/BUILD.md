# Build & status — ONE LIVE MANUSCRIPT

## Current manuscript: `affine-plank-triangle.tex`

- **Title:** *Transport and tiling bounds for the affine plank problem on the triangle*
  (R7-3 decision 2026-07-02: KEEP — see `notes/51-R7-2 §5`; revisit after Rosa's pass 3).
- **Status (2026-07-02, post-R8 precision pass):** compiles clean with local
  `pdflatex` (2 passes): **0 errors, 0 unresolved references, 0 overfull, 17 pages**
  → `affine-plank-triangle.pdf`.
- **R8 (auditorias/53) executed:** the two blocking overclaims REMOVED (Thm 2.1
  sharpness now about the uniform measure, new Rem 2.2 with the `[1/2,2/3]`
  one-measure-vs-all-directions range; the false "(equivalently Conjecture 1.1)"
  deleted from Problem 1); scope fenced everywhere (five levels (a)-(e) in the
  intro; Rem 6.9 "within the witness-measure approach"; Cor 7.7 always with the
  B-Y caveat); rigor items (unnumbered **Pocket Lemma** so Thm 6.6/6.8 keep their
  numbers; x*,y* positivity in text; Prop 9.1 split from Remark 9.2; Gardner Thm 1
  verbatim; Thm 3.2 compactness GAP actually fixed via eta-shaving + one-line BM-1D);
  editorial (abstract rewritten/pruned, no sales words, MSC+keywords, Ambrus URL);
  **4 TikZ figures** (median covering; weighted witness at p; facet loop; MMM edge
  tiling), renders visually verified.
- **Frozen delivery copy for doña Rosa (pass 4, R8-7):**
  `drafts/entregas/affine-plank-triangle-2026-07-02-pasada4.{pdf,tex}` (17 pp,
  first version with §7–§8 and figures; §1–§6/App A numbering STABLE vs her pass 3).
  Hand-off document: `notes/52-R8-7-entrega-dona-rosa-pasada4.md`. Chief delivers.
- **Frozen delivery copy for doña Rosa (pass 3, R7-0):**
  `drafts/entregas/affine-plank-triangle-2026-07-02-pasada3.{pdf,tex}` (11 pp version,
  WITHOUT §7–§8; includes the two minor polish items of `auditorias/52 §5.1–5.2`).
  Hand-off document: `notes/51-R7-0-entrega-dona-rosa-pasada3.md`. Do not touch.
- **Proved content (audit records `43/44-46/47/48/50/52`):**
  the `1/d` theorem with *method* sharpness correctly stated; two non-parallel
  directions; facet-parallel families; 3 facets + 1 arbitrary plank;
  **medians: `Σrw ≥ 1` + full rigidity** (Lemma 5.2 = `τ=½` case of Prop. A.1, human
  proof); concurrence characterization + **iff corollary** (Cor 6.4); **Thm 6.3
  weighted perimeter** (two-parameter family); **Thm 6.6: tightness and rigidity of
  the whole cyclic family**; **Thm 6.8: three-direction characterization** (witness ⟺
  concurrence; Gardner N=3 on the triangle settled); normalizer no-go (now Prop. 9.1).
- **NEW in R7 (2026-07-02, NOT yet externally audited):**
  - **§7 The transport defect** (`sec:defect`): Def 7.1 `D(u)`; Prop 7.2 (attained;
    `Σrw ≥ 1/D`; `D=1 ⟺` concurrence; `D≤2`); Prop 7.3 moment bound
    `D ≥ 1/(1−2δ(u))`, facets `δ=1/6`; **Thm 7.4 `D(facetas)=3/2` exact** (inscribed
    hexagon-triangle loop, marginals `(3/2)1_{[0,2/3]}`); **Thm 7.6 linear stability**
    `D ≤ 1+ε/(m(m−ε))` near concurrence (frozen-weight skeleton); **Cor 7.7:
    `Σrw ≥ 27/29 > 4√3−6` for all cyclic `τ` with `max|τ_i−½| ≤ 1/60`** — first bound
    beyond B-Y strictly inside non-concurrent territory; Rem 7.9 exact sandwich
    example; Problem 10.3 (is the moment bound always exact? `sup D = 3/2`?).
  - **§8 Witness family on the 3-simplex** (`sec:simplex3`): **Thm 8.1 σ-family** on
    `Δ³` with closed-form skeleton weights `a(σ), b(σ)` — `Σrw ≥ 1` for 4 concurrent
    directions, first transport instance in `d=3`; Prop 8.2: `d≥4` cyclic medians
    admit no 1-skeleton witness. Problem 2 (`prob:suff`) updated.
- **Appendix A:** complete classification of edge tilings for arbitrary cyclic triples
  (Prop. A.1, human proof).
- **Honest scope:** the triangle as a concrete body; NOT the conjecture via the Ambrus
  reduction (Remark 1.3). Cor 7.7's comparison with B-Y carries the honest caveat
  (their bound is uniform over all triples; ours local) — Rem 7.8.

## How to build
```bash
cd drafts/
pdflatex -interaction=nonstopmode affine-plank-triangle.tex
pdflatex -interaction=nonstopmode affine-plank-triangle.tex   # 2nd pass (refs)
```

## Ancillary files (for arXiv)
`drafts/ancillary/` (copies from `experiments/`): 8 scripts + README. Cited by the
text (Lemma 5.2, Thm 6.6, §7, §8, Prop. A.1, Prop. 9.1).

## Pending before submission
- Author/affiliation/email/(final) metadata block — REAL human identity, cannot be
  decided by the investigator; placeholder marked in the .tex.
- R8-7: chief hands the frozen pass-4 package (17 pp) to doña Rosa.
- R8-6 (quantitative stability of the whole family) and R8-8 (coupling moonshot):
  not started — tail of the queue per auditorias/53.

## Obsolete
`drafts/obsolete/` contains the manuscripts of the **toric era** (`paper.tex`,
`paper.pdf`, `bang-plank-paper.tex`), refuted and abandoned (`notes/15/22/23`; a
concurring external audit is recorded in `auditorias/49`). **Do not audit or cite** —
see `obsolete/README-OBSOLETE.md`.

(Note: the `hamilton-jacobi-*` files formerly kept in `drafts/` belong to a DIFFERENT
project, not to this plank project; they are not part of this manuscript and are
excluded from the repository.)
