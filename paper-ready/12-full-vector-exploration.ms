% MILESTONE 12 — Complete exploration of the 5 vectors, by success-probability
% Goal-driven sweep: learnings + findings + future-research per hito. HONEST.
% Date: 2026-06-28. Frontier NOT expanded; structural knowledge gained.

ORDER OF ATTACK (by honest success probability) and OUTCOME:

#1  4.2 COLORFUL CARATHÉODORY  [reformulated; open core]
  LEARNING: Derived a HELLY reformulation. A free (uncovered) point exists iff
  ∃ a side-assignment σ∈{below,above}^m with R_σ = Δ ∩ {⟨ũ_a,·⟩ on side σ_a} ≠ ∅;
  by 2-D Helly, R_σ≠∅ iff every TRIPLE of {chosen half-planes ∪ triangle edges} is
  jointly feasible. So "covering" = for EVERY σ, some triple is incompatible — a
  SAT/combinatorial condition. The facet sumset (note 08) is the barycentric special
  case where the colorful selection collapses to 1∈ΣF_i.
  WHY STUCK: the general colorful selection needs a "simplex-restricted colorful
  Brunn–Minkowski" — same wall as before (free point must stay in Δ).
  FUTURE RESEARCH: (a) prove a colorful/weighted BM on the simplex; (b) exploit the
  Helly-triple structure for ≤4 planks as a base case; (c) Tverberg-type partitions.

#2  3.2 PERTURBATION  [CONFIRMED: extremal is a strict local min]
  FINDING (computed): Hunter's extremal (3 facet planks, S=1) is a STRICT LOCAL
  MINIMUM — 20k perturbations of directions/positions never beat it (0.967≈1, grid).
  LEARNING: supports S≥1 locally and confirms Hunter rigidity. A necessary condition
  for the conjecture, now verified.
  FUTURE RESEARCH: a global variational/Morse argument — characterize ALL critical
  configurations of Σrw over coverings; show each has S≥1. (Needs the covering
  constraint as a smooth manifold; the boundary cases (plank touching) are the hard
  part.)

#3  3.4 SDP  [tool obtained (cvxpy/SCS); KEY structural learning]
  Installed cvxpy 1.9.2 (SCS, CLARABEL). KEY LEARNING on formulation:
  • The MEASURE side cannot be improved by a moment-SDP: μ(plank)=measure of a SLAB
    is NOT a polynomial-moment functional (it is the measure of a semialgebraic set),
    so the grid-LP value 0.62 IS the exact single-measure optimum; Lasserre-on-μ
    gives nothing better. The 1/2–0.62 cap is fundamental to the measure route.
  • Covering of a FIXED config is LP-certifiable per sign-choice (Helly/Farkas), no
    SDP needed. The genuine SDP opportunity is the DISJUNCTIVE covering program
    (min Σrw s.t. ∪P_a ⊇ Δ) — relaxing the OR over planks. That is exactly the hard
    combinatorial core.
  FUTURE RESEARCH: a Lasserre/moment-SOS relaxation of the disjunctive covering
    program (lift the sign/OR variables), which provably tightens toward 1. This is
    the most concrete numerical path and now has the tooling on R15.

#4  5.2 CONWAY FRIED-POTATO  [connection is one-directional]
  Fried-potato: cut a convex body by n successive hyperplanes minimizing the largest
  inradius of the pieces; its solution USES Bang's theorem (Bang ⟹ fried-potato).
  LEARNING: the implication is forward; INVERTING it (fried-potato ⟹ affine Bang) is
  NOT a clean equivalence — they are different optimizations (inradius vs relative
  width). A genuine link would require the fried-potato OPTIMUM for the triangle to
  coincide with the facet/Hunter cuts.
  FUTURE RESEARCH: compute the fried-potato optimum for the triangle; if its optimal
  first cut is edge-parallel (= Hunter), that gives an inductive bridge.

