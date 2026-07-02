% MILESTONE 06 — Negative & structural results  [RIGOROUS / AUDITED]
% Paper section: §6. These shape the problem and prevent dead ends.

N1. SINGLE-MEASURE CEILING.  [RIGOROUS]
  No single probability measure μ on Δ achieves c=1 against all directions.
  c=1 needs marginal density ≤ 1/w_K(u) in every u, i.e. uniform marginals
  everywhere. On the standard simplex, uniform marginal in e_k forces E[x_k]=1/2;
  but Σx_k=1 gives Σ_k E[x_k]=1 ≠ (d+1)/2 for d≥2. Contradiction.
  ⟹ the union-bound/witness-measure route is capped in [1/2, 1); the sharp 1
     requires the covering's COMBINATORICS (an integrality-gap phenomenon).
  This explains cleanly why 1/2 is easy and 1 is hard.

N2. PEELING / SIMILAR-TRIANGLE FALLACY.  [AUDITED FALSE]
  "Remove a fine plank P (rw=ρ); the complement contains a triangle similar to T
   of scale 1−ρ, covered by the rest" — FALSE for a generic fine plank.
  The cut by a bounding line of P is parallel to an edge only if u_P ⊥ that edge.
  Verified: for a tilted plank the cut leaves a QUADRILATERAL; the largest
  similar cap has scale 0.55, not 1−ρ=0.85; the rescale ratio is non-constant
  (1.16,1.55,1.39,1.04,1.00 vs the required 1.176). Affine invariance gives
  perpendicular OR adjacent, not both. DO NOT USE.

N3. SPLITTING SIGN-ERROR.  [AUDITED FALSE]
  Splitting planks to make all rw_a small drives Σrw²→0, which WEAKENS
  1≤2S−Σrw² to 1≤2S (only S≥1/2). It does NOT give S≥1/(2−b): that needs
  Σrw² LARGE (≥bS), the opposite. Counter: S=0.60 satisfies 1≤2S−Σrw² for all
  splits yet 0.60<2/3. DO NOT USE.

N4. MERGING IS VACUOUS GENERICALLY.  [STRUCTURAL]
  Merging parallel planks raises Σrw² but generic coverings have all-distinct
  directions, so nothing is parallel — the move is empty in the generic case.

TAKEAWAY for the paper. The sharp bound is genuinely combinatorial; present the
1/2 (and 1/d) results, the sharp 2-direction result, and frame the gap honestly.
