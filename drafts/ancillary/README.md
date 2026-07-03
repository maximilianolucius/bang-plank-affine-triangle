# Ancillary files for "Transport and tiling bounds for the affine plank problem on the triangle"
- median_rigidity_enumeration.py       — exhaustive symbolic enumeration (SymPy, exact over Q): the median edge-tiling system has exactly 3 solutions (Lemma 5.2).
- median_edgetilings_independent.py    — independent cross-check by direct rational search (no SymPy), same 3 solutions.
- median_edgetiling_types_crosscheck.py — third independent check via the L/M/R trace formulas of Appendix A (exact rational grid).
- median_rigidity_centroid.py          — centroid witness: m(G)=(1/2,1/2,1/2); only [1/3,2/3]^3 covers.
- cyclic_family_tight_rigidity.py      — Theorem 6.6 (tightness & rigidity of the cyclic family): symbolic verification of the affine identity, the margin (S ± abg/S), witness positivity, and exact rational coverage checks (MMM covers; LLL/RRR leave positive area) at several family points; also the general-tau tiling solutions of Proposition A.1.
- role_patterns_classification.py      — Theorem 6.8 (three-direction characterization): exhaustive exact classification of all 216 role assignments (concurrence conditions per class; supports the hand proof).
- bang_Nc_nogo_chord.py                — ell<=w scan + exact segment tightness of the chord lemma (normalizer obstruction).
- transport_defect.py                  — Section 7 (transport defect): facet loop with marginals (3/2)1_[0,2/3] (Theorem 7.4), moment bound delta(u) via exact LP, frozen-weight perturbation identities (Theorem 7.6), exact sandwich examples (Remark 7.9), small delta-landscape sweep (Problem 10.3).
- simplex3_weighted_skeleton.py        — Section 8 (3-simplex family): exact solution of the weighted 1-skeleton system for the sigma-family (Theorem 8.1, closed forms a(sigma), b(sigma), uniqueness), degeneracy of the literal d=3 cyclic medians, and the d>=4 skeleton obstruction (Proposition 8.2).
Run with Python 3 (+ sympy where noted; fractions/numpy stdlib otherwise).
