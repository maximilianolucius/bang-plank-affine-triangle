% MILESTONE 07 — The open core (≥3 directions)  [OPEN]
% Paper section: §6/§7. The honest statement of what remains.

WHERE THE METHODS STOP.
  • Witness measure: capped in [1/2,1) for ≥3 generic directions (06·N1).
  • 2-direction sharp proof (05) uses a 2-D coupling with uniform marginals
    (a witness measure flat in BOTH used directions). For 3 directions
    f_u,f_v,f_w on the 2-D simplex, no measure is flat in all three (06·N1),
    so c=1 is unreachable by a single measure.
  • The 2-D coupling = a bipartite transport (min cover = max coupling, König).
    With 3 directions, Φ=(f_u,f_v,f_w):Δ→[0,1]³ has a 2-D image surface and the
    "bands" are 3-D slabs; the duality is no longer bipartite/2-D.

THE TARGET (affine Bang lemma, on the vector model 04).
  Let U=(ũ_{a,i})∈[0,1]^{m×n}, each row min 0 max 1; intervals I_a, |I_a|=rw_a.
  CLAIM: Σ|I_a| < 1 ⟹ ∃ x∈Δ_n with (Ux)_a ∉ I_a ∀a.
  This is the non-symmetric / affine analogue of Bang's 1951 selection lemma
  (which handles the symmetric/centered case via signs maximizing ‖Σε_j a_j‖²).

QUANTIFIED BARRIER (computed, R15).
  • Best single-measure constant for the triangle: c* = 1.602 (LP over measures,
    min over μ of max over all planks μ(P)/rw(P)). So the BEST single witness
    measure proves only  S ≥ 1/c* = 0.624.  (area: c=2 ⟹ 0.5.)
  • The true minimum is 1. The gap 0.624 → 1 is an INTEGRALITY GAP: with 2
    directions the cover/coupling duality is bipartite (König-exact, max
    coupling = 1); with 3 directions it is tri-partite and the LP/measure
    relaxation is no longer tight (cf. 3-dimensional matching).
  • Note: 3 directions already contains the extremal config (3 edge-parallel
    planks, S=1), so it is essentially the full conjecture.

CANDIDATE NEXT STEPS.
  1. Covering-DEPENDENT witness measure μ (chosen after seeing the planks).
     CAVEAT: existence of such μ with μ(P_a) ≤ rw_a is LP-dual-EQUIVALENT to the
     conjecture itself — so this route needs an explicit CONSTRUCTION, not an
     existence argument.
  2. Multipartite/iterated transport replacing the bipartite coupling. (Naive
     iteration — 2 marginals uniform + 1 free — gives only a weighted bound, not 1.)
  3. Topological/sign route: the affine (non-symmetric) Bang lemma on the vector
     model (04); Bang's walk; colorful Carathéodory à la Ambrus. This is the only
     route NOT blocked by the integrality gap (it is combinatorial, not fractional).

INTEGRALITY GAP, MEASURED (R15).
  Fractional covering LP (= best witness-measure bound) restricted to 3 fixed
  directions, vs the true cover (=1):
    edge-normals (barycentric/extremal): fractional 0.682  → gap 0.318 (LARGEST)
    generic triples:                     fractional 0.92–0.96 → gap small
  The gap is MAXIMAL exactly at the barycentric extremal Σλ_i=1, where the
  measure/fractional bound is weakest — yet there the DIRECT argument is trivial
  (planks {λ_i≤ρ_i} cover ⟺ Σρ_i≥1, from Σλ_i=1). So the clean case for the
  fractional method is the hard case for the direct method, and vice-versa.
  Moral: route 3 must MATCH the direct barycentric mechanism, not the measure.
  (NB: 0.68 is the fractional relaxation, NOT a real covering — no contradiction.)

BARYCENTRIC INSIGHT.
  The extremal case is proved WITHOUT a measure: Σλ_i(x)=1 (partition of unity)
  forces an uncovered point whenever Σρ_i<1. The general counting argument should
  be a generalization of this partition-of-unity identity to arbitrary plank
  directions, not a single witness measure (which is provably capped at 0.624).

ROUTE-3 FOOTHOLD (computed, R15).
  For 3-direction sub-coverings with Σrw < 1: in 2805/2805 cases an uncovered
  point exists AND one can be taken at a VERTEX of the line arrangement
  (intersection of two plank boundaries, or a triangle vertex). I.e. the
  certificate of non-covering is COMBINATORIAL — the search for an uncovered
  point is finite. This is the structural basis a Bang-type lemma needs:
  reduce "∃ uncovered x" to a finite check over arrangement vertices, then
  argue by a counting / sign / parity invariant that Σ|I_a|<1 forces one to be
  free. (Contrast: the measure routes are fractional and hit the 0.624 ceiling.)

STATUS. OPEN — barrier quantified (0.624 single-measure ceiling); route-3 has a
  concrete combinatorial foothold (uncovered point at an arrangement vertex).
  Solid contributions remain 01–05 + the map 06. Recommended attack: route 3.
