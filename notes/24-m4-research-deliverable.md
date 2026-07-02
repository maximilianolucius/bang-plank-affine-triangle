# Research deliverable — m≥4 triangle case (Bang affine plank conjecture)
> Date: 2026-06-29. **Status: OPEN** (no full proof, no verified counterexample).
> Strict labeling: **[PROVED]**, **[PARTIAL / REDUCED]**, **[CONJECTURED]**, **[REFUTED]**, **[NUMERICAL ONLY — NOT PROOF]**.
>
> **[CORRECCION CRITICA 2026-06-30 — auditoria]** En §3 y en la tabla de §6, "Hunter m=3
> [PROVED]" debe leerse con cuidado: Hunter (1993) probó el caso de DOS planks y la
> CARACTERIZACION DE IGUALDAD `Σrw=1 ⟺ T=1` (las identidades `(2−T)(2−S)=1`, `R−1=(1−T)²/(2−T)`
> describen la FRONTERA DE IGUALDAD/config extremal, no la desigualdad general). El caso de
> TRES planks arbitrarios sobre el triángulo **sigue ABIERTO** (Verreault §2.2.3;
> Bakaev-Yehudayoff 2026). El argumento de obstrucción estructural de §3 (por qué m=3 no
> porta a m=4) NO depende de esto y permanece válido como observación. Lo realmente probado
> hacia Bang(3) es el subcaso "3 facetas + 1 arbitrario" (`notes/30` §1).

---

## Executive verdict

**The cubical conjecture for m≥4 planks with ≥4 effective (non-facet) directions is NOT proved in this session.**

- No explicit counterexample with Σrw < 1 was found; an apparent sub‑1 covering at Σ≈0.976 **failed under grid refinement** (coarse optimizer claimed cover; n=150+ found uncovered points). This is exactly the anti-fabrication failure mode.
- A **genuinely new partial reduction** is proved for the subfamily “3 facet planks + 1 tilted plank of the form f₄(x)=t x₂+x₃”.
- The general m≥4 case is reduced to a **finite combinatorial set‑cover problem** (already known) plus a **single open inequality** that must use position, boundary, and escape‑ALL structure.
- Hunter’s m=3 identity **does not extend** to a single scalar certificate for m=4; the algebraic closure is specific to three edge parameters.

---

## 1. The clean arena (recalled, **[PROVED]** equivalence)

Let Δ={x∈ℝ³: xᵢ≥0, Σxᵢ=1}. After normalization (affine invariance), each plank is data (ũₐ, Iₐ) with ũₐ∈[0,1]³, minᵢ ũₐᵢ=0, maxᵢ ũₐᵢ=1, Iₐ⊆[0,1], |Iₐ|=rwₐ.

Define Φ:Δ→[0,1]ᵐ, Φ(x)ₐ=⟨ũₐ,x⟩. Image Q=conv(Φ(e₁),Φ(e₂),Φ(e₃)) is a 2‑D triangle in the m‑cube with each coordinate spanning [0,1].

**Cubical conjecture (triangle):** if Q⊆⋃ₐ{yₐ∈Iₐ}, then Σₐ|Iₐ|≥1.

**Lemma 1.1 [PROVED].** The cubical statement is equivalent to Bang’s affine plank conjecture for the triangle (standard affine‑invariance + relative width = interval length after normalization).

**Lemma 1.2 [PROVED].** For fixed directions {ũₐ}, the minimum Σ|Iₐ| over all interval placements that cover Δ is the value of a **geometric set‑cover** (choose one interval per coordinate so every x∈Δ hits some slab). The LP relaxation (fractional cover) can be **<1** while the integer optimum is **1** — the integrality gap is real, not an artifact.

*Proof sketches omitted (already in notes 10, 23, paper-ready/FINAL-REPORT).*

---

## 2. What was attempted and why it fails (self‑audit vs §5)

