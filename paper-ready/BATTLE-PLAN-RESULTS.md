# Battle Plan (4 Phases) — Execution Results & Future Vectors
**Bang's affine plank conjecture for the triangle.** Date: 2026-06-28.
All phases RUN. Honest: the frontier (2/(1+√d), Bakaev–Yehudayoff 2026) was NOT
broken; each phase reduces, at its core, to the open problem — but we gained
concrete structure and one positive structural bridge (Phase 2).

> **[CORRECCIÓN 2026-06-30]** Este documento (y su marco "m>3 vs m=3") asume que el caso
> de 3 planks en el triángulo está cerrado por Hunter. **Es FALSO:** Hunter 1993 solo probó
> 2 planks + la caracterización de igualdad; el **caso de 3 planks está ABIERTO** (Verreault
> §2.2.3; B–Y 2026). Las menciones a "Hunter extremal / strict local min / m=3 base case" se
> refieren a la *configuración de igualdad* de Hunter (la curva `{T=1}`), no a un teorema de
> la desigualdad. La frontera real es **m=3 tilted**, no m≥4. Lo nuevo y probado sin Hunter:
> "3 facetas + 1 arbitrario" (`notes/30` §1).

---

## Phase 1 — Lasserre SDP on the Helly triples
**Idea:** covering ⟺ for every side-assignment σ, some Helly *triple* of
constraints is infeasible ⟹ finite polynomial system ⟹ lift to a moment SDP.

**Run & results:**
- **Helly reformulation [DONE].** Free point exists iff ∃σ∈{below,above}^m with
  R_σ = Δ ∩ {sides} ≠ ∅; by 2-D Helly, R_σ≠∅ iff every triple of {chosen
  half-planes ∪ triangle edges} is jointly feasible. The facet sumset is the
  barycentric special case.
