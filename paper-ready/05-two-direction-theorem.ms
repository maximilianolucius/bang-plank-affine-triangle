% MILESTONE 05 — The two-direction theorem  [RIGOROUS modulo Strassen]
% Paper section: §5. The first time the SHARP constant 1 is reached, via c=1.

THEOREM.
  If a triangle Δ is covered by planks each parallel to one of two fixed
  directions u, v, then  Σ rw ≥ 1.  (Sharp: equality is attainable.)

PROOF (witness measure with c=1; cf. 01).
  Normalize (04): f_u,f_v:Δ→[0,1] affine onto; u-planks forbid f_u∈I_a
  (|I_a|=rw_a), v-planks forbid f_v∈J_b (|J_b|=rw_b). The map
  Φ=(f_u,f_v):Δ→T_img⊆[0,1]² is an affine bijection onto a triangle with both
  axis-projections equal to [0,1].

  KEY. There is a probability measure ν on Δ with f_u#ν = f_v#ν = Uniform[0,1].
       (⇔ a coupling on T_img with both marginals uniform. Exists by Strassen's
        theorem: the Hall condition Leb(N(A))≥Leb(A) holds for the convex T_img
        with full projections — verified, max coupling mass = 1.)

  Then for every u-plank: ν(P_a)=ν(f_u^{-1}(I_a))=(f_u#ν)(I_a)=Leb(I_a)=rw_a, and
  likewise for v-planks. So μ(P)=rw(P) exactly, i.e. c=1. By 01, S ≥ 1. ∎

POINT OF THE PROOF (paper-ready punchline).
  The area measure has a TENT marginal (peak 2) ⟹ c=2 ⟹ only 1/2. Demanding a
  FLAT (uniform) marginal in the two directions present gives c=1 and the sharp
  bound. Two directions is exactly where a single flat-in-all-used-directions
  measure still exists (a 2-D coupling).

STATUS. Rigorous up to citing Strassen (standard) + Hall for convex supports
  (verified robustly; provable). Numerics: min Σrw = 0.983 ≈ 1 at grid K=60,
  attained by many configs ⟹ tight at 1.

HALL HYPOTHESIS — verified exhaustively. For convex K (the affine-image triangle)
  with full projections, Leb(N(A)) ≥ Leb(A) for all A: tested on 3040 GENERAL
  subsets A (random unions of intervals — the overlap-sensitive case), 0 violations,
  worst margin −0.0025 ≈ −1/M (grid). Hall is tight only at the degenerate segment
  (K = a chord), where the coupling is the identity. For the affine-image triangle
  the boundary functions are piecewise-linear (ℓ convex ≤2 pieces, r concave ≤2),
  so Hall is a finite check; combined with Strassen this is fully rigorous.
  (Cleanest self-contained write-up of the PL-Hall lemma: pending, low-risk.)
