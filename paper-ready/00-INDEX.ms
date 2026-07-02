% ============================================================================
% MILESTONE INDEX — Bang's affine plank conjecture for the triangle
% Paper-ready record of results. Status tags: [RIGOROUS] [NUMERICAL] [OPEN]
% Last updated: 2026-06-28
% ============================================================================

PROJECT GOAL
  Prove (or advance) Bang's affine plank conjecture for the triangle:
  every covering of a triangle by planks has  S := Σ rw(P_a) ≥ 1.
  By Ambrus's reduction (simplices ⟹ general convex bodies), the triangle
  case implies the planar affine conjecture.

INTELLECTUAL-HONESTY POLICY
  The full conjecture is OPEN. Nothing here claims to prove S ≥ 1 in general.
  Every file marks exactly what is proven, what is numerical, what is open.

% ----------------------------------------------------------------------------
PAPER-READY RESULTS (solid, includable)
% ----------------------------------------------------------------------------
  01-witness-measure-method.ms   [RIGOROUS]  LP-duality framework: a measure ν
                                 with ν(P)≤c·rw(P) ∀planks ⟹ S ≥ 1/c.
  02-one-over-d-theorem.ms       [RIGOROUS]  S ≥ 1/d for any convex body in R^d
                                 (S≥1/2 in the plane), via Brunn–Minkowski.
                                 Sharp at the simplex. Self-contained, elegant.
  03-refined-bound.ms            [RIGOROUS]  μ_area(P) ≤ rw(2−rw), i.e.
                                 1 ≤ 2S − Σrw². The sharpened union bound.
  04-vector-reduction.ms         [RIGOROUS]  Triangle ↔ standard 2-simplex:
                                 planks = (ũ_a∈[0,1]³ min0 max1, interval I_a).
                                 Clean linear/affine reformulation; kills the
                                 "similar-triangle" geometry trap.
  05-two-direction-theorem.ms    [RIGOROUS*] S ≥ 1 when planks use only TWO
                                 directions, via a witness measure with c=1
                                 (uniform marginals). *modulo Strassen (standard).
  08-facet-parallel-theorem.ms   [RIGOROUS]  S ≥ 1 for ANY number of FACET-
                                 PARALLEL planks on the n-simplex, ALL dimensions,
                                 via 1-D Brunn–Minkowski (sumset). Sharp. Breaks
                                 the single-measure ceiling combinatorially.

  TWO complementary SHARP sub-cases now proven by two different methods:
    • 2 directions (any)        → uniform-marginal coupling (measure, c=1).
    • facet-parallel (any #, ∀d)→ sumset / 1-D Brunn–Minkowski.
  Open: 3+ NON-facet directions (the image is a strict sub-triangle; neither
  method applies). See 07-open-core.ms.

% ----------------------------------------------------------------------------
NEGATIVE / STRUCTURAL RESULTS (guide the paper, prevent dead ends)
% ----------------------------------------------------------------------------
  06-negative-results.ms         Single-measure methods are capped in [1/2,1):
                                 c=1 needs uniform marginals in all directions,
                                 impossible on the simplex for d≥2. Also: the
                                 audited failures (peeling/similar-triangle;
                                 splitting sign-error) — documented so they are
                                 not repeated.

% ----------------------------------------------------------------------------
OPEN CORE (the genuine difficulty)
% ----------------------------------------------------------------------------
  07-open-core.ms                [OPEN]  3+ directions: no single witness
                                 measure reaches c=1; needs the covering's
                                 combinatorics. The affine (non-symmetric) Bang
                                 lemma on the vector model is the target.

% ----------------------------------------------------------------------------
SUPPORTING NOTES (in ../notes/)
% ----------------------------------------------------------------------------
  notes/07  elegant-measure-plan      notes/10  vector-reduction
  notes/08  the-1-over-d-theorem      notes/11  bang-lemma-formalization
  notes/09  fibonacci-bootstrap(WRONG-superseded)  notes/12 two-direction-theorem

SUGGESTED PAPER STRUCTURE
  §1 Intro + Ambrus reduction.   §2 Witness-measure method (01).
  §3 The 1/d theorem (02,03).    §4 Vector model of the simplex (04).
  §5 The two-direction theorem, sharp (05).   §6 Obstructions & open core (06,07).
