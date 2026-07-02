# M0 — De-risk findings & Gate G0 decision
### Synthesis of 7 parallel research agents. Date: 2026-06-27.

This is the deliverable of Phase M0 (`03-work-plan.md`). It resolves T0.1–T0.4 and
issues the **Gate G0** decision. Sources are the agents' primary-source reads
(Ball91, CM16, BY26, M–OM 2605.28744, Verreault survey, Ambrus appendix, the
toric-residue literature).

---

## EXECUTIVE SUMMARY / Gate G0 verdict: **GO** (conditional, recalibrated)

All four de-risk questions resolved favorably, but a **new central obstruction
surfaced** that reshapes the plan:

| G0 gate question | Verdict |
|---|---|
| Is the method niche (Euler–Jacobi/BKK critical-point counting on planks) empty? | **YES — confirmed empty** by the authoritative method catalog (Verreault survey) + negative search |
| Is the Ambrus → simplex reduction real (validates M2)? | **YES — verified against primary source** (`notes/40`, appendix read verbatim 2026-06-30). ½-vs-1 = half-width convention (resolved); reduction *proved* modulo a WLOG pairwise-orthogonal step; **target = simplices of dim `2d−1`, NOT the `d`-simplex** |
| Does our approach collide with the live competition (BY26)? | **NO — methodologically orthogonal**; BY26 is elementary convex geometry, sharp-for-cube, decouples planks |
| Is a usable toric/BKK Euler–Jacobi theorem available (CRUX 3)? | **YES — precise statement in hand** (D'Andrea–Dickenstein 2026 et al.) |
| **NEW: the shift problem (CRUX 0)** | **OPEN RISK** — affine planks are *shifted*; the engine is *centered*. This is now the make-or-break design question. |

**Decision:** Proceed to M1, but with the milestone ladder **re-centered on the
shift problem** and on Ambrus's simplex reduction. See §6 for the revised gates.

---

## T0.1 — Negative novelty search: niche is EMPTY

- **No paper** applies Euler–Jacobi vanishing or BKK/mixed-volume counting of the
critical points of a width/plank functional to the plank or relative-width problem.
- **Strongest evidence** (evidence of absence, not merely absence of evidence): the
**Verreault survey (Bull. LMS 2026)**, the field's definitive method catalog, has
**zero** occurrences of "Euler", "Jacobi", "Morse", "BKK", "Newton polytope",
"resultant", "critical point". It explicitly lists the methods in use: Bang's
sign-selection lemma, geometric reductions, Gram/PSD linear algebra, the
"polynomial method" (zeros of a *single* polynomial on the sphere), duality.
- **Neighbors to cite and distinguish** (pre-empt the referee):
  1. **Polynomial method** (Ball; Ortega-Moreno arXiv:2111.03961, 1906.04126; Zhao;
     **Glazyrin–Karasev–Polyanskii, IMRN 2023**): proves existence of *one* zero/sign
     of *one* polynomial on the sphere via max-modulus/IVT. **Never counts** a
     critical system. *Different technique.*
  2. **Akopyan–Karasev, "Bang's problem and symplectic invariants", J. Symplectic
     Geom. 2019 (arXiv:1404.0871):** the only prior heavy-machinery attack —
     **symplectic capacities**, not algebraic. Cite to show we surveyed the high-tech
     attempts.
  3. Euler–Jacobi/BKK enter convex geometry only via **mixed-volume / Alexandrov–
     Fenchel / Bézout inequalities** (Khovanskii–Teissier; arXiv:1704.00883), **never
     plank covering**.
- **Caveat:** the two flagship 2026 papers are too recent for citation trails;
  treat follow-up-absence as weak corroboration.

**Verdict: the methodological novelty claim is defensible.**

---

## T0.2 — The four key reads

### Ball 1991 — where central symmetry breaks (the step to "Euler–Jacobi-ify")
- **Theorem 1** (planks cover unit ball ⟹ Σ half-widths ≥ 1); **Theorem 2** (dual
  point form: unit functionals φᵢ, reals mᵢ, wᵢ>0, Σwᵢ=1 ⟹ ∃ x in unit ball with
  |φᵢ(x)−mᵢ| ≥ wᵢ); **Corollary** (1/(n+1) translate avoiding n hyperplanes, sharp).
- **Technique:** reduce to a matrix theorem; **Bang's Lemma** = argmax over the
  sign cube {±1}ⁿ of a quadratic form, single-coordinate-flip perturbation. The
  matrix A=(φᵢ(xⱼ)) has 1's on the diagonal; candidate point x=Σλⱼxⱼ.
- **Symmetry is load-bearing at TWO coupled points:**
  (a) *body symmetry* ⟹ C is a norm ball, so ±xⱼ∈C and ‖Σλⱼxⱼ‖≤Σ|λⱼ| — the {±1}ⁿ
  sign structure only makes sense for symmetric C;
  (b) *matrix symmetry* is essential to Bang's Lemma (Ball's explicit counterexample
  [[1,1],[−1,1]]). Since A is not symmetric, §2 is a **nuclear-norm symmetrization**
  (Lemma 4: minimize ‖(θᵢaᵢⱼ)‖_{C₁} s.t. Πθᵢ=1; rotate by orthogonal U).
