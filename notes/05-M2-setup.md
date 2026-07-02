# M2 — The simplex case: setup, engine formulation, test plan

> **[BANNER 2026-06-30 — auditoría.]** Dos correcciones que invalidan conclusiones de abajo:
> - **La vía algebraica/tórica está MUERTA** (ver `notes/15` [refutada definitivamente],
>   `notes/23 D13`, `notes/24`): al limpiar los denominadores **no-Laurent** del sistema de
>   gradientes de ancho relativo, la resultante densa es **idénticamente nula** (curvas
>   enteras de raíces en el infinito proyectivo). Por tanto **§5c ("el símplex requiere
>   genuinamente la maquinaria toric Euler–Jacobi") queda obsoleto**: no es que la requiera y
>   funcione — es que ni el crudo ni el tórico cierran sin desingularización (blow-ups). El
>   optimismo pro-tórico de esta nota **no sobrevivió**.
> - **Foco del "simplex" corregido** (`notes/40`, fuente primaria Ambrus): la reducción de
>   Ambrus **no** produce el `d`-símplex sino un símplex de dimensión **`2d−1`** (para `d=2`,
>   un tetraedro en `R⁴`, no el triángulo). "Probar Bang para el triángulo ⟹ planos generales"
>   **no** es la reducción de Ambrus. El §1 de abajo ("Σ para el simplex ⟹ todo") es correcto
>   como enunciado pero el objetivo es *todos* los símplices, dim `2d−1`.
>
> Lo que SÍ sobrevive de esta nota: **§5b** (hallazgo real y correcto — los testigos viven en
> las **esquinas** del símplex, donde las barreras de faceta los repelen; el motor de barrera
> falla en cuerpos acotados) y la formulación `(†)` del potencial. Ver banner análogo en
> `notes/06`.

> Status: **setup + initial exploration.** Strict tagging `[CHECKED]` / `[OPEN]`.
> Builds on M1 (the engine), the M0 toric Euler–Jacobi toolbox, and the merge with the
> unit-ball-sharp question (M1 §10.3). Date: 2026-06-27.

## 1. Why the simplex (Ambrus reduction)  `[CONFIRMED in M0]`
Ambrus (2010, *Appendix: Plank problems*): **proving Bang's affine conjecture for simplices
implies it for all convex bodies.** Independently cited by Bakaev–Yehudayoff. So the entire
conjecture reduces to:

> **Target (simplex affine plank).** If a simplex $K\subset\mathbb R^d$ is covered by planks
> $P_1,\dots,P_n$ (normal $u_i$, width $w_i$), then $\sum_i w_i/w_K(u_i)\ge 1$, where
> $w_K(u)=\max_{x\in K}\langle u,x\rangle-\min_{x\in K}\langle u,x\rangle$.

⚠️ Caveats from M0 (must resolve before relying on Ambrus): the appendix is unpublished;
reconcile the $\tfrac12$ vs $1$ (half-width) normalization. **Action:** read the appendix.

## 2. Contrapositive — what the engine must produce
Equivalently: if $\sum_i w_i/w_K(u_i)<1$ then the planks do **not** cover $K$, i.e.
$$\exists\,x\in K\ \text{ with }\ |\langle u_i,x\rangle-m_i|>w_i\ \ \forall i,$$
where plank $P_i=\{x:|\langle u_i,x\rangle-m_i|\le w_i\}$. The engine's job: **construct such
an $x$ from a critical point**, with the relative-width normalization $w_K(u_i)$ controlling
the constant.

## 3. The engine: a unified log-barrier on (simplex $\cap$ plank-complement)
Write $K=\{x:\langle a_k,x\rangle\le b_k,\ k=0,\dots,d\}$ ($d{+}1$ facets). Potential on a
chamber (cell of the $n$ plank-hyperplanes inside $K$):
$$
\Phi(x)=-\sum_{k=0}^{d} c_k\log\bigl(b_k-\langle a_k,x\rangle\bigr)
        -\sum_{i=1}^{n}\alpha_i\log\bigl|\langle u_i,x\rangle-m_i\bigr|,\qquad c_k,\alpha_i>0.
$$
Critical equation:
$$
\nabla\Phi=\sum_{k} \frac{c_k\,a_k}{b_k-\langle a_k,x\rangle}
          -\sum_{i} \frac{\alpha_i\,u_i}{\langle u_i,x\rangle-m_i}=0. \tag{$\dagger$}
$$
- This **generalizes the unit-ball engine** of M1 (there the $d{+}1$ facet terms are replaced
  by the single $\tfrac12\|x\|^2$ or the ball barrier $-\beta\log(1-\|x\|^2)$).
- Critical points lie **inside $K$** and avoid the planks — exactly the points we want.
- The system $(\dagger)$ is **rational**; clearing denominators gives a sparse polynomial
  system whose root count is governed by **BKK**, and the vanishing identity by **toric
  Euler–Jacobi** (the M0 toolbox: D'Andrea–Dickenstein 2026; condition $\mathrm{supp}(g)\subset
  \mathrm{int}(P_1+\dots)$).

## 4. The three pillars to establish (the hard core)
| Pillar | Question for the simplex system $(\dagger)$ |
|---|---|
| **P1 reality** | Does the imaginary-part/energy argument survive? Hessian $=\sum_k c_k\frac{a_k\otimes a_k}{(\cdot)^2}+\sum_i \alpha_i\frac{u_i\otimes u_i}{(\cdot)^2}\succ0$ — same PSD structure as M1, so plausibly yes. |
| **P2 count (BKK)** | Compute Newton polytopes of $(\dagger)$ cleared; is the count the BKK mixed volume, attained by simple real roots in bijection with the chambers (cells of $n$ planks $\cap\,K$)? |
| **P3 toric EJ** | Find a test polynomial $g$ (support in the interior of the Minkowski sum) whose toric-EJ identity forces a witness with $\sum_i w_i/w_K(u_i)\ge1$. The relative-width normalization $w_K(u_i)$ must enter through the weights $\alpha_i$ or $g$. |

**Key transferable win from M1 §10.1:** the *shift-cancellation* trick (subtract a correction
$g_2=\sum_i m_i\prod_{l\ne i}L_l$ to kill the shift term, identity $(\star\star)$) is exactly
the device likely needed for P3 here — the planks are shifted, and the facet barriers add
$d{+}1$ more affine forms. The simplex test polynomial is presumably
$\Delta\big(\prod_k(b_k-\langle a_k,x\rangle)^{c_k}\prod_i(\langle u_i,x\rangle-m_i)^{\alpha_i}\big)$
minus shift/curvature corrections — **to be derived**.

## 5. Test plan (numerical-first, as in M1)
1. **d=2 triangle testbed.** Build a triangle, $n$ planks, compute $w_K(u_i)$, the engine
   critical points of $(\dagger)$. Verify: (a) when $\sum w_i/w_K(u_i)<1$, some critical point
   avoids all planks (⟹ no cover); (b) the count of critical points vs #chambers vs BKK.
2. **Hunter extremal config.** Equilateral triangle, 3 planks, $\sum=1$ (the sharp case, =
   Chambers–Mouille Remark 4). Check the engine's behaviour at the extremal locus (where any
   proof must be tight) — this is the decisive stress test.