| Route | Outcome |
|---|---|
| Hunter / Helly m≥4→m=3 | **[REFUTED]** quantifier swap (notes 18, audit_helly.py) |
| Zonotope / support function | **[REFUTED]** position‑independent (notes 22) |
| Entropy / log potentials | **[REFUTED]** escape‑SOME (notes 19) |
| Nerve / KKM topology | **[REFUTED]** circular + misses boundary failures (notes 22) |
| Toric / Euler–Jacobi | **[REFUTED]** non‑Laurent denominators (notes 17) |
| Straightening flow | **[REFUTED]** not monotone (notes 13) |
| Infimal‑convolution dual (prop8) | **[REFUTED]** objective unbounded below without homogeneity constraints; “SUCCESS” was a numerical artifact |
| Semialgebraic 227M cells | **[REFUTED]** as proof — grid too coarse near Σrw=1 (notes 22) |
| Naive “Sf + span(f₄(Rf))≥1” | **[REFUTED]** as sufficient: Sf+span can be ≈0.98 for nonempty Rf, but **full cover still needs Σ≥1** once positions are checked |

---

## 3. Hunter m=3 — why it does not port to m=4

**Hunter (1993) [EQUALITY/EXTREMAL ONLY — see banner].** The relations below are Hunter's
characterization of the **equality** configurations (Σrw=1 boundary), NOT a proof of the
general 3-plank inequality (which is OPEN). For three planks on an equilateral triangle with edge parameters t₁,t₂,t₃ and relative widths summing to R:

\[
(2-T)(2-S)=1,\qquad R-1=(1-T)(S-1),\qquad T=t_1+t_2+t_3,\ S=s_1+s_2+s_3.
\]
Equivalently \(R-1=(1-T)^2/(2-T)\) using the constraint.

**Structural obstruction [PROVED as observation, not a theorem about all m=4].**

1. Hunter’s proof closes a **3×3** system: three independent edge parameters (tᵢ) determine three relative widths (sᵢ) via rational identities, then one scalar relation forces R≥1.
2. With **four** planks, there are **four** width variables and **twelve** edge‑crossing data (4×3), with only **three** independent edge lengths on the triangle. No single relation of Hunter type (one scalar = function of one aggregate T) can close without extra combinatorial hypotheses on how planks partition coverage along each edge.
3. Empirically, minimizing Σrw over m=4 **does not increase with m** (notes 23, BATTLE-PLAN) — extra planks are not “redundant slack”; they change the optimal interval placement. This kills any monotonic “add a plank → increase Σ” induction.

**Conclusion:** extending Hunter requires a **new** m=4 identity coupling edge crossings of all four planks, not a routine perturbation of (2−T)(2−S)=1.

---

## 4. PARTIAL RESULT — reduction for “3 facets + 1 tilted”

### 4.1 Setup

Fix t∈(0,1). Planks:

- Facets: fᵢ(x)=xᵢ, intervals Iᵢ=[aᵢ,aᵢ+rᵢ], i=1,2,3.
- Tilted: f₄(x)=t x₂+x₃, interval I₄=[c,c+r₄].

Note f₄(e₁)=0, f₄(e₃)=1, so after normalization w_Δ(u₄)=1 and **rw₄=r₄**.

Define the **facet‑escape set**
\[
R_f=\{x\in\Delta:\ x_i\notin I_i\ \forall i=1,2,3\}.
\]

### 4.2 Reduction lemma

**Lemma 4.1 [PROVED].** The four planks cover Δ **if and only if**:

1. Δ\R_f is covered by the three facet planks, and  
2. R_f⊆{x: f₄(x)∈I₄}.

*Proof.* A point in R_f is not covered by any facet plank by definition; it must be covered by plank 4. Points outside R_f are covered by some facet plank. ∎

**Lemma 4.2 [PROVED].** If R_f=∅, then the facet planks alone cover Δ, hence r₁+r₂+r₃≥1 by the facet‑parallel theorem (1‑D Brunn–Minkowski / sumset).

**Lemma 4.3 [PROVED].** If R_f≠∅, any covering must satisfy r₄≥span(f₄(R_f)):=max_{x∈R_f}f₄(x)−min_{x∈R_f}f₄(x).

*Proof.* f₄(R_f)⊆[c,c+r₄] ⟹ r₄≥|f₄(R_f)|; w_Δ=1. ∎

