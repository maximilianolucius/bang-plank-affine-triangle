% MILESTONE 04 — Vector model of the simplex covering  [RIGOROUS]
% Paper section: §4. Removes all complement-geometry; everything becomes linear.

REDUCTION.
  By affine invariance, the triangle ≡ the standard 2-simplex
        Δ = { x ∈ R³ : x_i ≥ 0, Σ x_i = 1 }.
  Each plank P_a normalizes (shift by a constant on Σx_i=1, then scale) to:
        a covector  ũ_a ∈ [0,1]³  with  min_i ũ_{a,i}=0,  max_i ũ_{a,i}=1,
        and an interval  I_a ⊆ [0,1]  with  |I_a| = rw_a,
  so that  P_a = { x ∈ Δ : ⟨ũ_a, x⟩ ∈ I_a }.

  COVERING ⟺ ∀ x∈Δ ∃ a : ⟨ũ_a,x⟩ ∈ I_a.
  CONJECTURE: covering ⟹ Σ_a |I_a| ≥ 1.

PROBABILISTIC FORM (bridge to a Bang-type lemma).
  A point x∈Δ is a probability distribution on {1,2,3}; f_a(x):=⟨ũ_a,x⟩ = E_x[ũ_a]
  is affine with f_a(e_min)=0, f_a(e_max)=1. Contrapositive:
     Σ|I_a| < 1  ⟹  ∃ distribution x with  E_x[ũ_a] ∉ I_a  ∀a  (an uncovered point).
  The forbidden region is an intersection of pairs of half-spaces — a linear,
  extreme-point problem (no similar-triangle geometry).

WHY IT MATTERS.
  • Verified numerically (62 coverings, min Σrw=1.15; area bound recovered).
  • It is the right arena: the failed peeling arguments died on the geometry of
    T∖P; here that geometry is gone. All difficulty sits in ONE linear lemma.

STATUS. Rigorous reformulation. The linear lemma it isolates is the open core (07).
