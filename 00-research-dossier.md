# Research Dossier — Candidate B
## Attacking Bang's affine (relative-width) plank conjecture with the Euler–Jacobi / BKK machinery

> Working folder: `/opt/VS/bang-plank-euler-jacobi/`
> Status: **research seed** (initial dossier). All work to stay inside this folder.
> Date started: 2026-06-27.
> **UPDATE 2026-06-27 (a):** deep-research completed → see `notes/01-deep-research-state-of-the-art.md`. Viability verdict revised in §7 below.
> **UPDATE 2026-06-27 (b):** Phase **M0 completed** (7 agents) → see `notes/04-m0-findings.md`. **Gate G0 = GO (conditional)**. Niche confirmed empty; Ambrus→simplex reduction confirmed; BY26 does not collide. NEW central obstruction identified: **CRUX 0, the shift problem** (affine planks are shifted; the M–OM engine is centered). Milestone ladder re-centered on CRUX 0 + the simplex.

---

## 0. One-paragraph thesis

The 2026 solution of the **real Hilbert linear-polarization conjecture** by Martínez & Ortega-Moreno introduced into the polarization/plank circle a genuinely new weapon: a **variational analysis of the critical-point system combined with the Euler–Jacobi vanishing theorem** (and, underneath, Bézout/BKK-type counting of solutions of a polynomial system). Pinasco–Galicer–Ortega-Moreno (June 2026) already showed this machinery is *extensible* (weighted version + entropy + a centred plank theorem in Hilbert space). The disruptive bet is to push the **same algebraic-variational engine** at the oldest unresolved target in this area: **Bang's conjecture on the sum of *relative* widths of planks covering a general convex body** — open since 1951 for non-symmetric bodies.

---

## 1. The protagonist's research map (Damián Pinasco, arXiv)

Disambiguation: **Damián Pinasco** (UTDT + CONICET, functional analysis / convex geometry) ≠ Juan Pablo Pinasco (PDEs, opinion dynamics). Filter accordingly.

### Program A — Polarization / plank / polynomial inequalities (his core identity)
| Year | arXiv | Title | Coauthors | Venue |
|---|---|---|---|---|
| 2026 | 2606.02567 | **Strong Polarization and Entropy** | Galicer, Ortega-Moreno | — (preprint) |
| 2023 | 2208.05584 | On the n-th linear polarization constant of ℝⁿ (n≤14) | solo | Math. Nachr. 296 (2023) 3593–3605 |
| 2017 | 1703.06316 | On the linear polarization constants of finite-dim spaces | Carando, Rodríguez | Math. Nachr. 290 (2017) |
| 2015 | 1507.02316 | Non-linear Plank Problems and polynomial inequalities | Carando, Rodríguez | Rev. Mat. Complut. 30 (2017) |
| 2012 | 1206.3130 | Lower bounds for norms of products of polynomials on Lₚ | Carando, Rodríguez | Studia Math. 214 (2013) |
| 2012 | — | Lower bounds … via **Bombieri inequality** | solo | Trans. AMS 364 (2012) |

### Program B — Asymptotic convex geometry / stochastic geometry
| Year | arXiv | Title | Coauthors |
|---|---|---|---|
| 2022 | 2211.06094 | On the volume ratio of projections of convex bodies | Galicer, **A. Litvak**, Merzbacher |
| 2019 | 1901.00771 | Asymptotic estimates for the largest volume ratio of a convex body | Galicer, Merzbacher |
| 2017 | 1707.03246 | The minimal volume of simplices containing a convex body | Galicer, Merzbacher |
| 2013 | 1312.0678 | Energy integrals and metric embedding theory | Carando, Galicer |

### Transversal threads
- **Probability:** 2020 · *Orthant probabilities and the attainment of maxima on a vertex of a simplex* (Smucler, Zalduendo) — equicorrelated Gaussians; tightly related to the "longest sum" tester.
- **Operator dynamics:** 2013/2015 hypercyclicity & strongly mixing convolution operators (Muro, Savransky).

**Collaborator network relevant to Candidate B:** Daniel Galicer (asymptotic geometric analysis, stochastic geometry), Oscar Ortega-Moreno (plank/polarization, the Euler–Jacobi method), Alexander E. Litvak (heavy hitter in AGA — a door into the general-bodies machinery), Mariano Merzbacher.

---

## 2. The methodological breakthrough we will weaponize (from 2606.02567)

**Setup (basis case).** Unit vectors `v₁,…,vₙ` a basis of ℝⁿ; weights `αⱼ = kⱼ/s`, `s=Σkⱼ`. Maximize
`P(x) = Π ⟨vⱼ,x⟩^{kⱼ}` on the sphere.

