# PROJECT NOTE — Attacking the open residual: m≥4 planks on the triangle
> Live research note. The only open triangle case after Hunter (m=3), the
> two-direction theorem, and facet-parallel. Date: 2026-06-28.

## Framing (established)
- Hunter (1993) proved the THREE-plank triangle case. Two directions (any m) and
  facet-parallel (any m) are also closed. The residual is **m≥4 planks, ≥4 tilted
  directions** (equivalently ≥1 genuinely non-facet direction beyond the others).
- Vector/cubical model: m affine functions on Δ; covering ⟺ a set-cover; conjecture
  ⟺ integer min Σrw ≥ 1.

## Finding 1 — the obstruction is an INTEGRALITY GAP (real, not discretisation)
Exact set-cover ILP vs its LP relaxation, refining the mesh K=8→32:
  edge-FACET set {90,210,330°}: LP → ~0.70 (stabilises), ILP = 1.0000 always.
  4 generic directions:         LP → ~0.96 (stabilises), ILP = 1.0000 always.
⟹ The LP/measure bound is genuinely < 1; the conjecture's bound is a property of
the INTEGER cover. No single witness measure (Gardner's c=1 object) can reach it —
consistent with the impossibility. The gap is largest (~0.31) at the most
"facet-like" symmetric configs.

## Finding 2 — symmetric m=4 mostly COLLAPSES; one genuine 4-direction extremal
Among symmetric 4-direction sets, the integer optimum usually activates only ≤3
directions (reducing to Hunter / two-direction):
  0,45,90,135° → 3 active;  0,30,60,90° → 3 active;  22.5°-spaced → 2 active.
The exception, a GENUINE 4-direction extremal: **3 facet directions + 1 tilted
("median")**, integer bins/dir [2,5,6,3], all four active, ILP=1, LP=0.69
(gap 0.31). This is the canonical hard m=4 instance.

## Finding 3 — the dual certificate lives on the BOUNDARY (edges)
For that genuine extremal, the optimal fractional witness (LP dual, mass 0.69)
concentrates: **0% near the vertices, 54% near the EDGES, 46% interior**, with all
four directions equally binding (≈11 tight bins each of 16). ⟹ The certificate is
boundary/edge-based — exactly where Hunter's m=3 proof (crossings of the planks
with the three edges) lives. So the natural attack is to GENERALISE HUNTER'S EDGE
ANALYSIS to ≥4 crossings, but with the integer (combinatorial) structure, since a
mere edge-measure caps at 0.69.

## Finding 4 — the tilted direction is NON-REDUCIBLE but NEUTRAL (answers "4-dir → 3-facet + median?")
Constructed coverings "3 facet bands {λ_k≤a_k} + 1 tilted plank covering the central
residual". The residual {λ_k>a_k ∀k} is a SCALED triangle (factor s=1−Σa_k). Tested
257 such coverings:
- The tilted plank covers the residual with width exactly s ⟹ total Σrw = Σa_k+s = 1
  (exactly tight).
- Re-covering that residual with FACETS costs ≥ s (Hunter on the small triangle);
  worst case the facet re-cover EXCEEDS the tilted width by +0.058. Reduction "facet
  re-cover ≤ tilted width" works in only 2/257 (1%, discretisation ties).
⟹ The 4th (tilted/"median") direction is NOT absorbable by facets with any saving;
it is NON-REDUCIBLE but NEUTRAL (same cost s). Structural reason: removing a FACET
band leaves a triangle (self-similar ⟹ peeling works = the solved case), but removing
a TILTED plank leaves a non-triangular (quadrilateral) residual ⟹ peeling breaks.
This re-confirms m≥4 irreducibility from the reduction angle, and explains WHY the
bound is exactly tight yet not facet-reducible. Edge-crossing structure of the
extremal is asymmetric (two edges heavily crossed, the third barely).

## Open research directions (honest, no guarantee)
1. **Edge-crossing combinatorics** (extend Hunter): parametrise the m planks'
   intersections with the 3 edges; seek the identity/inequality generalising
   R−1=(1−T)²/(2−T) to ≥4 crossings.
2. **Reduction 4-dir → 3-facet + tilted?** Can the tilted (median) direction be
   absorbed into the 3 facets so the facet-parallel theorem closes it? (Tested
   below — see note 13b / the §7 obstruction: the tilted constraint is on a
   mixture and the free point escapes Δ; likely NO, but worth pinning per-extremal.)
3. **An integer (not fractional) certificate** — the true target; the non-symmetry
   barrier. No current technique (measure, chord, polarisation, symplectic,
   colorful Carathéodory) produces it.

## Status
Sharp target identified (the genuine 4-direction extremal), obstruction
characterised (real integrality gap, edge-concentrated certificate). Next: the
edge-crossing analysis. Expert contact (Ambrus, ambrus.gergely@renyi.hu) in
progress — the highest-leverage step.