- **Character:** NOT algebraic geometry, NO polynomial system, NO Lagrange/critical
  points. Hybrid: discrete-variational (Bang) + continuous optimization (nuclear-norm
  symmetrization) + operator Cauchy–Schwarz.
  **[2026-06-30] La fuente `scratchpad/ball_fitz.txt` era efímera y se perdió; este análisis
  se consolidó, con respaldo de fuente primaria (Ambrus §Ball) y del draft M1, en
  `notes/41-ball-1991-analisis-recuperado.md`. El método exacto de simetrización (Ball 1991
  Lemma 4) queda [PENDIENTE] de re-lectura contra el original Invent. Math. 104.**
- **Implication:** the shift mᵢ lives inside Bang's Lemma (the μᵢ); so *the symmetric
  affine theorem already handles shifts* — encouraging for CRUX 0.

### Chambers–Mouille 2016 — the conditional sharp bound
- **Theorem 1** (sharp ≥ 1) **conditional** on: C∖⋃_{i≤m}Pᵢ convex for every m.
- **Theorem 2** (unconditional): Σ ≥ 1/dim π_V(C); plus **2/(1+d)** via centroid
  symmetrization C̃=(C−g)∩(g−C) + Ball + **Minkowski–Radon** w(C̃) ≥ 2/(1+d)·w(C)
  (equality essentially at the simplex).
- **Method of Thm 1:** induction by **peeling** (Prop. 3: homothety ρC⊂X̄,
  width-monotonicity). Pure elementary convex geometry — **no** variational/algebraic
  content.
- **For our recasting:** the convex-remainder hypothesis is an *orderability /
  non-notching* condition, NOT a stated non-degeneracy condition; recasting it as a
  reality/critical-point condition is **our** contribution. **Remark 4 (Hunter):**
  3 planks cover an equilateral triangle, Σ=1 sharp, yet **no ordering** keeps the
  remainder convex — Thm 1 cannot extend by peeling. This extremal config is exactly
  the planar 3-plank case (Problem M3b) and the natural stress-test for any new method.

### Bakaev–Yehudayoff 2026 — the live competition, no collision
- **Theorem 8:** Σ rw_K(Pᵢ) ≥ **2/(1+√d)** (current record; ≈0.82 in the plane).
- **Method:** central symmetrization L=½(K−K) → John position (B⊆L⊆√d·B) →
  strengthened **chord-length** Bang (Σ width/ℓ_K ≥ 1) → key **Lemma 7**
  ℓ_K(u)/w_K(u) ≥ 2/(1+√d) via a 2D similar-triangles + **perfect-square SOS**.
