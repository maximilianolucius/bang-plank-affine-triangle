% MILESTONE 11 — Research vector map (the 5 attack vectors)  [LIVE TRACKER]
% Honest status of every hito. Tags: [DONE] [PARTIAL] [REFUTED] [UNTOUCHED]
% Last updated: 2026-06-28

=========================================================================
VECTOR 1 — Topological-combinatorial (Bang's legacy)
=========================================================================
1.1 Non-symmetric Bang lemma (Gram matrix)   [UNTOUCHED-as-proof]
    Formalized the TARGET (affine Bang lemma, note 11) but did NOT prove the
    non-symmetric generalization. The hard core.
1.2 Reduction to a sign problem              [PARTIAL]
    Established: uncovered point = a sign-cell R_ε (intersection of half-planes).
    KEY computed fact: for Σrw<1, an uncovered point always sits at an ARRANGEMENT
    VERTEX (2805/2805) ⟹ the search is FINITE/combinatorial. Did NOT complete the
    sign-selection proof.
1.3 Bang's lattice "walk"                    [UNTOUCHED]
    Never analyzed Bang's lattice-walk and its behavior for fine planks.
1.4 Two-direction case                       [DONE]
    Proved Σrw≥1, sharp, via uniform-marginal coupling (note 12 / paper §5).
    Also facet-parallel (all dims) via sumset (note 08). Two sub-cases SOLVED.

=========================================================================
VECTOR 2 — Analytic / measure-theoretic (Ball, Gardner, Ambrus)
=========================================================================
2.1 Existence of a relative-width measure (Gardner)  [REFUTED for c=1]
    Proved NO single probability measure reaches c=1 on the simplex (3 uniform
    marginals impossible). Best single measure: c*=1.60 ⟹ only 0.624 (note 07,
    paper §7). Gardner's exact measure does NOT exist for the triangle.
2.2 Non-commutative version                  [UNTOUCHED]
2.3 Bound Σr_i² ≥ f(S)                        [PARTIAL / stuck]
    Have refined bound 1≤2S−Σr² and bootstrap b↦1/(2−b). The needed Σr²≥bS FAILS
    for fine planks; all fixes (merge/split/peel) audited and refuted (note 06).
    No valid f(S) found.
2.4 Best lower bound for d=2                  [DONE — reproduced SOTA]
    Read B-Y 2026 (2/(1+√d)≈0.828). Computed triangle-specific min ℓ/w=0.928 (a
    valid but trivial body-specific eval). Verified Ambrus reduces d→(2d−1)-simplex,
    whose min ℓ/w = EXACTLY 2/(1+√d): the SOTA is tight for this method. Identified
    the frontier program ("cost of the caps beyond the longest chord"); not closed.

=========================================================================
VECTOR 3 — Optimization / extremal (Hunter)
=========================================================================
3.1 Equality characterization (Hunter)       [UNTOUCHED]
    Did not extend Hunter's S=1 equality characterization to n planks.
3.2 Perturbation analysis                     [UNTOUCHED]
3.3 Peeling / descascarado                     [REFUTED]
    The "remove a fine plank ⟹ similar triangle in complement" is FALSE for a
    generic (tilted) plank: the cut isn't parallel to an edge, the cap is a
    quadrilateral, scale 0.55≠1−ρ (note 06·N2, audited numerically). Dead end.
3.4 SDP formulation                           [PARTIAL]
    Did LP (fractional cover = integrality gap; single-measure LP gave c*). Did
    NOT do a true SDP relaxation / pattern-mining for fixed plank count.

=========================================================================
VECTOR 4 — Simplification / duality (Carathéodory)
=========================================================================
4.1 Reduction to a vector problem            [DONE]
    The vector model: planks ↔ (ũ_a∈[0,1]³ min0 max1, interval I_a). Note 10,
    paper §4. Removes complement geometry.
4.2 Colorful Carathéodory (Ambrus)           [UNTOUCHED]
    Identified as the natural generalization of the barycentric partition-of-unity
    (the facet sumset is a special case), but did NOT adapt the colorful-Cara proof.
    *** Strongest UNTOUCHED lead. ***
4.3 Duality / separation (Hahn–Banach)       [PARTIAL]
    The witness-measure method IS LP duality/separation. Showed the covering-
    dependent certificate is LP-dual-EQUIVALENT to the conjecture (needs explicit
    construction, not existence). Did not pursue a Hahn–Banach separation directly.

=========================================================================
VECTOR 5 — Interdisciplinary connections
=========================================================================
5.1 Diophantine approximation (Davenport)    [UNTOUCHED]
5.2 Conway's "fried potato" problem          [UNTOUCHED]
    Inverting fried-potato ⟹ Bang could give a natural inductive route. Unexplored.
5.3 Surface-measure (boundary) argument      [PARTIAL / weak]
    Considered the perimeter/boundary measure; gives a bad constant (>2), abandoned.
    Did not find a plank-invariant surface measure on ∂triangle.

=========================================================================
SCORECARD
=========================================================================
DONE (4):     1.4 two-direction, 2.4 reproduce SOTA, 4.1 vector model, +facet-parallel
REFUTED (3):  2.1 c=1 measure, 3.3 peeling, (splitting) — documented dead ends
PARTIAL (5):  1.2 sign cells, 2.3 Σr², 3.4 SDP/LP, 4.3 duality, 5.3 surface
UNTOUCHED (7):1.1 non-sym Bang lemma, 1.3 lattice walk, 2.2 non-commutative,
              3.1 Hunter equality, 3.2 perturbation, 4.2 COLORFUL CARATHÉODORY,
              5.1 Davenport, 5.2 fried potato

MOST PROMISING UNTOUCHED LEADS (honest ranking):
  1. 4.2 Colorful Carathéodory (Ambrus) — the facet sumset already IS its barycentric
     special case; adapting the colorful version is the natural generalization.
  2. 1.2→1.1 sign cells are FINITE (verified) — a combinatorial/parity invariant on
     arrangement vertices is the most concrete topological lead.
  3. 5.2 Conway fried-potato inversion — a genuinely different inductive structure.

=========================================================================
ROUND 2 FINDINGS (2026-06-28) — attacked 1, 4.2, 2, 3
=========================================================================
[1.1 NON-SYMMETRIC BANG LEMMA — REFUTED as a route]
  Bang's lemma in matrix form: A symmetric, a_ii=1 ⟹ ∃ signs ε with
  |Σ_i a_ki ε_i w_i − m_k| ≥ w_k ∀k. TESTED by brute force:
    • symmetric A: 0 failures (validates).
    • arbitrary non-symmetric A: ~7% have NO sign vector (293/4000, n=3) ⟹ the
      non-symmetric sign lemma is FALSE.
    • low-rank A=UX^T (the affine structure, rank≤d): ~0.1% failures (rank2) — almost
      holds but NOT unconditional, AND the produced point x=Σε_i w_i u_i can fall
      OUTSIDE the simplex. ⟹ the sign/Bang route has a genuine obstruction for the
      affine simplex. Conclusion: Vector 1 (signs) cannot work naively; the route
      MUST be convex (4.2).

[4.2 COLORFUL CARATHÉODORY — confirmed necessary, not closed]
  Read Ambrus' machinery (Prop 8: the sign-graph has no directed cycle via an
  increasing potential ‖p(ε)‖; Prop 9: a deformation φ of the Bang system works iff
  it is non-contracting in plank directions). Ambrus states the cases where Prop 9
  applies are "uncertain" — NOT known to cover the simplex. The facet sumset (note 08)
  is the barycentric special case of the colorful selection. No general proof found.

[3 HUNTER/EXTREMAL — confirmed rigidity]
  3 single planks covering the triangle need Σrw > 1 generically (1.05–1.13);
  the sharp Σrw=1 requires edge-parallel planks at the edges (Hunter's extremal).
  Consistent with Hunter's equality characterization; the extremal is rigid/isolated.

[2.3 Σr²≥f(S) — still STUCK]
  No valid f(S); fine planks defeat every lower bound on Σr² (re-confirmed).

NET: serious effort, real STRUCTURAL/NEGATIVE results (sign route ruled out; convex
  route confirmed necessary; Hunter rigidity), but NO frontier advance. Open core
  intact. Beating 2/(1+√d) remains genuine open research.
