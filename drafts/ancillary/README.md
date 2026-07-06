# Ancillary files for "Transport and tiling bounds for the affine plank problem on the triangle"

Protocol (see Appendix B of the paper): the paper is proved by hand throughout,
with a **single exception** — Theorem "sandwichbang" (C^111_Delta(tau0)=1) is
*partially computer-assisted*. Its one finite step is discharged by an
exact-rational emptiness certificate, re-verified by an INDEPENDENT checker
(`bb_certificate_check.py`) that shares no code with the search. Every other
result is proved in full in the text or Appendix A. The remaining scripts are
secondary verification: exact re-derivations (rational/symbolic arithmetic
throughout, never floating point) of load-bearing identities and finite case
enumerations, swept exhaustively over explicitly finite index sets.

## QUICK START — verify the computer-assisted step (Theorem sandwichbang)

    python3 bb_certificate_check.py c3_sandwich_certificate.txt

- Environment: Python 3 (tested on 3.14), standard library ONLY
  (`fractions`, `hashlib`); no third-party package, no SymPy for this step.
- Runtime: a few minutes on one core; modest memory. Exact arithmetic only
  (no floating point) — hardware-independent.
- On SUCCESS the final line is `CERTIFICATE VALID`, preceded by the tree stats
  (812650 internal + 812651 leaves; P1=286024 P2=53907 P3edge=428672
  P3cell=2354 P4=41694) and the certificate SHA-256.
- On FAILURE (tampered/incorrect certificate) an `AssertionError` is raised and
  `CERTIFICATE VALID` is NOT printed. The checker has been confirmed non-vacuous:
  it rejects a tampered header, a non-interior split, a false leaf rule, and a
  truncated tree.

Other scripts — Inputs: none (all data hard-coded as exact rationals/symbols).
Outputs: assertion-checked "OK" lines; any failure raises.
Run: `python3 <script>.py` (SymPy required unless noted).

| script | verifies | accompanies |
|---|---|---|
| median_rigidity_enumeration.py | median edge-tiling system has exactly 3 solutions (exhaustive symbolic enumeration) | Lemma 5.2 |
| median_edgetilings_independent.py | same 3 solutions, independent rational search (no SymPy) | Lemma 5.2 |
| median_edgetiling_types_crosscheck.py | third check via the L/M/R trace formulas | Lemma 5.2, App. A |
| median_rigidity_centroid.py | centroid witness m(G)=(1/2,1/2,1/2); only [1/3,2/3]^3 covers | Theorem 5.1 |
| cyclic_family_tight_rigidity.py | margin identity, witness positivity, exact coverage checks; general-tau tiling solutions | Thm 6.6 (Lemmas 6.7–6.9), Prop. A.1 |
| role_patterns_classification.py | exhaustive exact classification of all 216 role assignments | Theorem 6.11 |
| bang_Nc_nogo_chord.py | ell<=w scan + exact segment tightness of the chord lemma | Proposition 9.1 |
| transport_defect.py | facet loop marginals (3/2)1_[0,2/3]; exact concurrence defects via LP; frozen-weight identities; sandwich example | Thm 7.4, Thm 7.13, Rem 7.17 |
| defect_duality.py | facet dual certificate (1-3t/2)_+; wedge-certificate algebra incl. sandwich dependency c=(75,76,74|113) -> 225/224; sign-counting of no-external-concurrence; centroid bound delta<=1/6; Delta^d facet-cycle marginals ((d+1)/2 on [0,2/(d+1)]) for d=2..7; B-Y region algebra eps(m)=km^2/(1+km) | Thm 7.3, Thm 7.6–7.8, Lem 7.9, Cor 7.15, Thm 8.2 |
| simplex3_weighted_skeleton.py | sigma-family closed forms a(sigma), b(sigma) + uniqueness; d=3 median degeneracy; d>=4 skeleton obstruction | Thm 8.1, Prop 8.4 |

## Round 10/12 additions (cited by Appendix B since pass 6)

