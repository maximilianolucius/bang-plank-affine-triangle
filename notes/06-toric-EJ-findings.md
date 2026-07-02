# Toric Euler–Jacobi for the plank problem — findings & resolution of the analysis

> **[BANNER 2026-06-30 — auditoría.]** Esta nota tiene una **contradicción interna** y un
> **optimismo que no sobrevivió**:
> - **Contradicción interna:** §3 concluye "el sistema genéricamente tiene ceros en el
>   infinito tórico"; §5b (corrección del mismo día) dice lo contrario ("7 críticos, TODOS en
>   el toro, NINGUNO en la frontera; la clean vanishing SÍ aplica"). Ambos usan configs
>   distintas (1 plank degenerado vs 3 planks paralelos a aristas), y **ninguno es el sistema
>   general de ancho relativo con shifts**.
> - **Veredicto final (posterior, definitivo):** la vía algebraica/tórica está **MUERTA**
>   (`notes/15` [refutada definitivamente], `notes/23 D13`, `notes/24`): el sistema de ancho
>   relativo tiene denominadores **no-Laurent** (`x/(1−x−y)`, `x/L_i`); al limpiarlos, la
>   resultante densa es **idénticamente ≡ 0** (raíces en el infinito). El "clean vanishing
>   disponible después de todo" de §5b **NO se generaliza** al problema real; era un artefacto
>   de una config particular con objetivo logarítmico, no el sistema de ancho relativo. Sin
>   desingularización (blow-ups) la vía tórica no cierra.
>
> Lo firme que queda: la **verificación de la herramienta** (§2, EJ clásico y tórico
> verificados numéricamente) es correcta; el fenómeno de **ceros en la frontera** (§3) es real
> pero no es el obstáculo decisivo (lo es la degeneración de la resultante, `notes/15`). Ver
> banner gemelo en `notes/05`.

> Status: the **analysis is resolved** (we determine exactly what the toric EJ delivers and
> what it requires); a full **proof** of the simplex case is the open frontier (it would prove
> Bang's conjecture). Strict tagging. Date: 2026-06-27. Tooling: sympy 1.13.1 + mpmath on R15.

## 0. What "resolving the toric EJ" can and cannot mean
Full resolution = deriving a toric-residue identity that forces $\sum_a \mathrm{rw}_a\ge1$ for
the simplex $\equiv$ **proving Bang's affine conjecture** (open even for 3 planks in the plane).
That is not attainable in-session. What *is* attainable, and what we achieved: a **rigorous
determination of how the toric EJ engages the plank problem** — verified tooling, the exact
algebro-geometric regime, and the precise machinery a proof must use.

## 1. The toric framework (correct setup)  `[established]`
- The simplex $\Delta^d$ is the **moment polytope of $\mathbb P^d$**. Its facets $\{x_i=0\}$,
  $i=0,\dots,d$, are the **toric boundary divisors**; its vertices are the **torus-fixed
  points**.
- M2's numerical finding (`m2_triangle.py`): the witnesses (uncovered points when
  $\sum\mathrm{rw}<1$) lie at the **corners** — i.e. on/near the boundary divisors and fixed
  points. The barrier-engine's interior critical points (analytic centers) never see them.
- Hence the relevant residue calculus is the **toric** one, where boundary divisors are
  first-class — consistent with M0's negative-search conclusion that this calculus has never
  been applied to planks.