3. **Reality (P1).** Numerically confirm all critical solutions of the cleared system are real.
4. **BKK (P2).** For small $d,n$ compute Newton polytopes + mixed volume (SageMath/by hand);
   compare to observed root count.
5. **Toric EJ (P3).** Empirically search for the test polynomial: evaluate candidate
   Laplacian/curvature combinations at the computed critical points (as in M1 §5a/§10.1).

## 5b. Initial findings (d=2 triangle testbed)  `[numerically established]`
`experiments/m2_triangle.py` + corner-localization run:
- **The barrier-engine's critical points (analytic centers) systematically MISS the
  witnesses.** For an equilateral triangle with 3 centered planks parallel to the sides at
  $\sum \mathrm{rw}=0.84<1$: uncovered points exist (14.6% of the triangle) and **100% of them
  lie within $0.25$ of a vertex** (mean distance to nearest vertex $0.134$ vs to centroid
  $0.452$). The centroid / central analytic center is **covered**.
- **Root cause (confirmed, structural):** the witnesses (uncovered points) live at the simplex
  **corners**, where the facet log-barriers $\to+\infty$ and *repel* the critical points. The
  analytic centers sit centrally and are covered. **This is exactly the obstacle of M1 §10.3
  (ball-barrier pushes away from the witness), now confirmed for bounded bodies in general.**
- Consequence: the naive "find a critical point avoiding all planks" does **not** work for
  bounded bodies. The barrier-engine witnesses non-covering only on boundaryless domains
  (the sphere — M–OM's setting).

## 5c. What this tells us about the right machinery  `[strategic]`
The corner witnesses are precisely the points where several facet-hyperplanes meet — the
**toric-boundary divisors** of the simplex's toric variety. The classical (dense) critical-point
picture cannot see them; the **toric Euler–Jacobi / global-residue** theorem (M0 toolbox:
D'Andrea–Dickenstein 2026) is built exactly to account for *zeros at toric infinity / on
boundary divisors*. So:
> **The simplex (and the unit-ball-sharp) problem genuinely requires the toric Euler–Jacobi
> machinery — not the elementary barrier engine.** The witnesses live on the boundary divisors
> that the toric residue theorem is designed to handle. This is the real, hard, unexplored core
> (CRUX 3 + P2/P3 for the simplex), and it is where any genuine advance must happen.

This both (i) explains *why* the elementary engine succeeded only on the sphere, and (ii)
pinpoints the toric residue calculus as the necessary tool — consistent with the M0 finding
that this calculus has never been applied to planks.

## 6. Honest scope
Proving M2 in full ≈ proving Bang's conjecture — a months-long program. This session:
formulate $(\dagger)$, build the triangle testbed, get initial signal on P1–P2 and on whether
$(\dagger)$'s critical points witness non-covering. Full P3 (the simplex test polynomial) and
the BKK analysis are the substantive open work.
