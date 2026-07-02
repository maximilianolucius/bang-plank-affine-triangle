# The M–OM engine, abstracted — and the dictionary toward planks

## A. The engine as three swappable parts (from 2606.02567, §2)

| Part | Hilbert/polarization instance | What it must provide |
|---|---|---|
| **Objective** | `P(x)=Π⟨vⱼ,x⟩^{kⱼ}`, maximize `log|P|` on `S^{n-1}` | a function whose critical points encode the inequality we want |
| **Critical system** | `hⱼ(y)=yⱼ(Ay)ⱼ−αⱼ=0`, `y=(⟨vⱼ,x⟩)`, `A=G⁻¹` | a 0-dim polynomial system, degree-2, `n` eqns |
| **Count** | Bézout: `Π deg = 2ⁿ` solutions, all **simple** | exact root count = product of degrees |
| **Reality** (Lemma 3) | imaginary-part energy argument ⟹ `b=0` | every complex root is real |
| **Chamber uniqueness** (Lemma 4) | one root per sign-orthant of `y` | roots ↔ combinatorial cells, in bijection |
| **Vanishing** | Euler–Jacobi: `Σ g(y)/detJh = 0` for `deg g ≤ n−1` | forces a root with the desired sign of `s²−Σkⱼ²/yⱼ²` |

The punchline trick: pick `g` so that `g(y)=Q(y)(s²−Σkⱼ²/yⱼ²)` with `Q=Πyⱼ`, and note `det Jh = Q·det(A+diag(αⱼ/yⱼ²))` with the second factor **positive** at every root. Euler–Jacobi ⟹ `Σ_roots (s²−Σkⱼ²/yⱼ²)·μ(y)=0` with `μ>0` ⟹ some root has `Σkⱼ²/yⱼ² ≤ s²`. That root's normalized `x=u` is the witness.

## B. The dictionary we want (sphere → general convex body)

Goal: a critical-point system whose "good root" yields `Σⱼ w(Pⱼ)/w(K;dirⱼ) ≥ 1`.

| Hilbert object | General-body candidate |
|---|---|
| sphere `S^{n-1}` (constraint) | boundary `∂K`, or sphere under the gauge/Minkowski functional `‖·‖_K` |
| inner product `⟨vⱼ,·⟩` | support function `h_K(·)` / width functionals `w(K;dirⱼ)` of the planks' normals |
| Gram `G`, `A=G⁻¹` | Hessian of the support function (curvature) / the body's local quadratic data |
| Bézout `2ⁿ` | **BKK mixed volume** of the Newton polytopes of the `hⱼ` — generally `< 2ⁿ` or structured |
| sign-orthant chambers | normal-fan cells of `K` / combinatorial face types |

### Crux #1 — Reality (analogue of Lemma 3)
The energy/imaginary-part argument used `A = G⁻¹` **positive definite** and `vⱼ` real. For a general body the "metric" is the support-function Hessian, PD on smooth strictly-convex pieces. Reality should survive on **smooth, strictly convex** `K`; polytopes/flat faces need a perturbation/limiting argument (M–OM already use a perturbation to pass from basis to general vectors — same flavor).

### Crux #2 — The count (analogue of Bézout `2ⁿ`)
This is the genuinely new ingredient. For non-quadratic / non-round constraints the right count is **BKK**: number of solutions = mixed volume of Newton polytopes (for generic coefficients). Two things to verify per body class:
- the system is a **0-dim complete intersection** (so Euler–Jacobi applies in its toric/BKK form),
- the BKK count is **attained by simple real roots** in bijection with the body's combinatorial cells (so the "one good root must exist" pigeonhole works).

### Crux #3 — Vanishing identity
Euler–Jacobi has a toric/BKK generalization (Khovanskii; the "toric residue" / global residue vanishing). Need the precise degree condition replacing `deg g ≤ n−1`. **Action item:** pin down the exact statement (Tier-3 reading).

## C. Sanity ladder (do these in order, on paper)
1. n=2 by hand for a non-symmetric `K` (e.g. a triangle): write the width functionals, the critical system, count roots, check the relative-width inequality drops out. If it works, the whole approach has legs.
2. Simplex in ℝⁿ (M2 entry): Newton polytopes are simple; compute BKK.
3. Symmetric `K` (M1): must recover Ball 1991 — if the engine *can't* do the already-proven symmetric case, stop and rethink.

> Note: (1) and (3) are the cheap falsifiers. Run them before any heavy machinery.