- **ZERO** algebraic/critical-point/Morse/BKK. **Decouples planks completely.**
- **Structural ceiling:** Lemma 7 is **sharp for the CUBE** (r=√d). So this
  per-direction, decoupled route **cannot pass 2/(1+√d)**; surpassing it requires
  *coupling* the plank configuration — exactly what a variational/critical-point
  method does. **The slack lives in the simplex**, not the cube.
- **No collision; orthogonal line of attack. To claim a new general bound we must
  beat 2/(1+√d).**

### Martínez–Ortega-Moreno (arXiv:2605.28744) — the engine, precisely
- Confirmed = the polarization solution (v2 retitled *"Polarization problems and
  Coxeter systems"*; authors Á. D. Martínez & O. Ortega-Moreno, CUNEF Madrid).
- **Theorem A:** Σ_{u∈E(P)} (Σⱼ 1/⟨vⱼ,u⟩² − n²)·µ(u) = 0, with
  µ(u)=det(I+(1/n)Σⱼ (vⱼ⊗vⱼ)/⟨vⱼ,u⟩²)⁻¹ > 0 ⟹ ∃ critical point with Σ 1/⟨vⱼ,u⟩²≤n².
- Critical map h(x)=Σ(⟨vⱼ,x⟩⟨wⱼ,x⟩−1/n)vⱼ, **degree 2**; E(P)={h=0}.
- **P1 reality** (Lem 2.1): imaginary-part energy n‖b‖²=−Σⱼ⟨vⱼ,b⟩²/(…)≤0 ⟹ b=0.
- **P2 count** (Lem 2.2): **strictly convex potential** Ψ(x)=½‖x‖²−(1/n)Σⱼlog|⟨vⱼ,x⟩|,
  one minimizer per sign chamber, 2ⁿ chambers = Bézout 2ⁿ. *This device delivers
  reality+simplicity+count in one stroke — and may be the cleanest thing to port to
  general bodies, possibly avoiding BKK altogether.*
- **P3 vanishing:** test polynomial **g = ΔP** (Laplacian, deg n−2), det J_h(u)=
  P(u)/µ(u), ΔP(u)=P(u)(n²−Σ1/⟨vⱼ,u⟩²). Uses **classical** Euler–Jacobi
  (Griffiths–Harris p.671), **not** BKK. Degree bound deg g ≤ ∑dᵢ−(n+1)=n−1.
- **Rigidity tool (G6):** harmonicity ΔP≡0 characterizes **Coxeter** extremizers;
  open problem = do Coxeter systems exhaust the strong-polarization extremizers.
- Scope is round/Hilbert only; planks are background. They note Bang's longest-sum
  *cannot* settle it (Matolcsi–Muñoz n=34), hence evaluating at a different sphere pt.

---

## T0.3 — Ambrus reduction to simplices: VERIFIED against primary source (validates M2)

> **[ACTUALIZADO 2026-06-30]** El apéndice se leyó **verbatim** (`pdftotext`); el análisis
> completo está en **`notes/40-ambrus-reduccion-verificada.md`**. Resumen de la resolución:
> - **½ vs 1 RESUELTO:** es half-width vs full-width. Conjecture 10 dice `Σ rw ≥ 1` (verbatim);
>   la reducción escribe planks de **semi-ancho** `wᵢ` con objetivo `Σ wᵢ ≥ ½`, y `rw_T(L̃ᵢ)=2wᵢ`
>   ⟹ los dos enunciados son **idénticos**. No es un enunciado más débil.
> - **La reducción está PROBADA** en el apéndice (no conjeturada), módulo el paso WLOG
>   "direcciones pairwise-ortogonales" (afín + aproximación, asertado).
> - **Corrección de foco:** el símplex objetivo tiene dimensión **`2d−1`** (para `d=2`, un
>   tetraedro en `R⁴`), **NO** el `d`-símplex. "Triángulo ⟹ planos generales" **no** es la
>   reducción de Ambrus.
>
> El texto original de abajo queda como registro; sus "caveats" (1) y (2) están ahora resueltos.

- **Primary source:** G. Ambrus, *"Appendix: Plank problems"* (2010),
  `https://users.renyi.hu/~ambrus/appendix.pdf`. His **Conjecture 10 = Bang's affine
  (relative-width) conjecture**. The reduction: choose x_{2i}, x_{2i+1}∈K realizing
  unit width in direction uᵢ; seek the covering point as a convex combination
  x=Σcᵢxᵢ (∈K by convexity); this recasts covering of K as covering of a **simplex T**
  (dim 2d−1 in R^{2d}) with relative widths preserved ⟹ **simplices ⟹ general bodies**.
- **Independent corroboration:** cited as **[Amb10]** by Bakaev–Yehudayoff.
- ⚠️ **Two caveats before relying on it:**
  1. **Unpublished** (an appendix/manuscript on his Rényi page, not a journal). We
     must read it in full and re-verify rigor before building M2 on it.
  2. The quoted target is "Σwᵢ ≥ **1/2**" — likely a **half-width** convention;
     reconcile the normalization with the Σ≥1 statement.
  - It is **not** in the Verreault survey (which never mentions simplices).
- **Strategic upshot:** M2 (simplex) is doubly justified — Ambrus says it implies
  everything, and BY26 shows the slack lives precisely at the simplex (their bound is
  sharp for the cube, loose for the simplex).

---

## T0.4 — Toric/BKK Euler–Jacobi (CRUX 3): precise statement in hand

- **Classical Euler–Jacobi:** for f₁,…,fₙ (deg dᵢ) a regular system with exactly
  Bézout-many d₁⋯dₙ **simple** zeros and **no zeros at infinity**, then for every g
  with **deg g ≤ (∑dᵢ) − n − 1** (strictly below the socle degree ∑dᵢ−n = deg J_f),
  Σ_{ζ} g(ζ)/J_f(ζ) = 0. *(Our planned bound is exactly right, off-by-one included.)*
  At deg g = socle, the sum is the nondegenerate Gorenstein trace (e.g. g=J_f gives
  the root count). Refs: Griffiths–Harris Ch.5; Vidras–Yger (ENS 2001) eq.(1.2);
  Cattani–Dickenstein (2005).
- **Toric / sparse generalization:** for Laurent systems with Newton polytopes Pᵢ,
  P=P₁+⋯+Pₙ full-dimensional, the condition **replacing the degree bound** is
  **supp(g) ⊂ interior(P)** (interior lattice points of the Minkowski sum). Then the
  toric global residue Σ_ξ g(ξ)/J_f^T(ξ) = 0, using the **logarithmic Jacobian**
  J_f^T=det(tᵢ∂fⱼ/∂tᵢ). Hypotheses for *vanishing*: finite torus zeros + **BKK
  attained (no zeros at toric infinity)** + P full-dimensional. **No simplicity or
  genericity needed for vanishing itself.** Converse needs **indecomposable**
  polytopes (full-dimensional Pᵢ ⟹ indecomposable). Reduces to classical when Pᵢ=dᵢΔ.
- **BKK sharp + simple roots:** Bernstein **facial non-degeneracy** (ND*: for every
  ν≠0 the initial forms In_ν(fⱼ) share no torus root) ⟺ BKK attained with multiplicity;
  **plus** a regular-value/generic-coefficient condition ⟹ all MV roots distinct & simple.
- **Key refs:** **D'Andrea–Dickenstein, arXiv:2601.13977 (2026)** (cleanest entry,
  Thm 1.1, Def 1.3 indecomposability); Khovanskii (1978); Cattani–Dickenstein (JPAA
  1997, no-genericity proof); Mondal, *How Many Zeroes?* (arXiv:1806.05346, Thm VII.7,
  ND*); Cox–Little–O'Shea Thm 7.5.4 (BKK only).