**Critical-point system.** Lagrange condition for `log|P|` gives `Σ kⱼ vⱼ/yⱼ = λx` with `yⱼ=⟨vⱼ,x⟩`; inner product with `x` ⟹ `λ=s`; against dual basis `wⱼ` ⟹ `yⱼzⱼ = kⱼ/s = αⱼ` where `z=Ay`, `A=G⁻¹`, `G` Gram. So the critical points solve the **quadratic system**
```
hⱼ(y) = yⱼ (Ay)ⱼ − αⱼ = 0 ,  j=1..n.
```

**Three pillars:**
1. **Reality (Lemma 3).** Every complex solution of `h(y)=0` is real (imaginary-part argument: `s‖b‖² = −Σ kⱼ Bⱼ²/(Aⱼ²+Bⱼ²) ≤ 0` forces `b=0`).
2. **One root per orthant (Lemma 4, from M–OM).** In each sign chamber of `(y₁,…,yₙ)` there is a unique real solution ⟹ exactly `2ⁿ` simple solutions, all real.
3. **Euler–Jacobi vanishing theorem.** For a system of `n` polynomials each of degree 2 with `2ⁿ = Π deg` simple solutions (Bézout-tight), any `g` with `deg g ≤ n−1` satisfies `Σ_{h=0} g(y)/det Jh(y) = 0`. Choosing `g` cleverly produces a solution with `Σ kⱼ²/yⱼ² ≤ s²`, i.e. the desired `u`.

**Why this matters for Candidate B.** The engine has three replaceable parts:
- the **objective** `Π⟨vⱼ,x⟩^{kⱼ}` (could become a width/plank functional),
- the **constraint manifold** (sphere ↔ boundary of a general convex body / its polar),
- the **counting** (Bézout `2ⁿ` ↔ **BKK / mixed-volume** count when the body is not a ball and the system is not "all degree 2").

The hard, novel mathematics of Candidate B lives precisely in replacing pillar (3)'s clean Bézout count with a **BKK (Bernstein–Khovanskii–Kushnirenko) mixed-volume count** adapted to the Newton polytopes that a general convex body produces, while preserving pillars (1)–(2) (reality + one-root-per-chamber).

---

## 3. The target problem (statement, history, what's open)

### 3.1 Tarski's plank problem and Bang's theorems
- A **plank** of width `w` = region between two parallel hyperplanes at distance `w`.
- **Tarski (1932):** if a convex body `K` is covered by planks, is `Σ widths ≥ width(K)` (minimal width of `K`)? 
- **Bang (1951):** YES (solved Tarski). Bang further **conjectured the stronger "affine/relative" form**:

> **Bang's affine plank conjecture.** If convex body `K` is covered by planks `P₁,…,Pₙ`, then
> `Σⱼ w(Pⱼ)/w(K; dirⱼ) ≥ 1`,
> i.e. the sum of the **relative widths** (each plank's width measured *relative to the width of `K` in that plank's direction*) is at least 1.

### 3.2 Status
- **Symmetric (centrally symmetric) `K`:** PROVED — **K. Ball, *The plank problem for symmetric bodies*, Invent. Math. 104 (1991) 535–543.**
- **General convex bodies:** **OPEN since 1951.** This is the prize.
- Complex / Hilbert analogues of the *plank* (not the affine conjecture) advanced by Ball (*Complex plank problem*, 2001) and now the centred Hilbert plank in 2606.02567 (Cor. 6).
- Partial / related: Bang's own absolute-width theorem; various special cases and asymptotic/relative results in the AGA literature (need a literature sweep — see `notes/lit-todo.md`).

### 3.3 Why polarization ↔ plank (the bridge Pinasco already uses)
In a Banach space `X`, `cₙ(X) ≤ nⁿ` follows from Ball's symmetric plank theorem; in Hilbert, products of functionals being large ⟺ a covering-by-planks statement. Pinasco's whole Program A repeatedly converts product-of-functional lower bounds into plank statements (e.g. 2606.02567 Cor. 6 derives a centred Hilbert plank from the weighted polarization inequality). **So the variational/Euler–Jacobi route to planks is already half-built inside his own corpus.**

---

## 4. The disruptive paper — framing & risk

**Title (working):** *A variational approach to Bang's affine plank conjecture.*
or *Critical points, Euler–Jacobi vanishing, and relative widths of planks.*

**Disruption logic.** Bang's affine conjecture is a 70+-year-old named open problem; Ball's symmetric case is in *Inventiones*. A method that breaks the symmetry barrier — or even substantially advances the general case — is a flagship result and re-positions Pinasco from "polarization specialist" to "person who cracked (a piece of) the plank problem".

