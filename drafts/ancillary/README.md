# Ancillary files for "Transport and tiling bounds for the affine plank problem on the triangle"

Protocol (see Appendix B of the paper): the paper is NOT computer-assisted.
Every theorem is proved in full in the text or in Appendix A; no proof depends
on a computation not reproduced in the text. These scripts are secondary
verification: exact re-derivations (rational/symbolic arithmetic throughout,
never floating point) of the load-bearing identities and finite case
enumerations. Where a script enumerates cases, the index set is explicitly
finite and swept exhaustively — no sampling, no lost cases.

Inputs: none (all data hard-coded as exact rationals/symbols).
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

## Round 10 additions (NOT yet cited by the frozen pass-5 text; to be wired
## into Appendix B at the next revision, after the external auditor's verdict)

| script | verifies | accompanies (future) |
|---|---|---|
| gardner_third_marginal.py | Route-B mixing inequality; M*(facets)=+inf (moment obstruction); pair-cost lemma pieces | notes/54-R10-1 |
| supD_dual_hunt.py | multi-knot dual LP machinery (float-guided, EXACT certification in fractions) + skeleton UBs + hunts | notes/54-R10-1 |
| supD_hunt_phase2.py | adapted-knot hunts (sandwich gap; class-(b) corner; tilted facets); independent random-point sanity of certified minima | notes/54-R10-1 |
| dual_certificates.py | SELF-CONTAINED verifier (no scipy) of the three archival dual certificates: D>=18/13 (tilt 1/10), D>=32/29 (class b), D>225/224 (sandwich) — moment bound not exact | notes/54-R10-1 |
| delta_eq_deltac.py | delta = delta_c theorem: counting lemma at general level (2928 external samples) + 507-triple sweep over all three pattern classes with exact point-in-triangle test | notes/54-R10-2 |