**Corollary 4.4 [PARTIAL / REDUCED].** For the 3+1 family, Bang’s inequality Σrw≥1 follows from the **single open lemma**:

> **Lemma L (open).** For all facet intervals with lengths rᵢ and escape set R_f≠∅, and fixed t∈(0,1),
> \[
> r_1+r_2+r_3+\bigl(\max_{x\in R_f} f_4(x)-\min_{x\in R_f} f_4(x)\bigr)\ \ge\ 1
> \]
> **whenever** Δ is coverable by these three facets together with a tilted plank of length r₄ on f₄.

Lemma L is **strictly stronger** than “Sf+span≥1”: numerically Sf+span can be ≈0.98 with nonempty R_f (e.g. Iᵢ=[0,0.3]), yet **no** placement of I₄ achieves full coverage at total Σ<1 once checked on a fine grid.

### 4.3 Numerics for the 3+1 family **[NUMERICAL ONLY — NOT PROOF]**

With coverage verified at grid resolution n=100–120:

- Differential‑evolution minima for Σrw cluster at **≈1.00–1.04** depending on t and seed.
- A coarse grid (n≈55) falsely reported Σ≈0.976 covering; refining to n=150+ found **6–29 uncovered points** in the alleged cover.

**Lesson:** for this problem, coarse grid “covering” is **unreliable** near the Σrw=1 boundary. Any computer-assisted proof must use interval arithmetic with explicit Lipschitz constants, not grid sampling.

---

## 5. General m≥4 — honest reduction to an open combinatorial core

For m≥4 with ≥4 distinct directions, fix ũ₁,…,ũₘ. Covering is equivalent to:

> **Problem P(ũ).** Choose intervals Iₐ of lengths rwₐ so that  
> ∀x∈Δ ∃a: ⟨ũₐ,x⟩∈Iₐ.

For each sign pattern σ∈{below,above}ᵐ, define
\[
R_\sigma=\{x\in\Delta:\ \langle\ũ_a,x\rangle\text{ is on the ``bad'' side of }I_a\text{ for each }a\}.
\]
Covering ⟺ R_σ=∅ for all 2ᵐ patterns σ.

**Lemma 5.1 [PROVED].** For fixed directions, the minimum Σrw is the optimum of a **discrete** set‑cover problem (one interval per direction; placement continuous but feasibility is combinatorial via sign cells). The fractional LP dual gives a per‑configuration witness measure with μ(Δ) equal to the fractional optimum (<1 possible).

**Open core [CONJECTURED equivalence to Bang].** Prove that for every admissible direction set of size ≥4 (not reducible to ≤2 directions), the integer optimum of P(ũ) is ≥1.

**Why this matches the four requirements (notes 23):**

| Requirement | Manifestation |
|---|---|
| Integer / combinatorial | Set‑cover optimum is integer in rwₐ; LP gap ≈0.30 |
| Position‑dependent | Intervals Iₐ=[aₐ,aₐ+rwₐ] — translation matters |
| Boundary‑based | Fractional dual concentrates ~54% mass on edges; Hunter m=3 uses edge crossings |
| Escape‑ALL | Must exhibit x∈⋂ₐ “outside Iₐ”, not minimize a sum of soft penalties |

No route in §5 of the prompt meets all four simultaneously.

---

## 6. Attempted counterexample — **[REFUTED]**

**Claim tested:** 3 facets with Iᵢ=[0,0.3] plus optimized tilted I₄ gives Σrw≈0.976 and covers Δ.

**Result [REFUTED]:** At grid n=150–300, uncovered points remain near (x₁,x₂)≈(0.30,0.31,…)—the central region R_f not fully captured by I₄. The conjecture is **not** refuted by this family.

---

## 7. What would constitute a proof from here

### Option A — Close Lemma L (3+1 family)
Prove Lemma L analytically, or prove directly that any cover of Δ forces Σ≥1. This would be the **first new proved subcase** beyond Hunter (m=3) and AKP (≤2 directions), but **does not settle** general m≥4 with four unrelated tilted directions.