- **Dual certificate (LP) [RUN].** For tight 3-direction coverings the witness
  measure attains μ(Δ)=S exactly (certifies the covering's own S≥1), with
  **35–49% of its mass near the simplex vertices** — *partially confirms* the
  Phase-4 "vertex measure" hypothesis. CAVEAT: by LP duality this is the
  *fractional cover of those very planks* ⟹ per-covering ⟹ **circular for a
  universal bound**.
- **Lasserre level-2 emptiness [RUN].** Built the moment SDP (cvxpy/SCS) for
  emptiness of {x∈Δ: p_a(x)≥0 ∀a}, p_a=(⟨ũ_a,x⟩−lo_a)(⟨ũ_a,x⟩−hi_a).
  **Level-2 does NOT distinguish covering from non-covering** (both feasible):
  with non-strict p_a≥0 the closure includes slab *boundaries* (the facetal
  centre is a boundary point), so the set is never strictly empty.

**Learning:** the SDP route is sound but level-2 is too weak. NEEDS **strict
margins p_a ≥ ε and level ≥ 3–4**. The universal bound still requires a UNIFORM
dual (not per-covering) — that uniformity is the open core.

---

## Phase 2 — Conway "fried-potato" optimum  ★ POSITIVE FINDING ★
**Idea:** the optimal cut of the triangle may align with Hunter's facetal config,
giving a hierarchical-decomposition replacement for the failed peeling.

**Run & results (equilateral triangle, n=1 cut):**
- Full inradius 0.500 → **optimal max-inradius after 1 cut = 0.301**, achieved at
  **θ = 150.8° = an edge-normal angle** ⟹ **the optimal cut IS edge-parallel**
  (= Hunter's direction!). Reduction ratio 0.602.

**Learning:** the fried-potato optimum's first cut coincides with the plank
extremal's direction — a genuine structural bridge. This *supports* replacing the
broken "peeling" (which failed on the penetration angle) with a **hierarchical
edge-parallel decomposition**.
**Caveat:** still one-directional (fried-potato ⟸ Bang); proving
"every plank covering refines into edge-parallel cuts without increasing Σrw" is
not done.

---

## Phase 3 — Morse theory on the arrangement (uses the strict local min)
**Idea:** Hunter's extremal is a strict local min; use connectivity + uniqueness
to exclude any global min with S<1, reducing m>3 to m=3.

**Run & results:**
- **Hunter extremal = strict local min [CONFIRMED].** 20k perturbations of
  directions/positions never beat S=1 (0.967≈1, grid). Rigidity holds.
- **m-reduction premise [REFUTED].** True min Σrw over m-plank coverings:
  m=3→0.982, m=4→0.986, m=5→0.979, m=6→0.984 (all ≈1, grid). **The min does NOT
  increase with m** ⟹ "m>3 is overdetermined / S relaxes" is FALSE; m>3 can be as
  tight as m=3. The reduction-to-m=3 argument does not go through this way.

**Learning:** the local-min fact is real but the global argument has a gap — a
unique interior local min does NOT exclude lower values on the boundary of the
(non-compact, stratified) configuration space, and m>3 does not relax. A rigorous
Morse/critical-point argument must handle the boundary strata (planks touching).

---

## Phase 4 — Restricted colorful Brunn–Minkowski (the heart)
**Idea:** use the Phase-1 dual (a vertex-weighted measure) to build
F(x)=Σλ_i·chord(x,u_i); show S<1 ⟹ F<1 on Δ ⟹ not covering (Borsuk–Ulam/Bang),
with the simplex restriction resolved by positivity of the dual.

**Assessment [theoretical, not runnable]:**
- The dual certificate is only known **per-covering** (Phase 1), not as a uniform
  object — so "the" measure to build F from is exactly what's missing.
- "F<1 everywhere ⟹ not covering via Borsuk–Ulam" and "positivity auto-resolves
  the simplex restriction" are **asserted, not proven** — this is precisely the
  open core (the same "free point must stay in Δ" wall, redressed).

**Learning:** Phase 4 is the genuine open problem. It becomes concrete only once
Phase 1 yields a UNIFORM dual; until then the Borsuk–Ulam step has no input.

---

## Overall verdict
The 4-phase strategy is **well-designed** (it correctly welds Helly→SDP→dual→BM),
and produced real structure: **(i)** a positive fried-potato bridge (Phase 2),
**(ii)** a partially vertex-concentrated dual (Phase 1), **(iii)** confirmation of
Hunter rigidity (Phase 3). But **two load-bearing premises failed** (Phase 3's
m-relaxation; Phase 4/1's uniform dual), and **the frontier was not advanced**.

## Future vectors of exploration / improvement (ranked, honest)
1. **Lasserre level 3–4 with strict margins** p_a ≥ ε (Phase 1, concrete & has
   tooling). Goal: certify covering for tight m≤5 and read off an SOS/dual that is
   uniform across positions — the only route with provable convergence to 1.
2. **Fried-potato n=2,3 + a refinement theorem** (Phase 2): prove every plank
   covering refines into successive edge-parallel cuts without increasing Σrw.
   This would be a genuine new inductive engine (replacing peeling).
3. **Make the dual certificate UNIFORM** (Phase 1→4): find a single
   construction (not LP-per-covering) — e.g. a vertex-weighted measure whose
   F(x)=Σλ_i chord(x,u_i) ≥ 1 on Δ. This is the real missing piece.
4. **Rigorous critical-point/Morse analysis** (Phase 3) handling boundary strata
   (plank-tangency) and the non-compactness; combine with the strict-local-min
   fact.
5. **Colorful Carathéodory / Tverberg** for the Helly triples (Phase 1↔4): a
   colorful selection theorem on the simplex generalizing the facet sumset.

---

# ADDENDUM — "Definitive Assault" (Phases A–D) assessment [RUN, REFUTED]
A surgical follow-up plan (Lasserre-4 + Fried-Potato horseshoe). Each phase RUN
and FALSIFIED for a concrete, verified reason:

**Phase A — Lasserre level 3–4 with strict margin ε.** RUN (cvxpy/SCS). It does
NOT distinguish covering from non-covering even at level 4 (all "optimal_
inaccurate" = feasible). ROOT CAUSE: each plank constraint p_a=(⟨ũ_a,x⟩−lo)
(⟨ũ_a,x⟩−hi)≥ε has TWO branches (the slab's two sides); the moment relaxation
cannot resolve this disjunction at low level. The EXACT decision tool is the
sign-cell LP (2^m linear programs), not an SDP. No usable SOS certificate at
practical level.

**Phase B — Depth Lemma + dynamic partition.** REFUTED. The claim "a tilted plank
of relative width r penetrates depth ≤ r" is FALSE: computed shadow_i/r for the
best vertex i over 40k tilted planks → MAX of min_i(shadow/r) = 3.73 (and a facet
plank already has the OTHER two shadows = 2.67·r). Tilting INCREASES the layer-
shadow, not decreases it. The layer construction is a single measure ⟹ capped at
the single-measure ceiling 0.62 (impossibility of c=1). Phase B cannot exceed 0.62.

**Phase C — Morse reduction m>3 → m=3.** Already REFUTED (main Phase 3): min Σrw
≈1 for ALL m (does not increase with m), so m>3 does not relax. The strict-local-
min fact is real but the global/connectivity step has the boundary-strata gap.

**Phase D — SOS dual from Phase A.** Vacuous: it needs Phase A to output a clean
SOS certificate, which does not materialize at practical Lasserre level.

**Net:** the assault is creative and correctly targets the two walls (uniform
dual; m-reduction), but every proposed bypass fails on verification — the depth
lemma is geometrically backwards, and the Lasserre disjunction is impractical.
The walls stand. The one durable positive remains Phase 2 (fried-potato optimal
cut is edge-parallel), but it has no proof-bearing consequence once the depth
lemma falls.

---

# ADDENDUM 2 — "Topological Hall on the sign hypercube" (ILP+Farkas) [RUN, REFUTED]
Plan: encode covering via the Helly sign-cells, bound the per-triple conflict set
W_T ⊂ {±1}³, and combine (LLL / Aharoni–Haxell Hall / ILP-Farkas) to get a free σ.

**Hito 1 — characterize W_T and its claimed Lipschitz bound |W_T| ≤ 4(1−Σr)₊.**
RUN (60k triples, bucketed by Σ_T r). RESULT (max per bucket):
  Σr≈0.5 → #empty(W_T)=7, #free octants=7
  Σr≈1.0 → #empty=7, #free=6
  Σr≈1.5 → #empty=7, #free=4
**REFUTED:** #empty(W_T) reaches 7 even at Σr=0.5 (bound demands ≤2), and #free
octants reaches 4 at Σr=1.5 (bound demands 0). The conflict sets are LARGE
regardless of Σr; the dependence on Σr is weak, NOT the claimed Lipschitz/linear
decay. The Lipschitz bound is the load-bearing premise of Hitos 2–4; it fails.

**Hitos 2–3 — LLL / hypergraph Hall.** Author-acknowledged to fail: LLL needs
P(A_T) ≤ 1/(e·deg), but the dependency degree is O(m²) (triples sharing a plank);
Aharoni–Haxell's expansion condition reduces to 3Σr<3, insufficient.

**Hito 4 — ILP + Farkas dual ⇒ "uniform measure".** The covering of a FIXED
geometry is decidable by 2^m sign-cell LPs (exact). But min Σrw over geometries is
a CONTINUOUS disjunctive program, not a pure ILP. The Farkas/LP dual of a specific
instance is the per-covering witness measure (already shown LP-dual-EQUIVALENT to
the conjecture ⇒ circular). "Generalize the multiplier pattern to all m" = exactly
the open uniform-dual problem. (Numerical min Σrw ≈ 1 for m=3..6 already confirmed.)

**Net:** the ILP route is exact but its combinatorial bound (Hito 1) is false and
its dual is per-instance/circular — it does not escape the two walls.

---
# RUNNING TALLY OF REFUTED BYPASSES (all computationally verified)
single-measure c=1 · area/layer ceiling 0.62 · peeling (penetration angle) ·
splitting (sign error) · non-symmetric sign lemma · naive Bang walk ·
m>3 → m=3 reduction · Lasserre lvl≤4 (disjunction) · fried-potato depth lemma
(shadow grows, not shrinks) · W_T Lipschitz bound (conflict sets large ∀ Σr).
DURABLE POSITIVES: 2-direction (sharp), facet-parallel (sharp), Helly
reformulation, Hunter = strict local min, fried-potato cut = edge-parallel.
THE TWO WALLS (= the open problem): a UNIFORM dual certificate; irreducibility of
m>3. Beating 2/(1+√d) remains Bakaev–Yehudayoff 2026 expert territory.

---
# ADDENDUM 3 — "Universal Dual Measure" plan (Ambrus/CM/BY/Farkas) [assessed]
**FACTUAL CORRECTION:** the SOTA planar bound is 2/(1+√2) ≈ 0.828 (Bakaev–
Yehudayoff 2026), which IMPROVED the older 2/(1+d) = 2/3 (Chambers–Moullié). The
plan inverted these (called 2/3 the new bound).

- **Phase 1 (Ambrus colorful Bang/Carathéodory):** OPEN. Ambrus' Prop 9 deformation
  condition is, in his own words, "uncertain" — not known to cover the simplex.
  The genuine core; not refuted, not closed.
- **Phase 2 (Chambers–Moullié convex-complement, per-region):** REFUTED. C-M needs
  the planks ORDERED so each prefix-complement is convex. TESTED: **0% of generic
  coverings are orderable** (a tilted middle plank splits the complement into two
  pieces ⟹ non-convex). C-M applies only to edge-built coverings (e.g. facetal,
  already handled).
- **Phase 3 (fried-potato + BY):** premise rests on the wrong SOTA value, AND the
  "refinement to edge-parallel cuts without increasing Σrw" needs the depth lemma,
  already REFUTED (shadow grows under tilt).
- **Phase 4 (0-1 Farkas, position-independent dual):** the load-bearing claim
  "Farkas coefficients depend only on r_i, not positions" is FALSE — same r at
  different positions are different coverings with different constraints, hence
  different duals (the witness measure is provably position-dependent).

**Net:** Phase 1 = the open core (untouched-closable); Phases 2,3,4 refuted at
their foundation. Pattern holds: every elaborate bypass collapses onto the two
walls. Honest recommendation: consolidate the solid results; the open problem
needs expert collaboration (Ambrus / Bakaev / Yehudayoff), not more elementary
combinatorial plans.
