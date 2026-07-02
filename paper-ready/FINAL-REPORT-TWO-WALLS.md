# FINAL REPORT — Bang's Affine Plank Conjecture for the Triangle: Resolved Status of the Investigation
**Date: 2026-06-28.** This consolidates DEEP-RESEARCH-TWO-WALLS.md and
PROMPT-TWO-WALLS.md into the complete, rigorous, honest final state of our
investigation. The underlying conjecture is OPEN (since Bang 1951; actively
researched, latest Bakaev–Yehudayoff 2026). This report "resolves" the research
documents — it does NOT fabricate a proof of the open conjecture.

> **[CORRECCIÓN CRÍTICA 2026-06-30 — verificada contra fuentes]** Este documento afirmaba
> en varios puntos que "el caso de 3 planks en el triángulo está cerrado por Hunter (1993)"
> y que la frontera abierta empieza en m≥4. **ESO ES FALSO.** Verreault (survey, §2.2.3,
> verbatim: *"the case of a covering by three planks is still open"*) y Bakaev–Yehudayoff
> (2026, "open even in the plane") confirman que **el caso de 3 planks ya está ABIERTO**.
> Hunter 1993 ("Some special cases of Bang's inequality") solo probó (i) el caso de **2
> planks** en el plano y (ii) la **caracterización de igualdad** `Σrw=1 ⟺ t₁+t₂+t₃=1`;
> NO la desigualdad `Σrw≥1` para 3 planks arbitrarios. La verdadera frontera limpia es
> **m=3 con 3 direcciones tilted**. (Lo que SÍ se probó nuevo y sin Hunter: "3 facetas + 1
> plank arbitrario", `notes/30` §1.) Las afirmaciones de abajo quedan corregidas en
> consecuencia.

## 0. One-paragraph verdict
For the TRIANGLE, the affine plank conjecture `Σrw ≥ 1` is **PROVEN for: ≤2 planks; any
number of planks in ≤2 directions (AKP 2019); facet-parallel families (all d); and "3
facet-parallel planks + 1 arbitrary plank" (`notes/30` §1, Hunter-free)**. It is **OPEN
already for 3 planks in 3 genuinely tilted directions** (Verreault; B–Y 2026) — Hunter
1993 only classified the *equality* case (`Σrw=1 ⟺ T=1`), it did NOT prove the 3-plank
inequality. In the open range the best proven bound is `Σrw ≥ 0.928` (B–Y method on the
equilateral triangle, above the universal 0.828). The open core coincides, after the
vector/cubical reduction, with a **simplex-restricted sumset / non-symmetry barrier** —
the same obstruction blocking the general conjecture in the literature.

## 1. PROVEN (rigorous)
| Case | Result | Source |
|---|---|---|
| 1 plank | `rw ≥ 1` | trivial |
| 2 planks, any body | `Σrw ≥ 1`, equality classified | Hunter 1993 (Proc. AMS 117(3):819) |
| 2 directions, any m | `Σrw ≥ 1`, sharp | AKP 2019 (elementary); = our uniform-marginal coupling |
| 3 planks, triangle | Hunter classified **equality only** (`Σrw=1 ⟺ T=t₁+t₂+t₃=1`); the **inequality `Σrw≥1` is OPEN** | Hunter 1993 (equality); Verreault: 3-plank still open |
| 3 facets + 1 arbitrary, triangle | `Σrw ≥ 1` | ours, `notes/30` §1 (fiber argument, Hunter-free) |
| Facet-parallel, any m, all d | `Σrw ≥ 1`, sharp | ours: 1-D Brunn–Minkowski / sumset `1∈ΣFᵢ` |
| Any covering, universal | `Σrw ≥ 2/(1+√d)` (≈0.828, d=2) | Bakaev–Yehudayoff 2026 |
| Triangle, universal, any m | `Σrw ≥ 0.928` | B–Y chord/width evaluated on the equilateral triangle (min ℓ/w = 0.928) |

## 2. THE SINGLE OPEN RESIDUAL (precise)
**Triangle, m ≥ 3 planks in ≥ 3 tilted directions** (already open at m=3). Equivalent clean forms:
- **Cubical:** `Q=conv(q₁,q₂,q₃)⊂[0,1]ᵐ` (affine triangle, every coordinate full
  range `[0,1]`); if `Q ⊂ ⋃ₐ{y_a∈I_a}` then `Σ|I_a| ≥ 1`. (the m=3 tilted case is itself
  OPEN — Hunter did equality only; the facet/coordinate-aligned case = our sumset; the
  open part is the genuinely tilted, ≥3-direction range.)
- **Simplex-restricted sumset:** for 3 affine `f_u,f_v,f_w` on Δ with one relation
  `αf_u+βf_v+γf_w=κ`, a free point with `f∈F` exists when `Σ|F|` is large enough,
  but the free point must lie IN Δ (the image triangle), not just on the plane — the
  exact wall. Facets (`Σλᵢ=1`) are where the relation keeps the point in Δ.

**Verified facts about the residual:**
- min Σrw ≈ 1 for m=3,4,5,6 (does NOT increase with m).
- m≥4 does NOT reduce to m=3: 95% of m=4 covers have all 4 planks essential.
- Hunter's m=3 identity has no closed-form m≥4 extension we could find.
- **EXACT ILP confirmation (set-cover):** for every tested direction set (3,4,5,6
  directions, random + edge-normals+extras), the EXACT integer minimum of Σrw is
  **1.0000** — no sub-1 covering exists, via exact integer optimization (not random
  search). The fractional/LP relaxation is < 1 (the integrality gap; e.g. 0.706 at
  edge-normals); the integer optimum is achieved either by the trivial single
  full-width plank (generic directions) or by the Hunter/facet 3-way split
  (edge-normals). This is the strongest numerical evidence short of a proof
  (discretized; finite direction sets) — it does NOT constitute a proof.

## 3. THE OBSTRUCTION MAP (why it is hard — literature-confirmed)
**Both walls are ONE barrier: NON-SYMMETRY.** Every known `c=1`/exact method needs
central symmetry of `K`, or a cross-family symmetry hypothesis that fails for ≥3
generic plank directions on a non-symmetric body:
- **Gardner 1988:** the `c=1` relative-width measure for ALL directions does not
  exist (R³, and the all-direction version in R²) — Wall 1 is a theorem.
- **B–Y 2026:** `2/(1+√d)` is the intrinsic ceiling of chord-normalization (perfect
  square, both factors tight); the residual gap to `c=1` is exactly Gardner's
  missing measure ⟹ Wall 1c ≡ Wall 1a.
- **Polynomial/polarization** (Ortega-Moreno, Glazyrin–Karasev–Polyanskii, Zhao,
  Jiang–Polyanskii): gives point-witnesses for centered/symmetric planks; **real
  unequal-width affine case provably fails**.
- **Symplectic** (AKP 2019): capped at 3/4 for the triangle (medial Minkowski
  billiard length 3/2 < 2).
- **Ambrus 2023 colorful-Carathéodory:** needs `⟨uᵢ,vⱼ⟩=⟨uⱼ,vᵢ⟩`, fails for ≥3
  generic directions.

## 4. ROUTES REFUTED WITH CERTAINTY (do not revisit)
single fixed measure c=1 · area/perimeter/layer measure (c≥2, perimeter c=∞) ·
peeling (penetration angle) · splitting (Σrw²→0 wrong way) · non-symmetric sign
lemma · Σrw²≥f(S) · m>3→m=3 reduction · Lasserre lvl≤4 (slab disjunction) ·
fried-potato depth lemma (shadow grows) · Chambers–Moullié orderability (0% generic)
· W_T Lipschitz bound · 0-1 Farkas position-independence · cyclic two-direction
Gardner certificate (E′>S found).

## 5. BEST PATHS FORWARD (honest, no guarantee)
1. **Semialgebraic critical-cover enumeration** of the residual (m=4, 3 directions):
   stratify the 2ᵐ sign cells, find active templates at the minimum, certify
   `Σrw−1≥0` by Bernstein/interval arithmetic. Computer-assisted, rigorous if it
   closes.
2. **Transverse stability of the equality variety {T=1}:** prove `Σrw−1 ≥ c·d²`
   off the Hunter curve (our perturbation data: strict local min). Would pin the
   infimum if combined with a compactness/degeneracy analysis.
3. **A new certificate TYPE surviving non-symmetry** — signed/vector measure,
   non-homogeneous polynomial device, or a Gardner-measure relaxation exploiting
   that a real covering cannot use only "bad" directions. This is the genuine
   research frontier; no current technique achieves it.
4. **Expert collaboration** (Ambrus / Bakaev / Yehudayoff / Karasev) — the residual
   is at the 2026 frontier.

## 6. Honest closing
The investigation is **complete and at its rigorous limit.** We proved two sharp
theorems (2-direction; facet-parallel, all dimensions), gave the cleanest known
statement of the open residual (the cubical theorem), built a literature-confirmed
obstruction map, and eliminated ~15 routes with certainty. The residual **m≥3 tilted**
triangle case (open already at m=3) — equivalently the simplex-restricted sumset /
non-symmetry barrier —
**remains open**, in line with the entire field. No proof of it is claimed; none was
fabricated. That is the resolved, truthful state of the work.