- **Framing precedent:** Euler–Jacobi is the residue case of **Cayley–Bacharach**
  (Eisenbud–Green–Harris, Bull. AMS 1996), which *is* used in extremal combinatorics
  — useful precedent that "EJ identities constrain configurations." But the specific
  bridge **toric-EJ → convex-geometry extremal inequality does NOT exist yet** → novel.

---

## NEW CENTRAL OBSTRUCTION — CRUX 0: the shift problem

The single most important strategic finding, from the Verreault survey:

> The survey draws a hard line between **centered planks** (no shift) — "really
> polarization problems," where the polynomial/complex-plank machinery works — and
> **shifted planks** — the genuine affine conjecture. It explicitly judges the
> polynomial methods **"unlikely to yield a streamlined demonstration of Ball's plank
> theorem"** and not to reach the affine (shifted) case.

- The M–OM engine is **centered**: P(x)=∏⟨vⱼ,x⟩, no offsets. The affine plank has
  **shifts** mᵢ (the plank is aᵢ ≤ ⟨·,uᵢ⟩ ≤ bᵢ, generally not centered at 0).
- **This is the make-or-break design question (Problem 4.1 in the manuscript).** Any
  critical-point/EJ attack on the *affine* conjecture must build the shifts into the
  objective and its critical system.