| script | verifies | accompanies |
|---|---|---|
| gardner_third_marginal.py | Route-B mixing inequality; M*(facets)=+inf (moment obstruction); pair-cost lemma pieces | Prob 10.4 (refuted route) |
| supD_dual_hunt.py | multi-knot dual LP machinery (float-guided, EXACT certification in fractions) + skeleton UBs + hunts | Rem 7.20, Prob 10.4 |
| supD_hunt_phase2.py | adapted-knot hunts (sandwich gap; class-(b) corner; tilted facets); independent random-point sanity of certified minima | Rem 7.20 |
| dual_certificates.py | SELF-CONTAINED verifier (no scipy) of the three archival dual certificates: D>=18/13 (tilt 1/10), D>=32/29 (class b), D>225/224 (sandwich) | Rem 7.20 |
| delta_eq_deltac.py | delta = delta_c theorem: counting lemma at general level (2928 external samples) + 507-triple sweep with exact point-in-triangle test | Thm 7.11, Lem 7.10 |
| covering_constant.py | Thm 6.13: vertex identities, 3 polynomial identities (margins + excess (P-Q)^2/((1+P)(1+Q))), exact coverage oracle (8 sign cells, Chebyshev LP), MMM coverings, edge-LP LB, float-guided Sigma-r hunt with exact certification (anti-sensation protocol) | Thm 6.13, Lem 10.2, Sec 10 |

## Round 13 additions (NOT yet cited by the frozen pass-6 text; integrate after the verdict)

| script | verifies | accompanies (future) |
|---|---|---|
| c3_extreme_regime.py | extreme-regime theorem for C_3 (corner ranges/extents symbolic; Case A strict excesses; Case B gap implications at 400 tau; end-to-end oracle sanity); exact insufficiency of naive per-piece bounds (1875/1094 < 2 at the sandwich) | notes/56-R13 |
| r13_2_bounded.py | certified adapted-loop upper bounds D(tilt eps) < 3/2 for eps=1/10,1/20,1/50 (facets local max, symmetric path); denser sandwich dual/skeleton attempt | notes/56-R13 |

## Round 14 additions (NOT yet cited by the frozen pass-6 text)

| script | verifies | accompanies (future) |
|---|---|---|
| tilt_local_max.py | THEOREM: (3/2)/(1+eps) <= D(tilt eps) <= (3/2)(1-eps)/(1-eps+eps^2) < 3/2 on (0,1/2); x*=(1-2eps)/(3(1-eps)); reproduces 135/91, 190/127, 1225/817 | notes/57-R14 |
| c3_balanced_bb.py | exact branch-and-bound for the balanced regime of C_3(sandwich): prunes P1 (Sigma r), P2 (extreme thm), P4 (empty plank -> 2-plank thm), P3 (enlarged config fails: exact 1-D edge test + positive-area cell via exact clipping — complete failure test) | notes/57-R14 |

## Round 15 additions (certification package; integrate into Appendix B after freeze lifts)

| script | verifies | accompanies (future) |
|---|---|---|
| c3_balanced_bb.py (emit_certificate) | emits the deterministic preorder certificate of T(tau0): tree shape + per-leaf rule/witness, no boxes | Thm sandwich-bang, App B |
| bb_certificate_check.py | INDEPENDENT checker (no shared code): reconstructs boxes, verifies tiling (binary-tree identity) + re-validates all 812651 leaves + SHA -> CERTIFICATE VALID | Thm sandwich-bang, App B (Pillar 2/4) |
| r15_equality.py | equality classification: min proper 2-plank cover width = 31/25, 31/25, 5/4 (all >1) -> C3(sandwich)=1 attained only trivially | Thm sandwich-bang (equality) |

Certification artifacts (SHA-256, full):
  c3_balanced_bb.py        b2468aa9acc91f4fbeec9b58afed706d3b865e7f0e49ecfa2c3804eae382f4cb
  bb_certificate_check.py  90a25ce8ea059abed4707b5314a164be40298b1fe9fe42394d56a1c69c48eb1b
  c3_sandwich_certificate.txt (12062803 B)  ead66ff2cfd547f8e2acd7c7bf5cce67d114a0aa1146559fc5b065028de6b86c
Checker output: 812650 internal + 812651 leaves; P1=286024 P2=53907 P3edge=428672 P3cell=2354 P4=41694; CERTIFICATE VALID.

## Note on the certificate file (arXiv)
`c3_sandwich_certificate.txt` (12 MB) is the emptiness certificate for
Theorem 10.8, re-verified by `bb_certificate_check.py` (CERTIFICATE VALID).
It is regenerable deterministically:
    python3 -c "import c3_balanced_bb as bb; bb.emit_certificate('c3_sandwich_certificate.txt')"
(the searcher is deterministic: fixed DFS, midpoint bisection, split
coordinate = first widest). SHA-256 ead66ff2cfd547f8...  If size is a concern
for arXiv, ship the two scripts and these instructions instead of the file.
