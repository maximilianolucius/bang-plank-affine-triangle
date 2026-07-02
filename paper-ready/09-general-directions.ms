% MILESTONE 09 — Why non-facet directions resist (the open frontier, diagnosed)
% Paper section: §7 (companion to 07-open-core). Precise obstruction analysis.

THE MINIMAL NON-FACET CASE: 2 facets + 1 tilted direction ũ_3=(0,t,1), t∈(0,1).
  In barycentric (λ_1,λ_2) coords (λ_3=1−λ_1−λ_2), the tilted constraint is
  g := ⟨ũ_3,λ⟩ = 1 − λ_1 − (1−t)λ_2, giving the WEIGHTED partition of unity
        λ_1 + (1−t)λ_2 + g = 1.
  Equivalent to covering the triangle Δ by strips in 3 directions e_1,e_2,(1,1−t)
  — i.e. THIS IS the general 3-direction problem (no reduction).

WHY THE SUMSET METHOD (08) FAILS HERE.
  The weighted sumset gives 1 ∈ F_1 + (1−t)F_2 + F_3 ⟸ Σ Leb > weighted total,
  yielding rw_1+(1−t)rw_2+rw_3 ≥ 1 — BUT only for covering the BOX [0,1]², not Δ.
  The free point may land in B∖Δ (where λ_3 = g−tλ_2 < 0, i.e. g<t). Since
  Δ-covering is WEAKER than box-covering, the box bound does NOT transfer to Δ.
  ROOT CAUSE: in the facet case the 3rd constraint is on λ_3 itself (∈[0,1] ⟹
  λ_3≥0 ⟹ point in Δ automatically). For a tilted direction the constraint is on
  the mixture g, which does NOT force λ_3≥0 — the free point escapes Δ.

WHY THE COUPLING METHOD (05) FAILS HERE.
  Take ν uniform in (λ_1, g) (a 2-direction coupling). Then ν(plank_1)=rw_1 and
  ν(plank_3)=rw_3 exactly, but ν(plank_2)=c_2·rw_2 with c_2 = peak of the λ_2-
  marginal of ν. Three uniform marginals are impossible (06·N1), so c_2 > 1
  necessarily, and rw_1 + c_2 rw_2 + rw_3 ≥ 1 with c_2>1 is WEAKER than Σrw≥1.

SUMMARY. The two proven sub-cases sit on opposite sides of a wall:
  • facet-parallel: 3rd constraint on a true coordinate ⟹ free point stays in Δ
    ⟹ sumset/BM closes it (08).
  • 2 directions: only 2 marginals needed ⟹ a uniform-marginal coupling exists
    ⟹ measure closes it (05).
  • 1 tilted direction breaks BOTH: it needs a 3rd marginal (kills coupling) and
    its constraint is a mixture (kills the in-Δ sumset). This is the genuine core.

OPEN PROBLEM (sharp form). Find a tool that finds an IN-Δ free point for a tilted
  constraint — e.g. a sumset/Brunn–Minkowski inequality restricted to a simplex
  (not a box), or a covering-dependent certificate. This is the affine Bang
  conjecture for the triangle.