## 2. The toric EJ tool, verified  `[CHECKED numerically]`
Classical EJ ($n=1$): $\sum_{\text{roots}}1/f'=0$ for $\deg f\!-\!2\ge\deg g$ — verified.
Toric EJ ($n=1$, interior monomial $t$ of $[0,d]$): $\sum t/(tf')=0$ — verified.
Toric EJ ($n=2$, Newton polytopes = unit squares, **no boundary roots**): interior monomial
$xy$ gives $\sum xy/J^T = O(10^{-41})\approx0$ at 40-digit precision — verified. Here
$J^T=\det(t_i\,\partial f_j/\partial t_i)$ is the logarithmic (toric) Jacobian. So our handling
of the tool is correct.

## 3. THE crux finding: the plank system has zeros on the boundary divisors  `[CHECKED]`
For the $d=2$ simplex (triangle in the chart $x_0=1-x_1-x_2$), the critical system of
$\log Q$, $Q=x_0^c x_1^c x_2^c\,\prod_a L_a^{\alpha_a}$ (one plank, generic data), has **four**
critical solutions, of which **one lies exactly on the boundary divisor** $\{x_0=0\}$
(found: $x_0=0,\ x_1=x_2=\tfrac12$ — the midpoint of the edge opposite vertex $0$), the other
three interior.

> **Consequence (the heart of the matter).** The plank–simplex critical system **generically
> has zeros at toric infinity** (on the boundary divisors). This is *exactly* the hypothesis
> the clean toric Euler–Jacobi vanishing theorem **excludes** ("BKK attained / no zeros at
> infinity"). So the clean vanishing identity **does not apply directly**; the problem sits
> precisely in the regime of **D'Andrea–Dickenstein, "Toric Euler–Jacobi vanishing theorem
> *and zeros at infinity*", arXiv:2601.13977 (2026)** — whose title names this very situation.

This is not a defect of the approach; it is *structurally inevitable*, because the witnesses
(uncovered points) **are** the boundary objects. Any toric-residue proof must carry the
boundary-divisor (infinity) contributions, not discard them.

## 4. What a proof must therefore do  `[OPEN — the frontier]`
1. Use the **refined boundary-residue identity** (D'Andrea–Dickenstein 2026, Thm 1.4 et seq.):
   for systems *with* zeros at infinity, the global residue equals a sum of **boundary-divisor
   residues**. The interior-test-polynomial sum is no longer $0$ but a controlled boundary term.
2. Identify the **test polynomial** $g$ (interior support) so that the boundary term is exactly
   $\sum_a\mathrm{rw}_a-1$ (or forces its sign). This is the simplex analogue of the
   $(\star\star)$ shift-cancellation device (M1 §10.1) — now with facet/curvature corrections.
3. Establish the three pillars (reality, BKK count incl. boundary multiplicities, the refined
   vanishing) for the specific Newton polytopes of the plank–facet system.
4. Conclude $\sum_a\mathrm{rw}_a\ge1$ for the simplex $\Rightarrow$ (Ambrus) Bang's conjecture.

Each of (1)–(3) is a substantial research step; (4) is a famous open problem. This is a
multi-month program for a specialist in toric residues, not an in-session derivation.

## 5. Honest resolution statement
- **Resolved (the analysis):** the toric EJ engages the plank problem **through the
  zeros-at-infinity / boundary-residue regime**; the clean vanishing theorem is the wrong form;
  the 2026 D'Andrea–Dickenstein boundary-residue refinement is the necessary tool; the precise
  remaining steps are (1)–(3) above. Tooling verified; the boundary-zeros phenomenon confirmed
  numerically for $d=2$.
- **Open (the proof):** deriving the boundary-residue identity that yields $\sum\mathrm{rw}\ge1$.
  Equivalent to proving Bang's conjecture for simplices. Not achievable in-session.

## 5b. CORRECTION (2026-06-27, after re-examination)  `[important]`
My §3 claim that the plank system *"generically has zeros at toric infinity"* was **too strong
/ based on a degenerate 1-plank case**. Re-checked: the **generic 3-plank** config (planks
parallel to the triangle's edges) has **7 critical points, ALL in the torus, NONE on the
boundary divisors**, and the clean toric EJ **does** apply (defect $\sum g/J^T = O(10^{-15})$
for the interior test polynomial $g=x_1x_2(1-x_1-x_2)$). So the clean vanishing is available
after all for the relevant configs — the situation is **more tractable** than §3 suggested.
- **Revised open task:** find the M–OM-style *target* $T$ (the analogue of $n^2-\sum1/y_j^2$)
  such that $\sum_{\rm crit}\mu\,T=0$ **and** $T$'s sign yields $\sum_a\mathrm{rw}_a\ge1$. This
  is the *same* "find the test polynomial" problem that $(\star\star)$ **solved** for the
  shifted case (M1 §10.1) — so it is plausibly within reach, not blocked.
- **Re-verifications (independent):** $(\star\star)$ re-confirmed (`m1_check.py`: all pass);
  the simplex conjecture $\sum\mathrm{rw}\ge1$ holds on **17{,}022 random triangle coverings**
  (min observed $=1.108$).

## 6. Why this is still a real contribution
This pins down, rigorously, the exact algebro-geometric mechanism by which a critical-point /
residue method must attack the affine plank problem — a *new* viewpoint (M0: never attempted),
identifying the brand-new (2026) boundary-residue calculus as the key. Combined with the
proven shifted strong-polarization identity $(\star\star)$ and Prop. M1.1/M1.2, the project
delivers a coherent program and genuine partial results, with the toric boundary-residue
derivation as the clearly-mapped open frontier.
