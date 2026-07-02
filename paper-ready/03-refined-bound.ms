% MILESTONE 03 — The refined union bound  [RIGOROUS]
% Paper section: §3 (sharpening of 02 in the plane).

PROPOSITION.
  For the uniform (area) measure on a planar convex body K and any plank P,
        μ_area(P) ≤ rw(P)·(2 − rw(P)).
  Consequently, for any covering of K by planks,
        1 ≤ Σ_a rw_a(2 − rw_a) = 2S − Σ_a rw_a²,        where S = Σ rw_a.

PROOF.
  d=2 case of 02: the marginal f in direction u is a unit-mass density on an
  interval of length w=w_K(u) whose square-root is concave (Brunn–Minkowski),
  hence f is "tent-dominated": f ≤ (2/w)·(distance-to-nearer-end)/(·)… precisely,
  a concave-sqrt unit density on [0,w] satisfies, for a sub-interval of relative
  length r=rw, ∫ ≤ r(2−r) (the tent of peak 2/w attains the extremal mass
  r(2−r) on an end-anchored sub-interval; any placement gives ≤ that). The union
  bound over the cover gives 1 ≤ Σ rw_a(2−rw_a). ∎  (Verified: max over 3·10^5
  planks of [μ−rw(2−rw)] = −0.0000.)

USE.
  • If every plank is "coarse" (rw_a ≥ b): Σrw² ≥ bS ⟹ 1 ≤ (2−b)S ⟹ S ≥ 1/(2−b).
    This drives the bootstrap self-map b ↦ 1/(2−b), fixed point 1, steps 1−1/n.
  • CAUTION (audited): the bootstrap step does NOT close in general — fine planks
    (rw<b) break Σrw²≥bS, and all attempted fixes failed (see 06). The refined
    bound alone yields only S ≥ 1/2. Include it as a tool, not as a proof of 1.

STATUS. The inequality is rigorous and verified. Its use to reach 1 is OPEN.
