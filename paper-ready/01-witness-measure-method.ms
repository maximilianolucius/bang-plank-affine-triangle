% MILESTONE 01 — The witness-measure method  [RIGOROUS]
% Paper section: §2 (the framework underlying everything).

STATEMENT (Lemma).
  Let K ⊂ R^d be a convex body covered by planks P_1,…,P_n. Suppose there is a
  Borel probability measure μ on K and a constant c>0 with
        μ(P_a) ≤ c · rw(P_a)      for every plank P_a.
  Then  Σ_a rw(P_a) ≥ 1/c.

PROOF.
  1 = μ(K) ≤ μ(⋃_a P_a) ≤ Σ_a μ(P_a) ≤ c Σ_a rw(P_a).  ∎

REMARKS (paper-ready).
  • This is LP duality: μ is a feasible dual to the covering LP; 1/c is the
    bound it certifies. The whole game is the best constant c attainable.
  • The recurring theme of the paper: choosing μ to FLATTEN the marginals.
      – area measure ⟹ c = d  (marginal peak d/w);     gives 1/d.
      – uniform-marginal measure in the used directions ⟹ c = 1; gives 1.
  • Hard barrier (see 06): a single μ cannot achieve c=1 against ALL directions
    simultaneously when d≥2, so the sharp bound 1 is not a single-measure fact
    beyond special direction sets (e.g. ≤2 directions in the plane).

STATUS. Fully rigorous, elementary. Foundation for 02, 03, 05.
