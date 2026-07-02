# RESEARCH PROMPT — Break the two walls of the affine plank conjecture (triangle)

You are an expert in convex/discrete geometry. We have worked intensely on **Bang's
affine plank conjecture for the triangle** and reduced it to TWO precise walls. We
need you to (a) research these walls, (b) think broadly and creatively about how to
break them, and (c) propose a concrete work/research plan. Be rigorous; do not
fabricate proofs of open statements. Below is everything we have established
(proven, refuted, and the literature), so you can start from the frontier.

---
## 1. The problem (precise)
A **plank** is a slab `P = {x : a ≤ ⟨u,x⟩ ≤ b}` (unit normal `u`, width `w(P)=b−a`).
For a convex body `K`, `w_K(u) = max_K⟨u,·⟩ − min_K⟨u,·⟩`, and the **relative width**
is `rw(P) = w(P)/w_K(u_P)` (affine-invariant). A finite family **covers** `K` if
`K ⊆ ⋃P_a`.

**Bang's affine conjecture:** if planks cover `K`, then `Σ_a rw(P_a) ≥ 1`. It is
**open for all d ≥ 2**, including the plane. By Ambrus' reduction it suffices to
treat simplices; we focus on the **triangle** `T`. Sharp: 3 planks parallel to the
edges, `Σrw = 1` (Hunter's extremal).

**Vector model (useful):** by affine invariance `T` ≡ the standard 2-simplex
`Δ={x∈R³: x_i≥0, Σx_i=1}`. Each plank ↔ `(ũ_a∈[0,1]³ with min 0 & max 1, interval
I_a⊆[0,1] of length rw_a)`, and `P_a = {x∈Δ: ⟨ũ_a,x⟩∈I_a}`. Covering ⟺
`∀x∈Δ ∃a: ⟨ũ_a,x⟩∈I_a`. Facet-parallel planks are exactly `ũ_a = e_i`
(constraints on a single barycentric coordinate).

## 2. What is PROVEN (use freely)
- **Two directions:** if all planks lie in ≤2 directions, `Σrw ≥ 1` (sharp). Proof:
  a witness measure `ν` on `Δ` with both directional marginals uniform ⟹ `ν(P_a)=rw_a`
  exactly (constant `c=1`) [= Gardner's relative-width measure for 2 directions]. The
  same theorem is Akopyan–Karasev–Petrov, *J. Symplectic Geom.* 17(6) (2019), Thm 7.1
  — proved by **ELEMENTARY combinatorics** (project to ℝ², inscribe in a unit square,
  6-case induction), "independent of the symplectic considerations." It has **no
  3-direction analogue** (no normalization fixes three relative-width scales).
- **Three planks on a triangle:** **OPEN.** Hunter 1993 (Proc. AMS 117(3):819, "Some
  special cases of Bang's inequality") only classified the **equality** case
  (`Σrw=1 ⟺ T=t₁+t₂+t₃=1`); he did **NOT** prove the inequality `Σrw≥1` for 3 arbitrary
  planks. The 3-plank triangle case is **still open** (Verreault §2.2.3, verbatim; B–Y
  2026). Do NOT use it as a proven base case. (Proven NEW and Hunter-free: "3 facets + 1
  arbitrary plank", `notes/30` §1.)
- **Facet-parallel (any number, all dimensions):** `Σrw ≥ 1`, via 1-D Brunn–Minkowski:
  a free point ⟺ `1 ∈ F_1+…+F_{n+1}` (`F_i=[0,1]\I_i`); if `1∉ΣF_i` then
  `(1−F_1)∩(F_2+…) =∅` in `[0,n]` ⟹ `ΣLeb F_i ≤ n` ⟹ `Σrw ≥ 1`.
- **General lower bounds:** `Σrw ≥ 1/d` (Chambers–Moullié 2016, via John+Bang), improved
  to `2/(1+d)`; current SOTA `Σrw ≥ 2/(1+√d) ≈ 0.828` in the plane (Bakaev–Yehudayoff
  2026, arXiv:2602.20290) via Bang's strong form `Σ opt/ℓ_K(u) ≥ 1` (ℓ = longest chord
  ∥ u) and `ℓ/w ≥ 2/(1+√d)` (tight at the cube AND at the regular (2d−1)-simplex —
  we verified this equality numerically to 4 digits).

## 3. What is REFUTED (do NOT propose these; we verified each fails)
- Single fixed witness measure with `c=1`: impossible (uniform marginals in all
  directions contradict `Σλ_i=1`). Best single measure `c*≈1.60 ⟹ only 0.624`.
- "Peeling": removing a fine plank does NOT leave a similar triangle (the cut is not
  edge-parallel for a tilted plank; complement is a quadrilateral, cap-scale ≠ 1−ρ).
- "Splitting to shrink Σrw²": wrong direction (Σrw²→0 weakens 1≤2S−Σrw² to S≥½).
- Non-symmetric Bang sign-lemma: FALSE for arbitrary non-symmetric A (≈7%
  counterexamples by brute force); low-rank helps but the produced point escapes Δ.
- `Σrw² ≥ f(S)` second-moment bound: no valid f (fine planks defeat it).
- Reduce `m>3` to `m=3`: FALSE — min Σrw ≈ 1 for ALL m (does not increase with m).
- Lasserre/moment SDP (level ≤4, with strict margin): does NOT certify covering (the
  per-plank constraint `(⟨ũ,x⟩−lo)(⟨ũ,x⟩−hi)≥0` has TWO branches; the disjunction
  needs impractically high level; exact tool is the 2^m sign-cell LPs).
- Fried-potato "depth lemma" (tilted plank penetration ≤ r): FALSE — the layer-shadow
  GROWS under tilt (up to 3.7·r); it is a single measure ⟹ capped at 0.62.
- Chambers–Moullié convex-complement decomposition: 0% of generic coverings are
  orderable (a tilted middle plank splits the complement ⟹ non-convex).
- W_T conflict-set "Lipschitz bound" `|W_T| ≤ 4(1−Σr)₊`: FALSE (|W_T| large ∀ Σr).
- 0-1 Farkas dual "independent of positions": FALSE (per-covering ⟹ circular).

## 4. THE TWO WALLS (this is what we need you to break)

### WALL 1 — A uniform (configuration-independent) dual certificate.
The natural `c=1` certificate is **Gardner's relative-width measure** (Pacific J.
Math. 135 (1988) 299): a probability measure `μ` on `T` with `μ(P)=rw(P)` for every
plank `⊥` a used direction. **Gardner's theorem:** such a measure for ALL directions
⟹ the conjecture for `T`. **But it does NOT exist** for all directions in `R²` (only
for any fixed pair of directions; this is exactly our impossibility). Per-covering
certificates exist but are LP-dual-EQUIVALENT to the conjecture (circular).
**NEED:** a certificate that is (i) uniform across configurations, (ii) NOT a single
probability measure — e.g. a polynomial, a symplectic capacity, a colorful selection,
or a relaxed/signed measure.

### WALL 2 — The 3-plank triangle case is OPEN (and is the genuine frontier).
**[CORRECCIÓN 2026-06-30]** A previous version asserted "the THREE-plank triangle case is
NOT open — it is Hunter's theorem." **That is FALSE.** Hunter 1993 proved only (i) the
**2-plank** case in the plane and (ii) the **equality characterization**
`Σrw=1 ⟺ T=t₁+t₂+t₃=1` (`R−1=(1−T)²/(2−T)` is the *equality* form, not a proof of `R≥1`).
Verreault (survey §2.2.3): *"the case of a covering by three planks is still open."* B–Y
2026: open even in the plane. Proven & closed: 1 plank; 2 planks; ≤2 directions (AKP);
facet-parallel (our sumset); and "3 facets + 1 arbitrary" (`notes/30` §1, new).
So the open targets are:
- **(W2a) Triangle, m ≥ 3 planks in ≥3 tilted directions** — open **already at m=3**, the
  cleanest frontier. min Σrw ≈ 1 numerically for m=3..6, and m>3 does NOT reduce to m=3.
  NEED: prove the m=3 tilted case (e.g. via the fiber/`W₂` route of `notes/30` §2, or a
  transverse-stability theorem near the equality curve `{T=1}`), then push to m≥4.
- **(W2b) General planar convex body, 3 planks** — genuinely open (Verreault survey).
  AKP did 2 directions via symplectic/elementary; 3 directions on a non-symmetric
  body is the wall.

## 5. Literature / live techniques + their PRECISE obstruction
**THE UNIFYING DIAGNOSIS (key):** Walls 1 and 2 are the SAME barrier — **non-symmetry**.
Every known `c=1` success needs central symmetry of `K` or a cross-family symmetry
hypothesis that fails for ≥3 generic plank directions on a non-symmetric body.
- **Gardner 1988** (Pacific J. Math. 135:299): relative-width measure ⟹ conjecture;
  exists for ≤2 directions in ℝ², provably NOT for all directions (fails for the
  triangle's side-parallel set). This IS Wall 1.
- **Bakaev–Yehudayoff 2026** (arXiv:2602.20290): `2/(1+√d)` via strong Bang
  `Σ width/ℓ ≥ 1` + `ℓ/w ≥ 2/(1+√d)`; ceiling intrinsic (perfect square, both factors
  tight, cube/simplex extremal). The residual gap to `c=1` = "replace chord ℓ by
  width w" = Gardner's non-existent measure ⟹ Wall 1c ≡ Wall 1a.
- **Polynomial/polarization** (Ortega-Moreno 2021 PAMS; Glazyrin–Karasev–Polyanskii
  IMRN 2023 arXiv:2112.05382 + Bull. LMS 2024; Zhao 2022; Jiang–Polyanskii zone
  GAFA 2017): yields a primal **point-witness, not a dual measure**; works for
  homogeneous forms on a centered sphere (= centered planks); **real unequal widths
  provably fails** (GKP). Off-center affine slabs + `w_K(u)≠w_K(−u)` (not a norm) ⟹
  no Gram structure to polarize.
- **Ambrus 2023, "A generalization of Bang's lemma," PAMS 151(3):1277–1284,
  arXiv:2201.08823** (colorful-Carathéodory, unifies Bang+Kadets): plank application
  needs `⟨uᵢ,vⱼ⟩=⟨uⱼ,vᵢ⟩` (Eq. 5), which **FAILS for ≥3 generic directions on a
  non-symmetric body**. Same wall.
- **AKP symplectic strand** (Artstein-Avidan–Ostrover billiard/capacity, IMRN 2014):
  covers symmetric/almost-parallel only; **CAPPED at 3/4 for the triangle** (the
  medial triangle is a Minkowski billiard of relative length 3/2 < 2). Not a route.
- **Chambers–Moullié 2016** (peeling induction; extremal is non-peelable, Rem. 4);
  **Ball 1991** (symmetric case = the only `c=1` regime); **Ambrus 2010** (reduction
  to simplices, `d → (2d−1)`-simplex). Verreault survey arXiv:2203.05540.

## 6. THE ASK
For EACH wall:
1. Research the most relevant recent techniques (cite precisely).
2. Think broadly/creatively: propose 2–4 distinct attack strategies, stating for each
   what it would give and the precise obstruction to overcome. Prioritize approaches
   that are configuration-independent (Wall 1) or that prove the open m=3 tilted triangle
   case, or settle 3 planks on a general planar body (Wall 2).
3. Give a concrete, staged work plan (with falsifiable intermediate milestones and,
   where possible, numerical experiments we can run to validate before proving).
Be explicit about which proposals are speculative vs grounded. We have strong
numerical tooling (Python/numpy/scipy/cvxpy on a compute server). Do NOT re-propose
any refuted route in §3, and note that the **symplectic route is capped at 3/4** and
the **polynomial route requires symmetry** — so a winning idea must specifically
**defeat the non-symmetry barrier** that unifies both walls. **CLEAN OPEN TARGETS
(corrected): (W2a) the triangle with m≥3 planks / ≥3 tilted directions** — OPEN already
at m=3 (Hunter only did the equality case; the inequality is unproven); **(W2b)
3 planks on a general planar convex body**. The most valuable output is a certificate
TYPE (not a single probability measure) that survives the off-center /
`w_K(u)≠w_K(−u)` non-symmetry — e.g. a signed/vector measure, a non-homogeneous
polynomial device, a Gardner-measure relaxation exploiting that a real covering
cannot use only "bad" directions, or a genuinely new invariant. NOTE: the cubical
3-coordinate-slab statement on the simplex image is the (OPEN) m=3 case — proving it is
the goal, not a given; then push to m≥4 coordinate slabs.
