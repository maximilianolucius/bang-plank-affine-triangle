# Deep Research + Work Plan — The Two Walls of the Affine Plank Conjecture
**Bang's affine plank conjecture for the triangle.** Date: 2026-06-28.
Scope: (W1) a *uniform/configuration-independent* dual certificate; (W2) the
irreducibility of m≥3 planks. Grounded in the literature (Verreault survey
arXiv:2203.05540; Gardner 1988; Akopyan–Karasev–Petrov 2019; Glazyrin–Karasev–
Polyanskii IMRN 2023; Chambers–Moullié 2016; Bakaev–Yehudayoff arXiv:2602.20290,
2026; Ambrus 2010/2022).

## Reframing from the literature (important corrections)
- **The first OPEN case is THREE PLANKS** (not "m>3"). Verreault: *"the case of a
  covering by three planks is still open"*; two planks proved (Hunter; Alexander;
  Gardner; …), two **directions** proved recently (Akopyan–Karasev–Petrov 2019,
  *J. Symplectic Geom.* 17(6):1579–1611).
- **Wall 1 IS Gardner's theorem.** Gardner (Pacific J. Math. 135 (1988) 299–312):
  if C admits a *relative width measure for all directions* — a Borel probability
  measure μ with μ(P)=rw(P) for every plank P ⟂ a used direction — then Bang holds
  for C. Via Ohmann's observation it suffices to have it for the d **coordinate**
  directions. Gardner proved: **such measures (coordinate directions) ALWAYS exist
  in R²** (⟹ the two-direction case), **but the all-direction version does NOT**
  (and even the coordinate version fails in R³). Our "single-measure impossibility"
  (uniform marginals in all directions contradict Σλ_i=1) is exactly Gardner's
  obstruction, independently re-derived.

═══════════════════════════════════════════════════════════════════════
## WALL 1 — A uniform (configuration-independent) dual certificate
═══════════════════════════════════════════════════════════════════════
**The wall, precisely:** the natural c=1 certificate is Gardner's relative-width
measure; it does NOT exist for all directions (R²) ⟹ no single measure proves the
full planar conjecture. Per-covering certificates exist but are LP-dual-equivalent
to the conjecture (circular). So a certificate must be a NEW object that is (i)
uniform across configurations and (ii) not a single probability measure.

### Live techniques in the literature (what to borrow)
1. **Polynomial method — Glazyrin–Karasev–Polyanskii (arXiv:2112.05382, IMRN 2023,
   [52]; Bull. LMS ext. [53]).** A covering by n planks ↔ a degree-n polynomial P
   (product of the plank-defining linear forms); the theorem: *for every nonzero
   degree-n polynomial there is a point of the unit BALL at distance ≥ 1/n from the
   zero set* ⟹ Bang's theorem for the ball. **HONEST SCOPE:** this is proven for
   the EUCLIDEAN BALL / sphere / complex projective space (the SYMMETRIC case,
   already covered by Ball 1991). It is NOT adapted to the AFFINE / relative-width /
   simplex setting — that adaptation is itself open. So the polynomial method is a
   *candidate*, not a ready tool, for the triangle.
2. **Chord-length normalization — Bakaev–Yehudayoff (2026).** Bang's strong form
   Σ opt/ℓ_K(u) ≥ 1, then ℓ/w ≥ 2/(1+√d) (tight at the cube AND, we verified, at
   the reduced regular (2d−1)-simplex). OBSTRUCTION to going past 2/(1+√d): the
   chord/width ratio is a genuine geometric invariant equal to 2/(1+√d) for the
   extremal body; improving needs a normalization between chord ℓ and width w that
   is still Bang-admissible — none is known.
3. **Symplectic capacities (AKP 2019, [3]).** Reformulate plank covering via a
   symplectic invariant; gave the two-direction theorem. The capacity is a
   configuration-independent quantity — a candidate "uniform certificate."
4. **Colorful Carathéodory / contact pairs (Ambrus 2010/2022, [7]).** Generalized
   Bang lemma via contact pairs; our facet sumset is the barycentric special case.

### WORK PLAN — Wall 1
- **W1-A [highest leverage, untried by us]:** Implement the Glazyrin–Karasev–
  Polyanskii polynomial method for the triangle. Build the degree-m polynomial
  whose zero set must contain the planks; show Σrw<1 ⟹ the polynomial is forced to
  have a zero pattern impossible on Δ ⟹ uncovered point. Verify numerically for
  m=3,4, then seek the closed-form certificate. *Tooling: sympy/numpy already on R15.*