#5  4.3 DUALITY / HAHN–BANACH  [equivalent to the conjecture]
  LEARNING: the witness measure IS the LP dual; a covering-DEPENDENT separating
  measure exists iff Σrw≥1 (LP-dual-equivalent) ⟹ needs explicit construction.
  Hahn–Banach separation of {a simplex point} from ∪planks reduces to the same.
  FUTURE RESEARCH: construct the dual certificate explicitly for 3 directions using
  the Helly-triple structure (#1).

#6  3.1 HUNTER EQUALITY EXTENSION  [partial]
  Confirmed (via #2) the 3-plank extremal is rigid. Extending "S=1 ⟹ facet config"
  to n planks is open. FUTURE: a stability/rigidity theorem (S close to 1 ⟹ config
  close to facet) — would also bound the approach to the infimum.

#7  1.3 BANG LATTICE WALK  [route obstructed]
  Bang's walk lives on signs {−1,1}^n with potential ‖p(ε)‖² increasing (Prop 8: no
  directed cycle ⟹ a sink = uncovered point). LEARNING: signs do NOT fit the simplex
  (convex coords needed), and we already REFUTED the non-symmetric sign lemma (note
  11, round 2: 7% counterexamples). So the walk must be re-cast on the simplex with a
  NEW potential. FUTURE: define a "convex Bang walk" on the barycentric lattice whose
  potential forces an uncovered vertex; the arrangement-vertex finiteness (note 07,
  2805/2805) is the substrate.

#8  2.3 Σr²≥f(S)  [STUCK, re-confirmed]
  Fine planks drive Σr²→0 with S fixed; no f(S) exists making 1≤2S−Σr² ⟹ S≥1. The
  area measure is genuinely capped at 1/2 this way. FUTURE: a covering-dependent
  second-moment bound (using overlaps), not a universal f(S).

#9  5.1 DAVENPORT / DIOPHANTINE  [untouched, hard]
  Bang ⟷ Davenport-type theorems on lines meeting unit squares ⟷ simultaneous
  Diophantine approximation. LEARNING: the dictionary is real but deep; no quick
  operationalization. FUTURE: formalize the triangle plank covering as a simultaneous
  approximation problem and import a transference/inhomogeneous-approximation theorem.

#10 2.2 NON-COMMUTATIVE  [out of reach]
  Common generalization of affine + complex via operator algebras. Requires machinery
  (Gram matrices over C*-algebras) beyond this toolkit. FUTURE: specialist territory.

#11 5.3 SURFACE MEASURE  [weak]
  Tarski's disk proof uses spherical area on the boundary CIRCLE (curvature). The
  triangle's polygonal boundary has no curvature analog; the perimeter measure gives
  constant >2 (worse than area). LEARNING: no plank-invariant surface measure on
  ∂triangle found. FUTURE: a measure on an ASSOCIATED sphere (e.g. via the Gauss map
  or the (2d−1)-simplex of Ambrus embedded in S^{2d−1}).

=========================================================================
OVERALL HONEST SUMMARY
=========================================================================
SOLVED/CLOSED: 2-direction (sharp), facet-parallel (sharp, all d), vector model,
  SOTA reproduced+understood (2/(1+√d) tight at the reduced simplex).
NEGATIVE/RULED-OUT with certainty: single measure c=1, peeling, splitting,
  NON-SYMMETRIC sign lemma, naive Bang walk.
NEW THIS SWEEP: Helly reformulation of covering (#1); Hunter extremal = strict
  local min (#2, computed).
FRONTIER: NOT expanded. Beating 2/(1+√d) / closing 3 directions remains open
  (Bakaev–Yehudayoff 2026 is the live frontier with heavy machinery).

TOP-3 FUTURE RESEARCH (highest leverage, honest):
  1. Lasserre/moment SDP (#3) — the one route that PROVABLY converges to 1 and could
     give clean certificates for fixed plank counts. Needs an SDP solver.
  2. Simplex-restricted colorful Brunn–Minkowski (#1) — would generalize the one real
     sharp tool we have (the facet sumset).
  3. Fried-potato optimum for the triangle (#4) — cheap to compute, could reveal an
     inductive bridge if the optimal cut is edge-parallel.