**Risk profile.** HIGH for full resolution (decades-resistant). Mitigations / calibrated milestones:
- **M1 (warm-up, low risk):** re-derive Ball's symmetric plank theorem via the Euler–Jacobi engine — proof-of-concept that the variational method reaches *affine/relative* statements, not just Hilbert ones.
- **M2 (medium):** prove the affine conjecture for new structured classes (simplices, bodies with few faces, bodies of revolution, unconditional bodies) where the Newton polytopes / BKK count are controllable.
- **M3 (the prize):** general convex bodies, or a quantified `Σ rel. width ≥ 1 − ε(n)` bound improving the best known.
- **Fallback that still publishes:** a **method paper** — "Euler–Jacobi / BKK counting as a tool in plank & polarization problems" — that resolves several extremal constants exactly where only asymptotics existed.

**Where the genuinely new math is.** Replacing Bézout's clean `2ⁿ` simple real roots (special to the round sphere) by a **BKK mixed-volume count** for the critical system of a *general* body's support/width functional, while re-establishing:
- (P1) reality of all solutions (analogue of Lemma 3),
- (P2) one solution per "chamber" / sign or combinatorial type (analogue of Lemma 4),
- (P3) a vanishing identity (Euler–Jacobi holds for *any* zero-dimensional complete intersection with the right degree/Newton-polytope conditions) that forces existence of a good critical point.

---

## 5. Immediate next actions (to be done inside this folder)

1. **Literature sweep** → `notes/lit-todo.md`: Bang 1951; Ball 1991 (read the symmetric proof in detail — it is the thing to "Euler–Jacobi-ify"); Bang's relative-width formulation; surveys (Bezdek; Brass–Moser–Pach *Research Problems in Discrete Geometry*); recent relative-width / plank papers (Ortega-Moreno has plank papers — pull them all).
2. **Re-cast M–OM critical system** abstractly (objective / constraint / count) and write the dictionary "sphere → ∂K, Gram → support-function Hessian" → `notes/method-abstraction.md`.
3. **Attempt M1** (symmetric case via Euler–Jacobi) on paper → `drafts/M1-symmetric-warmup.md`.
4. **BKK feasibility memo:** compute Newton polytopes / mixed volumes for the simplex case (M2 entry point) → `notes/bkk-simplex.md`.

## 7. VIABILITY VERDICT (post deep-research, 2026-06-27)

### What the research confirmed (good news)
- **The target is genuinely OPEN** — verified `3-0` against 2026 primary sources (Bakaev–Yehudayoff, Verreault survey). Not a mirage, not secretly solved.
- **The methodological niche is empty:** no verified trace of Euler–Jacobi / BKK / Morse solution-counting applied to planks/relative-widths. The differentiator is real.
- **Ball's symmetric proof is "optimize a quadratic over `{±1}ⁿ` of a symmetric matrix"** — *the same algebraic family* as the M–OM critical system and Pinasco's sign-vector arguments. The bridge M1 (recover Ball via Euler–Jacobi) is natural, not a stretch.
- **Chambers–Mouille Theorem 1** (sharp bound 1 *if each successive remainder stays convex*) reads almost like a variational/critical-point reformulation already — a strong hint the engine is pointed the right way.

### What the research warned (sobering news — recalibrate ambition)
- **The problem is BRUTAL:** open *even in the plane*, **even for 3 planks**. Decades of strong people (Ball, Bezdek, Litvak, Kupavskii, Pach, Yehudayoff) have only nudged a constant. Full resolution is a **moonshot**, not a plan.
- **LIVE COMPETITION:** Bakaev–Yehudayoff *just* (Feb 2026) moved the bound to `2/(1+√d)`. Any "new general bound" result must **beat `2/(1+√d)`** or it is dead on arrival. Clock is ticking; others are actively on this.
- The "n≤14"-style incremental win (the move that made the polarization paper publishable) **has a direct analogue here**, and that analogue — not the full conjecture — is the realistic disruptive deliverable.

### Revised framing of "disruptive but feasible"
Full conjecture = moonshot (keep as M3 aspiration, do not promise). The **credible disruptive outcomes**, in increasing ambition:
1. **Recover Ball's symmetric theorem via the Euler–Jacobi engine** (M1). Low risk, proof-of-concept, *publishable as a "new proof"* + sets up everything else. **This is the floor: it de-risks the whole program and is worth a note on its own.**
2. **Prove the SHARP bound 1 for a new structured non-symmetric class** — simplices (via the **Ambrus reduction**, if it checks out), bodies of revolution, or `d=2` with `≥3` planks. *A first of its kind* → genuinely disruptive, medium risk.
3. **Beat `2/(1+√d)` for general bodies** with the algebraic-variational method. Concrete, competitive, high-value; must out-run Bakaev–Yehudayoff. Medium-high risk.
4. **Settle 3 planks in the plane** — small but embarrassingly-open; a focused variational/case analysis could land it and would be quotable.

