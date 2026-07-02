% MILESTONE 02 — The 1/d theorem  [RIGOROUS]
% Paper section: §3. Self-contained, no John ellipsoid, no Bang's lemma.

THEOREM.
  Let K ⊂ R^d be a convex body covered by planks P_1,…,P_n
  (plank P_a: unit normal u_a, width w_a, rw(P_a)=w_a/w_K(u_a),
   w_K(u)=max_{x∈K}⟨u,x⟩−min⟨u,x⟩). Then  Σ_a rw(P_a) ≥ 1/d.
  In the plane (d=2): Σ rw ≥ 1/2.  The constant 1/d is sharp (simplex).

PROOF (via 01 with μ = uniform measure on K, c = d).
  Fix a direction u; normalize ⟨u,·⟩ to range over [0,w], w=w_K(u). The marginal
  density is f(t)=V(t)/vol(K), V(t)=vol_{d−1}(K∩{⟨u,·⟩=t}).
  By Brunn–Minkowski, g:=V^{1/(d−1)} is concave on [0,w].

  Lemma. f≥0, ∫_0^w f =1, g=f^{1/(d−1)} concave ⟹ max f ≤ d/w.
  Pf. At the peak t* of g, concavity+g≥0 give g(t) ≥ g(t*)·h(t), h the tent
      (h(0)=h(w)=0, h(t*)=1, linear). So f=g^{d−1} ≥ (max f)·h^{d−1}, hence
      1=∫f ≥ (max f)∫_0^w h^{d−1} = (max f)·(w/d). Thus max f ≤ d/w. ∎

  Therefore for any plank P={a≤⟨u,·⟩≤b}:  μ(P)=∫_a^b f ≤ (d/w_K(u))(b−a)=d·rw(P).
  Apply 01 with c=d. ∎

SHARPNESS. Equality iff V(t) ∝ tent^{d−1}, i.e. cone/simplex cross-sections.
  d=2 triangle: c=2 (num. 1.999). d=3 simplex: c=3 (num. 2.909).
  Non-simplices are easier: disk c=4/π≈1.27.

STATUS. Fully rigorous and verified numerically (max_P μ(P)/rw(P) matches c_d).
  This is the clean base bound the whole bootstrap starts from.