- **W1-B:** Read AKP's symplectic capacity and test whether the capacity of the
  triangle's plank configuration is configuration-independent and ≥1 — the symplectic
  invariant is the most literature-supported "uniform" object.
- **W1-C:** A *relaxed* Gardner measure: since the exact all-direction measure
  fails, seek a measure with μ(P) ≤ rw(P)·(1+δ(u)) where δ averages to 0 over the
  used directions of an actual covering — exploiting that a covering's directions
  cannot all be the "bad" ones (the 2-direction theorem already forbids ≤2 bad ones).

═══════════════════════════════════════════════════════════════════════
## WALL 2 — Irreducibility of m≥3 (even three planks is open)
═══════════════════════════════════════════════════════════════════════
**The wall, precisely:** min Σrw ≈ 1 for ALL m (verified; does not increase), so
extra planks are not redundant; and the FIRST open case is m=3. Hunter [58]
characterized equality (3 planks of an equilateral triangle: Σ=1 ⟺ t1+t2+t3=1;
the extremal is the 3 edge-parallel planks — which we confirmed is a strict local
minimum). Two directions proved via symplectic invariants (AKP 2019).

### Live techniques / structure
1. **Hunter's equality geometry [58].** The extremal is rigid; a *stability* version
   (Σrw close to 1 ⟹ configuration close to facetal) would control the infimum.
2. **AKP symplectic invariant for 2 directions [3].** The only proof that handles a
   genuine 2-parameter family; the question is whether the invariant extends to 3
   directions (the symplectic manifold becomes higher-dimensional).
3. **Colorful Carathéodory / contact pairs [7].** A colorful selection theorem on
   the simplex would directly give the 3-plank/3-direction uncovered point.

### WORK PLAN — Wall 2
- **W2-A [sharpest target]:** Attack the THREE-PLANK case directly (the first open
  case, not "m>3"). Three planks ⟺ three affine functions on Δ with one linear
  relation; combine the AKP symplectic invariant (2 of the 3 directions) with a
  control on the third. Numerically map the 3-plank min-Σrw landscape (we have the
  tooling) to find the exact extremal family and its symmetry.
- **W2-B:** Prove Hunter STABILITY: Σrw = 1+ε ⟹ config is O(ε)-close to facetal.
  This + the strict-local-min fact (verified) + compactness of the *normalized*
  configuration space (mod affine) would pin the infimum at 1. The gap we hit was
  the non-compact/boundary strata — address them by adding the "plank-tangency"
  boundary explicitly as a stratified space.
- **W2-C:** Adapt the colorful Carathéodory contact-pair lemma (Ambrus [7]) to the
  triangle; our facet sumset proves the special case, so the target is the tilted
  contact pair.

═══════════════════════════════════════════════════════════════════════
## Honest meta-assessment
Both walls are now LITERATURE-IDENTIFIED, not just empirical:
- W1 = non-existence of Gardner's all-direction measure (Gardner 1988) — a theorem,
  not a failure of ours.
- W2 = the open three-plank case (Verreault) — the genuine research frontier.
The two NEW, untried-by-us techniques with the best chance are **(1) the Glazyrin–
Karasev–Polyanskii polynomial method** (W1-A) and **(2) the AKP symplectic
invariant extended from 2 to 3 directions** (W2-A). Both are recent (2019–2023)
and configuration-independent in nature — exactly what the walls demand.
NB: beating 2/(1+√d) for general bodies is a separate, harder frontier (BY 2026);
the triangle's three-plank case is the cleaner target.

═══════════════════════════════════════════════════════════════════════
## SYNTHESIS FROM THE DEEP-RESEARCH AGENT (verified, cross-checked)
═══════════════════════════════════════════════════════════════════════
### THE UNIFYING INSIGHT — both walls are ONE barrier: NON-SYMMETRY.
Every known `c=1`/exact success requires either central symmetry of `K` or a
cross-family symmetry hypothesis that fails for ≥3 generic plank directions on a
non-symmetric body, with the **simplex/triangle as the universal hard core**
(Ambrus reduction). Wall 1 and Wall 2 are the same obstruction seen two ways.