- **Reason for optimism:** Ball's symmetric proof *does* carry the shifts (the μᵢ in
  Bang's Lemma). So shifts are not intrinsically incompatible with the
  quadratic/critical structure — the task is to find the *shifted* objective whose
  critical system stays a controllable (ideally degree-2 / nice-Newton-polytope)
  complete intersection with a reality argument and a convex-potential count.

---

## Strategic refinements to the plan (consequences of M0)

1. **CRUX 2 may not need BKK.** M–OM get the count from a **strictly convex
   potential**, not BKK. First try: build a convex potential Ψ_C from the body's
   gauge/support function. Keep toric-EJ (T0.4) as the fallback when the body's
   critical system is not of nice degree.
2. **Re-order the ladder around CRUX 0 and the simplex.** The simplex is (a) implied-
   to-be-sufficient by Ambrus and (b) where BY26's slack lives. Make the shift the
   first thing tested, on the simplex.
3. **Ortega-Moreno is the near-mandatory coauthor.** He co-invented the engine *and*
   has his own polynomial-method plank line (2111.03961, 1906.04126) — he already
   knows the centered/shifted divide intimately.
4. **The 3-plank planar extremal config is concrete** (Hunter's equilateral triangle,
   Σ=1; CM16 Remark 4 = survey's t₁+t₂+t₃=1). Use it as the running falsifier.
5. **Beating BY26 (2/(1+√d)) requires coupling planks** — our method's structural
   advantage. That is the honest headline target for M3a.

---

## Revised milestone gates (supersede §C of `02-gaps-and-milestones.md`)

- **M1′ (warm-up, decisive):** reconstruct Ball's **symmetric** theorem — *including
  shifts* — via a critical-point/convex-potential + Euler–Jacobi argument. Tests CRUX 0
  and CRUX 1 on the easiest case. **If the engine can't absorb the shift even for
  symmetric bodies, the algebraic route is likely dead → fall back to a "new proof of
  Ball" note or a non-algebraic variational attack.**
- **M2′ (the reachable prize):** simplex case, via Ambrus's reduction (after verifying
  the appendix). Resolve CRUX 1/2 concretely; build Ψ_simplex.
- **M3′ (stretch):** beat 2/(1+√d) by coupling planks, and/or close planar 3-plank
  (Hunter config), and/or remove CM16's convexity hypothesis by recasting it as
  non-degeneracy of the critical system.

**Immediate next actions (M1′ prep):** (i) read Ambrus's appendix in full + fix the
1/2 vs 1 normalization; (ii) read Ortega-Moreno 2111.03961 & 1906.04126 to learn how
he already handles polynomials-on-the-sphere for planks; (iii) attempt the *shifted*
objective for a symmetric body and check whether Bang's μᵢ-quadratic is its critical
system.