### Option B — Edge‑crossing extension (Hunter type)
Parametrize m planks by their 3m edge intercepts on ∂Δ, impose affine relations from each plank’s line, and derive an inequality R−1≥Φ(edge data)≥0. **Obstruction:** 3m > 3+1 degrees of freedom; need extra combinatorial selection (which plank covers which edge segment).

### Option C — Rigorous computer proof for one fixed 4‑direction template
Semialgebraic stratification of a **single** rigid direction quadruple (e.g. one facet triple plus one generic tilt) with **interval arithmetic** certifying Σrw−1≥0 on all strata. Must handle Σrw→1 boundary (margin→0). Not attempted to completion here.

---

## 8. Precise obstruction (why the problem resists current tools)

1. **Fractional methods cap below 1** (Gardner / integrality gap) — any proof using a single positive measure is dead.
2. **Local‑to‑global failures** (Helly, entropy, nerve) — escape‑SOME ≠ escape‑ALL.
3. **Position‑independent certificates fail** (zonotope, Farkas 0‑1) — valid covers can have arbitrarily “narrow” zonotope in every direction.
4. **Hunter’s m=3 is a closed 3×3 rational system**; m=4 adds one width without adding a new triangle edge, so slack is distributed across **interior** coverage partitions, not edge lengths alone.
5. **Numerical confirmation is cheap; proof is not** — ILP already gives min Σrw=1.0000; the research gap is a **theorem**, not evidence.

---

## 9. Summary table

| Statement | Status |
|---|---|
| Full m≥4, ≥4 tilted directions, Σrw≥1 | **OPEN** |
| Explicit counterexample Σrw<1 | **Not found** (one false positive refuted by refinement) |
| 3 facets + 1 tilted f₄=t x₂+x₃ | **PROVED** (now subsumed: "3 facets + 1 arbitrary", notes/30 §1, fiber proof) |
| Hunter m=3 (general inequality) | **OPEN** (Hunter gave only 2-plank + equality char.; see banner) |
| Hunter m=3 equality `Σrw=1 ⟺ T=1` | **PROVED** (literature) |
| ≤2 directions | **PROVED** (AKP / Strassen) |
| Facet‑parallel only | **PROVED** (Brunn–Minkowski 1‑D) |
| Sf+span(f₄(Rf))≥1 as sufficient | **REFUTED** (numerical) |
| Coarse grid covering at Σ<1 | **REFUTED** as counterexample |

---

## 11. Update (2026-06-29) — first PROVED subcase

See **`notes/25-theorem-3plus1-symmetric.md`**.

**Theorem [PROVED].** Three facet planks \(I_i=[0,r]\), \(r\le1/3\), plus one tilted plank \(f_4(x)=tx_2+x_3\) covering \(\Delta\) implies \(3r+r_4\ge1\).

Proof: partition \(\Delta=R_f\cup(\Delta\setminus R_f)\); facets cover \(\Delta\setminus R_f\) exactly; affine span of \(f_4\) on \(R_f\) equals \(1-3r\).

The **general** 3+1 family (arbitrary facet shifts \(a_i\)) remains open; \(S_f+\mathrm{span}(f_4(R_f))\ge1\) is **false** in general, but full covering still requires \(\sum\ge1\) (numerically).

The **full m≥4** case with four unrelated directions remains **OPEN**.


Attack **Lemma L** for the 3+1 family via **edge stratification**:

1. Decompose ∂Δ into three edges; on each edge, the facet constraints reduce to 1‑D interval covering; the tilted plank induces an affine map g₄ on each edge.
2. For a covering, each edge must be covered by the union of plank traces; derive three inequalities (one per edge) coupling (r₁,r₂,r₃,r₄) and (a₁,a₂,a₃,c).
3. Combine with interior point constraints (R_f covered by I₄) — this is where Hunter’s m=3 identity linearizes, and where m=4 needs a **new** interior compatibility condition.

If Lemma L is proved, publish as a clean **partial theorem**; do **not** claim the general m≥4 case without a proof independent of the four‑direction template.