**Verdict: GO, with recalibrated targets.** The disruptive thesis survives, but reframed as *"first algebraic-variational (Euler–Jacobi/BKK) attack on the affine plank problem, delivering (≥) a new structured-case theorem and/or an improved general bound"* — with full resolution as upside, not the deliverable. The empty methodological niche + the Ball-quadratic ↔ M-OM-critical-system bridge are the two pillars that make this worth doing now. **Hard gate: a fast literature negative-check (§7 of the report) before claiming method novelty, and an honest read of BY26's method so we don't reinvent or collide.**

## 8. Key references (full list to grow in `refs/`)
- [M-OM] A. D. Martínez, O. Ortega-Moreno, *A solution to the polarization problem*, preprint 2026. **← the method.**
- [GOP] Galicer, Ortega-Moreno, Pinasco, *Strong Polarization and Entropy*, arXiv:2606.02567 (2026). PDF saved in `refs/`.
- [P23] Pinasco, *On the n-th linear pol. constant of ℝⁿ*, Math. Nachr. 296 (2023). PDF saved in `refs/`.
- [Ball91] K. Ball, *The plank problem for symmetric bodies*, Invent. Math. 104 (1991) 535–543. **← the barrier to break.**
- [Ball01] K. Ball, *The complex plank problem*, Bull. LMS 33 (2001) 433–442.
- [Bang51] T. Bang, *A solution of the "plank problem"*, Proc. AMS 2 (1951) 990–993.
- [Tarski32] A. Tarski, *Remarks on the degree of equivalence of polygons*, Parametr 2 (1932) 310–314.
- Euler–Jacobi vanishing theorem; BKK theorem (Bernstein 1975) — standard refs to be added.

### References surfaced by M0 (2026-06-27)
**Affine-plank / planks:**
- [Amb10] G. Ambrus, *Appendix: Plank problems* (2010), `users.renyi.hu/~ambrus/appendix.pdf` — **simplex reduction** (Conj. 10). *Unpublished; verify in full + reconcile 1/2 vs 1 normalization.*
- [AK19] Akopyan–Karasev, *Bang's problem and symplectic invariants*, J. Symplectic Geom. (2019), arXiv:1404.0871 — only prior heavy-machinery (symplectic) attack; cite & distinguish.
- [GKP23] Glazyrin–Karasev–Polyanskii, *Covering by planks and avoiding zeros of polynomials*, IMRN (2023) — polynomial method (centered planks).
- [OM21a] O. Ortega-Moreno, *An optimal plank theorem* (2021), arXiv:1906.04126.
- [OM21b] O. Ortega-Moreno, *The complex plank problem, revisited* (2021/22), arXiv:2111.03961. — **read for M1′ prep; he is the near-mandatory coauthor.**
- [White–Wisewell] polygon characterization; "spiky bodies" extension (survey ref [10]).
- [3] (survey) two-parallel-directions case (~2021).

**Toric / Euler–Jacobi toolbox (CRUX 3):**
- [DAD26] D'Andrea–Dickenstein, *Toric Euler–Jacobi vanishing theorem and zeros at infinity*, arXiv:2601.13977 (2026) — **cleanest entry**; Thm 1.1 (supp(g)⊂int(P₁+…+Pₙ)), Def 1.3 indecomposability.
- [Kho78] Khovanskii, *Newton polyhedra and the Euler–Jacobi formula*, Russian Math. Surveys 33:6 (1978).
- [CD97] Cattani–Dickenstein, *A global view of residues in the torus*, JPAA 117/118 (1997) — no-genericity proof.
- [VY01] Vidras–Yger, *On some generalizations of Jacobi's residue formula*, Ann. Sci. ENS 34 (2001), arXiv:math/9905044 — explicit degree bound.
- [Mon21] P. Mondal, *How Many Zeroes?*, CRM Short Courses, Springer (2021), arXiv:1806.05346 — BKK sharpness (Thm VII.7, ND*).
- [CLO] Cox–Little–O'Shea, *Using Algebraic Geometry*, Thm 7.5.4 — BKK only.
- [EGH96] Eisenbud–Green–Harris, *Cayley–Bacharach theorems and conjectures*, Bull. AMS 33 (1996) — EJ ⊂ Cayley–Bacharach; extremal-use precedent.
- [GH] Griffiths–Harris, *Principles of Algebraic Geometry*, Ch. 5 / p. 671 — classical EJ (as used by M–OM).