### Corrected / sharpened citations
- **Hunter 1993** (Proc. AMS 117(3):819–821): triangle `n=3` equality is
  `R−1 = (1−T)²/(2−T)`, so `R=1 ⟺ T=t₁+t₂+t₃=1`. **The equality locus is a
  one-parameter variety {T=1}, NOT rigid** — the 3-edge-parallel cover is one
  member, not the unique extremal. (Refines our "strict local min": locally strict
  in our perturbation test, but the global equality set is a curve.)
- **Chambers–Moullié 2016, Remark 4:** the explicit extremal 3-plank cover of the
  equilateral triangle is **NON-PEELABLE** (no plank's removal leaves a convex
  complement) ⟹ the published, rigorous form of Wall 2's irreducibility. Their
  Theorem 1 (peeling induction `Σrw≥1` if convexly orderable) is exactly the route
  that this extremal defeats.
- **Akopyan–Karasev–Petrov, J. Symplectic Geom. 17(6):1579–1611 (2019)** [NOT DCG;
  Petrov is a coauthor]. **CORRECTION:** the two-direction theorem (Thm 7.1) is
  proved by **ELEMENTARY combinatorics** (project to ℝ², inscribe in unit square,
  6-case induction), explicitly "independent of the symplectic considerations." The
  **symplectic strand covers a DIFFERENT slice** (symmetric / "almost-parallel"
  `nᵢ·nⱼ≥0`, via Minkowski-billiard length = 4). **It is CAPPED for the triangle:**
  Example 3.3 — the medial triangle is a closed Minkowski billiard of relative
  length 3/2 < 2, so the symplectic method gives only `≥3/4` for the triangle even
  granting the open capacity-subadditivity conjecture. ⟹ "extend symplectic 2→3"
  is a dead premise; the 2-direction win is combinatorial and has NO 3-direction
  analogue (no normalization fixes 3 relative-width scales).
- **Ambrus 2023, "A generalization of Bang's lemma," Proc. AMS 151(3):1277–1284,
  arXiv:2201.08823:** colorful-Carathéodory generalization (unifies Bang+Kadets).
  Its plank application needs the **cross-family condition ⟨uᵢ,vⱼ⟩=⟨uⱼ,vᵢ⟩ (Eq. 5)**,
  automatic for symmetric/Kadets configs but **FAILS for ≥3 generic directions on a
  non-symmetric body** — the same non-symmetry wall. Does NOT crack the triangle.
- **Polynomial/polarization method** (Ortega-Moreno 2021; Glazyrin–Karasev–
  Polyanskii IMRN 2023 / Bull. LMS 2024; Zhao 2022; Jiang–Polyanskii zone GAFA
  2017): produces a **primal point-witness, not a dual measure**, and works for
  **homogeneous forms on a centered sphere** (= centered planks). **Real unequal
  widths provably fails** (GKP counterexample). Affine slabs are off-center and
  `w_K(u)≠w_K(−u)` is not a (semi)norm ⟹ no Gram/quadratic structure to polarize.
- **Bakaev–Yehudayoff 2026:** the `2/(1+√d)` ceiling is intrinsic — Lemma 7 reduces
  to a perfect square, equality at `r=√d`; BOTH factors (strong Bang; chord/width)
  are individually tight (cube/simplex extremal). The residual gap to `c=1` is
  exactly "replace longest-chord ℓ by width w", which IS Gardner's non-existent
  all-directions measure. **Wall 1c ≡ Wall 1a.**

### Revised honest assessment of our work-plan
- **W1-A (polynomial method):** weaker than hoped — proven only for symmetric/ball;
  real unequal-width affine case provably resists. Keep as exploratory, not primary.
- **W2-A (symplectic 2→3):** RETRACTED — AKP's 2-direction is elementary; symplectic
  is capped at 3/4 for the triangle. The combinatorial 6-case induction has no 3-D
  analogue.
- **STILL the cleanest targets:** (i) a NEW certificate type that survives
  non-symmetry — the open frontier nobody has cracked; (ii) Hunter STABILITY on the
  one-parameter equality locus {T=1} (W2-B), now better-posed: the locus is a curve,
  so "stability" means transverse strict-positivity of Σrw−1 off {T=1}, which our
  perturbation data supports.
