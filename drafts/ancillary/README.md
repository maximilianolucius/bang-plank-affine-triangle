# Ancillary files for "Transport and tiling bounds for the affine plank problem on the triangle"
- median_rigidity_enumeration.py    — exhaustive symbolic enumeration (SymPy, exact over Q): the edge-tiling system has exactly 3 solutions (Lemma "computer-assisted").
- median_edgetilings_independent.py — independent cross-check by direct rational search (no SymPy), same 3 solutions.
- median_rigidity_centroid.py       — centroid witness: m(G)=(1/2,1/2,1/2); only [1/3,2/3]^3 covers.
- bang_Nc_nogo_chord.py             — ell<=w scan + exact segment tightness of the chord lemma (normalizer obstruction).
Run with Python 3 (+ sympy for the first; fractions/numpy stdlib otherwise).
