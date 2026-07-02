# [REFUTADA — depende de peeling] The Fibonacci bootstrap (proof skeleton)

> **[REFUTADA 2026-06-30 — auditoría.]** Este "proof skeleton" de `Σrw ≥ 1` para el
> triángulo (¡la conjetura abierta!) es **matemáticamente insostenible**. Tres fallas,
> cualquiera fatal (ver `AUDITORIA_CLAUDE_30Jn.md §2 #1`):
> 1. **Depende de "peeling"**, refutado explícitamente en `paper-ready/BATTLE-PLAN-RESULTS.md`,
>    `notes/24` y `paper-ready/PROMPT-TWO-WALLS §3`: el corte de un plank inclinado **no** es
>    paralelo a la arista; el complemento es un **cuadrilátero**, no un triángulo semejante.
>    El paso central de abajo ("la subregión más allá del nivel `s` es `T'=sT` semejante")
>    solo vale para planks **paralelos a aristas**, no para el caso general.
> 2. **Conflación de inducciones:** la inducción es sobre niveles abstractos `k`
>    (`b_k = 1−1/F_k → 1`), pero una cobertura tiene un conjunto **finito y fijo** de planks;
>    nada garantiza que cubrir `T'` reinvoque la hipótesis con las mismas planchas ni con las
>    escalas de Fibonacci.
> 3. **El límite es imposible:** `b_k → 1` exige infinitos pasos de peeling sumando `rw` en
>    cada paso; con planks finitos no se puede pelar infinitamente. La recursión
>    `1/ε_{k+1}=1/ε_k+1/ε_{k−1}` es un **ajuste a posteriori** a `1/F_k`, no una derivación
>    geométrica.
>
> El único contenido firme reutilizable es la **base** `b_1 = 1/2` (= el teorema `1/d` de
> `notes/08`, correcto y verificado). Todo lo demás (bootstrap, trapezoide, recursión de
> Fibonacci) queda refutado. Documento conservado como registro histórico.

---

> *Texto original (refutado) a continuación.*

# The Fibonacci bootstrap: Σrw ≥ 1 for the triangle (proof skeleton)
> Reconstructed from the hint sequence 1−1/2, 1−1/3, 1−1/5, 1−1/8, … (Fibonacci gaps).
> Base case rigorous; bootstrap structure identified; precise constants = remaining work.
> Date: 2026-06-27.

## The target and the iteration
We prove $\sum_a \mathrm{rw}(P_a)\ge 1$ for any plank covering of a triangle by establishing
$$\sum\mathrm{rw}\ \ge\ b_k\ :=\ 1-\frac1{F_{k}}\qquad(F_k=2,3,5,8,13,21,\dots\ \text{Fibonacci}),$$
for every $k$, and letting $k\to\infty$ ($F_k\to\infty\Rightarrow\sum\mathrm{rw}\ge1$).
The **gaps** $\varepsilon_k:=1-b_k=1/F_k$ satisfy the harmonic two-term recursion
$$\frac1{\varepsilon_{k+1}}=\frac1{\varepsilon_k}+\frac1{\varepsilon_{k-1}}
\quad\Longleftrightarrow\quad \varepsilon_{k+1}=\frac{\varepsilon_k\varepsilon_{k-1}}{\varepsilon_k+\varepsilon_{k-1}}.$$
**Numerically confirmed**: this recursion with $\varepsilon_1=\tfrac12,\varepsilon_2=\tfrac13$
reproduces $1/F$ exactly and $b_k\uparrow1$.

## Base cases (rigorous)
- $b_1=\tfrac12$: the **area-measure** argument (note 08) — $\mu_{\rm area}(P)\le2\,\mathrm{rw}(P)$,
  union bound $\Rightarrow\sum\mathrm{rw}\ge\tfrac12$. *(Verified.)*
- A second base level $b_2=\tfrac23$ seeds the two-term recursion. *(To pin down.)*
- Trivial check $n=1$: a single covering plank has $\mathrm{rw}\ge1$.

## The bootstrap (structure identified; the engine of the Fibonacci)
The improvement is **combinatorial**, not a flatter measure (ruled out: the area measure with
$c=2$ is essentially optimal among single measures; concentrating mass only worsens the peak).

**Peeling into a similar triangle.** By affine invariance fix the triangle $T$. Choose a plank
direction along an altitude; the sub-region of $T$ "beyond level $s$" is a **scaled-similar copy
$T'=sT$** (scale $s\in(0,1)$, similar to $T$). Crucially, for a similar copy
$$\mathrm{rw}_{T'}(P)=\frac{w_P}{w_{T'}(u_P)}=\frac{w_P}{s\,w_T(u_P)}=\frac{\mathrm{rw}_T(P)}{s},$$
the **correct direction** for a *lower* bound (smaller similar triangle ⇒ larger rel. width,
and dividing by $s$ amplifies). Applying the inductive bound to the planks covering $T'$:
$$\sum_{P\text{ cover }T'}\mathrm{rw}_T(P)=s\sum\mathrm{rw}_{T'}(P)\ge s\,b_{k}.$$
Adding the peeled plank's own relative width gives a **self-map**
$$b_{k+1}=1-s(1-b_k)=1-s\,\varepsilon_k.$$

**Why two terms (the trapezoid).** Peeling leaves not just $T'$ but a **band/trapezoid**
$T\setminus T'$ between two similar triangles (scales $1$ and $s$). Covering the band engages a
*second* similar sub-triangle at a *different* scale — bringing in the previous level $b_{k-1}$.
The two scales $(s,s')$ tied to consecutive levels produce the **two-term** recursion; matching
$\varepsilon_{k+1}=\varepsilon_k\varepsilon_{k-1}/(\varepsilon_k+\varepsilon_{k-1})$ forces
$s=\varepsilon_{k-1}/(\varepsilon_k+\varepsilon_{k-1})$ (the scale at which the band's two
similar pieces balance). This is the Fibonacci engine.

## Status
- **Rigorous:** the iteration target/recursion ($1-1/F_k\to1$); the base $b_1=\tfrac12$;
  the self-map $b_{k+1}=1-s\varepsilon_k$ from peeling a similar triangle (correct direction).
- **Identified (skeleton):** the two-scale trapezoid step that yields the two-term Fibonacci
  recursion; the balancing scale $s=\varepsilon_{k-1}/(\varepsilon_k+\varepsilon_{k-1})$.
- **Remaining to make airtight:** the exact geometric covering of the band (trapezoid) by the
  two similar sub-triangles and the bookkeeping that the scales land on consecutive $\varepsilon$;
  handling that the band is not itself a triangle (subdivide into similar triangles).
- This skeleton matches **every** hint: the factor $2$ (base), the bound $1/2$ (Hint 1), and the
  Fibonacci gap sequence $1-1/F_k\to1$.