- **CORRECTION RETRACTED (2026-06-30):** an earlier "correction" here claimed the
  **three-plank triangle is NOT open** ("it is Hunter's theorem", "closed"). **That was
  WRONG and is hereby retracted** — it also contradicted the top of this very document
  (§"Reframing": *"The first OPEN case is THREE PLANKS"*). Verified against sources:
  Hunter 1993 ("Some special cases of Bang's inequality") proved only (i) the **2-plank**
  case in the plane and (ii) the **equality characterization** `Σrw=1 ⟺ T=t₁+t₂+t₃=1`;
  he did **NOT** prove the inequality `Σrw≥1` for three arbitrary planks. Verreault
  (§2.2.3, verbatim): *"the case of a covering by three planks is still open."* B–Y 2026:
  open even in the plane. So the **3-plank triangle case is OPEN** and is the genuine
  clean frontier (the original "3-direction triangle = open core" framing was CORRECT).
  The `R−1=(1−T)²/(2−T)` relation is Hunter's *equality* form, not a proof of the bound.

### Pointers we did NOT have before (for future attack)
- Artstein-Avidan–Ostrover billiard/capacity machinery (IMRN 2014, arXiv:1111.2353)
  — the symplectic engine; but capped at 3/4 here (Example 3.3).
- Balitskiy–Mitrofanov–Polyanskii, "Triangle covering problems and the Viterbo
  inequality in the plane," arXiv:2603.12495 (2026) — ties triangle covering to
  isobilliard/Viterbo; does NOT resolve the affine triangle. (NB Viterbo's
  volume-capacity conjecture was DISPROVED in 2024, Haim-Kislev–Ostrover.)
- Naszódi fractional illumination + Artstein-Avidan–Naszódi randomized coverings —
  the only genuine fractional-duality results in covering geometry (for homothets,
  not planks) — a possible template for a fractional plank certificate.

═══════════════════════════════════════════════════════════════════════
## EXTERNAL-MODEL PROPOSAL (assessed + one idea falsified, 2026-06-28)
═══════════════════════════════════════════════════════════════════════
An external model returned a strong response. Two central ideas:

**(A) The "cubical triangle theorem" [= our vector model; CORRECT TARGET].**
Reframe the 3-plank case: with `F(x)=(⟨ũ₁,x⟩,⟨ũ₂,x⟩,⟨ũ₃,x⟩)`, the image
`Q=F(T)=conv(q₁,q₂,q₃)⊂[0,1]³` is an affine triangle with FULL coordinate ranges,
and the planks are 3 coordinate slabs. Target:
   `Q ⊂ ⋃ᵢ{yᵢ∈Iᵢ} ⟹ Σ|Iᵢ| ≥ 1`,  i.e.  `Σ|Fᵢ|>2 ⟹ Q∩(F₁×F₂×F₃)≠∅`.
This IS our vector model (facet-parallel = the special plane y₁+y₂+y₃=1, proved by
1-D BM). Verified numerically (min Σrw ≈ 1). It removes the forbidden all-direction
Gardner measure — but PROVING it is exactly the open 3-plank core. The model's
suggested route (a "metric cubical intersection theorem for triangular membranes,"
KKM/Lebesgue-flavored) is the genuine open lemma.

**(B) The cyclic two-direction Gardner certificate [FALSIFIED].**
Use the three 2-direction Gardner measures μ₁₂,μ₂₃,μ₃₁ (each c=1 exact for its pair).
Covering ⟹ `2S + E' ≥ 3` where `E' = μ₁₂(P₃)+μ₂₃(P₁)+μ₃₁(P₂)`. If `E' ≤ S` then
`S ≥ 1`. **TESTED (min-leakage couplings via LP, 3-direction covers): E' can EXCEED
S** — found a genuine cover with `S=1.277, E'=1.500, E=E'−S=+0.223 > 0`. So the
certificate is INSUFFICIENT (the model flagged this exact failure mode). The
ensemble-of-pairwise-measures route does NOT prove the 3-plank case. (No
contradiction with the conjecture: that cover has S≥1 anyway.)

**Net:** the external model crystallized the right target (the cubical/vector
theorem) and the right secondary tools (semialgebraic sign-cell enumeration;
transverse Hunter stability on the curve {T=1}), but its one elegant *certificate*
(cyclic Gardner) is refuted. Proving the cubical triangle theorem remains the open
core — now stated in the cleanest possible non-measure form.
