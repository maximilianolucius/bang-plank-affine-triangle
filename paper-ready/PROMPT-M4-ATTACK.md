# Research task: prove (or refute) the m≥4 case of Bang's affine plank conjecture for the triangle

You are a research mathematician. Your job is to make genuine progress on a SINGLE
open problem, starting from established results. **Absolute rigor is mandatory.**
A plausible-sounding narrative is worthless; only a verifiable proof, a verifiable
counterexample, or an honestly-labelled partial result counts. Read the
ANTI-FABRICATION RULES at the end FIRST — prior attempts failed by ignoring them.

## 1. The problem
A *plank* is a slab `P={x : α ≤ ⟨u,x⟩ ≤ β}`. For a convex body `K`, the *relative
width* of `P` is `rw(P)=width(P)/w_K(u) ∈[0,1]` (affine-invariant). Bang's affine
conjecture: if planks `P_1,…,P_n` cover `K`, then `Σ rw(P_a) ≥ 1`.

It is OPEN. We work on the **triangle** `T` (the planar simplex).

> **[CORRECCIÓN 2026-06-30]** Este prompt fue escrito asumiendo que "m=3 está cerrado por
> Hunter" y que la frontera empieza en m≥4. **Eso es FALSO.** Hunter 1993 solo probó el
> caso de 2 planks y la *caracterización de igualdad* `Σrw=1 ⟺ T=1`; el caso de **3 planks
> en el triángulo está ABIERTO** (Verreault §2.2.3; B–Y 2026). La verdadera frontera limpia
> es **m=3 con 3 direcciones tilted**, no m≥4. Casos realmente PROBADOS para el triángulo:
> 1 plank; 2 planks; ≤2 direcciones (AKP); facet-parallel (sumset); y "3 facetas + 1
> arbitrario" (`notes/30` §1). Reinterpretar la tarea de abajo: atacar **m=3 tilted**
> primero (es el caso abierto más limpio); m≥4 viene después.

For the triangle the conjecture is PROVEN only in the cases listed above; the open
residual to attack (reframed) is:
> **m ≥ 3 planks using ≥ 3 effective (genuinely tilted, non-facet) directions — open
> already at m=3.**

## 2. The clean arena (use this model)
By affine invariance `T` = standard 2-simplex `Δ={x∈ℝ³ : x_i≥0, Σx_i=1}`. Evaluating
the `m` plank forms gives an affine embedding `Φ:Δ ↪ [0,1]^m`, image
`Q=conv(q_1,q_2,q_3)` (a 2-D triangle in the m-cube, each coordinate ranging over the
full `[0,1]`). Each plank becomes a coordinate slab `{y_j ∈ I_j}`, `|I_j|=rw_j`.
**Cubical conjecture:** if `Q ⊆ ⋃_j {y_j∈I_j}` then `Σ|I_j| ≥ 1`.
Equivalently it is the **minimum of a geometric SET-COVER**: choosing forbidden
sub-intervals in each coordinate of total length `Σ|I_j|` so every point of `Q` lands
in some forbidden slab. The conjecture ⟺ the integer minimum is `≥ 1`.

## 3. PROVEN results you may freely use (do not reprove)
- **Two-direction theorem** (any number of planks in 2 fixed directions ⟹ Σrw≥1):
  a coupling on `Q` with both coordinate marginals uniform gives a witness measure
  with constant `c=1` (Strassen). [= Akopyan–Karasev–Petrov 2019.]
- **Facet-parallel theorem** (any m, all dimensions): if every plank is parallel to a
  facet (slab `{λ_i∈I_i}` in barycentric coords), a free point exists iff
  `1∈F_1+…+F_{n+1}` (Minkowski sum of free sets `F_i=[0,1]\I_i`); 1-D Brunn–Minkowski
  gives `Σ Leb F_i ≤ n` when covered, i.e. `Σrw≥1`. Short and sharp.
- **Hunter (1993):** classified the **equality** case for three planks on a triangle —
  `Σrw=1 ⟺ T=t_1+t_2+t_3=1` (`R−1=(1−T)²/(2−T)` is the equality form). He did **NOT**
  prove `Σrw≥1` for 3 planks; **m=3 is OPEN** (Verreault; B–Y 2026). Do not treat as closed.
- **3 facets + 1 arbitrary plank (triangle):** `Σrw≥1` — proved Hunter-free in `notes/30`
  §1 (fiber argument). This is the genuine new closed subcase.
- **1/d bound and `1≤2S−Σrw²`** in the plane (area measure).

## 4. FIRM structural findings about the residual (use as constraints/clues)
- **The obstruction is an INTEGRALITY GAP, and it is REAL.** The set-cover LP
  relaxation stabilises at ≈0.70 (<1) as the mesh refines, while the integer optimum
  is exactly 1. ⟹ **No single witness measure / fractional certificate can reach 1**
  (consistent with Gardner's impossibility). A winning argument must use the INTEGER
  (combinatorial) structure, not a probability measure.
- **The dual certificate concentrates on the BOUNDARY:** the optimal fractional
  witness puts ~54% of its mass near the three edges, 0% near the vertices, with all
  directions equally binding. (This is where Hunter's m=3 proof — crossings of the
  planks with the 3 edges — lives.)
- **m≥4 is genuinely IRREDUCIBLE** (do not try to reduce to m=3): 95% of m=4 coverings
  have all planks essential; the tilted direction is non-reducible to facets (it is
  exactly as efficient, not less); removing a tilted plank leaves a non-triangular
  residual (peeling breaks); the tilted sumset escapes Δ.
- **Exact ILP confirms** the integer minimum is `1.0000` in every tested direction set
  (3–6 directions). So the conjecture is almost certainly TRUE here; your goal is a
  PROOF (or, if you believe it false, an explicit covering with `Σrw<1`, which would
  be a historic counterexample — held to the same rigor).

## 5. REFUTED routes — do NOT propose these (each has a proven fatal flaw)
- **Single fixed witness measure** (any positive measure): capped at `c*≈1.60` ⟹ ≤0.62;
  cannot reach 1 (the integrality gap is real).
- **Reduction m≥4 → m=3** (Helly / deletion / merging): irreducible; a *quantifier swap*
  — Hunter gives a free point in SOME sign-chamber per triple, not a common one.
- **Zonotope / support-function** `Σ(w_i/2)[-u_i,u_i]`: **position-independent**, but
  covering is position-dependent; verified that valid coverings (e.g. the 3 facet
  planks) violate `W_Z≥W_Δ` in all directions. Same as 0-1 Farkas. Dead.
- **Entropy / log-sum potentials, or any "escape SOME plank" criterion:** *quantifier
  swap* — a covering failure needs a point escaping ALL planks simultaneously; a
  global min of a sum/average only escapes some. Dead.
- **Topological nerve / KKM on the cube:** the claim "Σ|I_j|<1 ⟹ nerve non-contractible"
  is the conjecture in disguise (unproven), AND false as a detector: boundary failures
  leave a contractible union (β₁=0), so topology gives no signal where the real free
  points are.
- **Toric / BKK / Euler–Jacobi:** the gradient system has non-Laurent denominators;
  cleaning them gives a dense resultant ≡ 0 (roots at infinity). Dead without blow-ups.
- **Straightening flow** (rotating tilted planks to facet normals): the relative width
  *increases* in 68% of configs; not monotone. Dead without coupled cell dynamics.
- **Lasserre/SOS up to level 4, peeling, Σrw²≥f(S), polynomial polarization** (needs
  symmetry), **symplectic** (capped at 3/4): all refuted or insufficient.

## 6. What a WINNING certificate must satisfy (the synthesised target)
From the findings, any argument that closes m≥4 must be SIMULTANEOUSLY:
1. **integer / combinatorial** (not a fractional measure) — from the real gap;
2. **position-dependent** (uses where the planks sit, not just normals+widths);
3. **boundary/edge-based** (the free points live near the edges);
4. **of "escape-ALL" (sup) type**, not sum/average — from the quantifier-swap lesson.
No known technique meets all four. A genuine advance either (a) builds such an object,
or (b) extends Hunter's edge-crossing identity `R−1=(1−T)²/(2−T)` to ≥4 edge crossings,
or (c) proves a simplex-restricted (free-point-stays-in-Δ) Brunn–Minkowski/sumset
inequality for one tilted direction added to facets.

## 7. Deliverable
Either: a complete rigorous proof of the cubical conjecture for m≥4; OR a verified
explicit counterexample; OR a genuinely new, fully-proved PARTIAL result (e.g. a clean
subfamily: 3 facets + 1 specific tilted direction; or m=4 with a stated symmetry),
clearly delimiting what is and isn't proven. State all lemmas with proofs; mark every
unproven step.

## ANTI-FABRICATION RULES (read first; prior attempts failed here)
- **Confirming the conjecture numerically is NOT a proof.** "0 violations over N
  samples/cells", "100% of random configs", "the optimizer found gap>0" only restate
  that the conjecture is true — which is already known exactly via ILP. Do not present
  such evidence as a proof or "computer-assisted certificate" unless you exhibit an
  actual rigorous certificate (an explicit SOS identity, or interval arithmetic whose
  cell size × Lipschitz bound < the local margin EVERYWHERE including near {Σrw=1},
  where the margin →0 — show the refinement handles this).
- **Separate PROVEN from CONJECTURED in every paragraph.** Label asserted steps.
- **No grandiose language** ("inattackable", "irrefutable", "definitive pillar").
  It is a tell for hand-waving. Write like a referee who will reject on the first gap.
- **Self-audit each claim against §5–§6:** does it secretly assume a positive measure
  (gap)? a single sign-chamber (quantifier swap)? position-independence? escape-SOME?
  If yes, it is already refuted — discard it.
- If you cannot prove it, say so explicitly and report the precise obstruction. An
  honest "I reduced it to lemma L, which I could not prove, and here is why L is hard"
  is far more valuable than a false proof.
