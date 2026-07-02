# M1′ — Working notes: the symmetric Euclidean case WITH shifts
### Critical-point / convex-potential / Euler–Jacobi attack on CRUX 0
> Status: **research in progress.** Strict tagging: `[CHECKED]` = derived and verified
> here; `[OPEN]` = not established, do not cite as proved. Nothing here is a theorem yet.
> Date: 2026-06-27.

---

## 0. Target of M1′

Euclidean specialization of Ball's Theorem 2 (symmetric, **with shifts**):

> **(Shifted Hilbert plank — the statement we want to recover.)** Let
> $v_1,\dots,v_n\in\mathbb R^n$ be unit vectors, $m_1,\dots,m_n\in\mathbb R$ shifts,
> and $p_1,\dots,p_n>0$ with $\sum_j p_j=1$. Then there is a point $u$ in the unit
> ball with $|\langle v_j,u\rangle-m_j|\ge p_j$ for all $j$.

The centered case $m_j=0$ is the Martínez–Ortega-Moreno / GOP result. The whole
question of M1′ is whether the **engine survives the shift** $m_j\ne0$. The answer
from these notes: **the three structural pillars survive cleanly; two genuine
obstacles remain (the test polynomial and the unit-ball normalization).**

Throughout, basis case $n=d$, $v_1,\dots,v_n$ a basis; $G=(\langle v_i,v_j\rangle)$
Gram, $A=G^{-1}$; dual basis $w_j$ ($\langle v_i,w_j\rangle=\delta_{ij}$);
$y_j=\langle v_j,x\rangle$, $z=Ay$ so $x=\sum_k z_k v_k$.

---

## 1. The shifted critical system is still degree 2  `[CHECKED]`

Mimic M–OM but with a **shifted log-barrier potential**:
$$
\Psi_m(x)\;=\;\tfrac12\|x\|^2\;-\;\sum_{j=1}^n p_j\,\log\bigl|\langle v_j,x\rangle-m_j\bigr|.
$$
Stationarity $\nabla\Psi_m=0$:
$$
x\;=\;\sum_{j=1}^n \frac{p_j\,v_j}{\langle v_j,x\rangle-m_j}. \tag{1}
$$
Pair (1) with the dual vector $w_i$. Since $\langle x,w_i\rangle=z_i$ and
$\langle v_j,w_i\rangle=\delta_{ij}$,
$$
z_i=\frac{p_i}{y_i-m_i}\quad\Longleftrightarrow\quad (y_i-m_i)\,z_i=p_i
\quad\Longleftrightarrow\quad \boxed{\,h_i(y):=(y_i-m_i)\,(Ay)_i-p_i=0\,}. \tag{2}
$$
Each $h_i$ is **degree 2** in $y$ (affine factor $\times$ linear factor): the shift
$m_i$ only translates the first factor, it does **not** raise the degree. Bézout
number $=\prod_i\deg h_i = 2^n$, identical to the centered case.

> **Significance.** This is the core good news of M1′: the affine shift is absorbed
> with no degree penalty. The system is the centered M–OM system
> $y_i(Ay)_i=p_i$ with $y_i\rightsquigarrow y_i-m_i$ in the first factor only.

---

## 2. Reality of the critical locus survives  `[CHECKED]` (CRUX 1)

Replay M–OM Lemma 2.1 on (1). Let $u=a+ib\in\mathbb C^n$ solve (1). Put
$A_j:=\langle v_j,a\rangle-m_j$ and $B_j:=\langle v_j,b\rangle$ (note $m_j$ enters
**only the real part** because $m_j\in\mathbb R$). Then
$\langle v_j,u\rangle-m_j=A_j+iB_j$ and
$$
u=\sum_j \frac{p_j v_j}{A_j+iB_j}=\sum_j \frac{p_j(A_j-iB_j)}{A_j^2+B_j^2}\,v_j .
$$
Imaginary part: $b=-\sum_j \dfrac{p_j B_j}{A_j^2+B_j^2}\,v_j$. Pair with $b$ (using
$\langle v_j,b\rangle=B_j$):
$$
\|b\|^2=-\sum_j \frac{p_j\,B_j^2}{A_j^2+B_j^2}\le 0\quad(\text{since }p_j>0)
\;\Longrightarrow\; b=0 .
$$
So every complex solution is real. **The shift is harmless to reality** precisely
because it is real and lands in $A_j$ only. ✓ CRUX 1 holds for shifts.

---

## 3. Exact count $2^n$, simple, no zeros at infinity  `[CHECKED]` (CRUX 2)

$\Psi_m$ is a sum of $\tfrac12\|x\|^2$ and convex log-barriers, so on each
connected component (chamber) of $\mathbb R^n\setminus\bigcup_j\{\langle v_j,x\rangle=m_j\}$
it is **strictly convex** (Hessian $=I+\sum_j p_j\,\dfrac{v_j\otimes v_j}{(y_j-m_j)^2}\succ0$),
$\to+\infty$ at the chamber walls (log barrier) and at infinity (the $\tfrac12\|x\|^2$
term). Hence $\Psi_m$ has **exactly one** critical point per chamber.

In the basis case $x\mapsto y$ is a linear isomorphism and the walls are the $n$
coordinate hyperplanes $\{y_j=m_j\}$, whose arrangement has exactly $2^n$ chambers
(the sign patterns of $y_j-m_j$). So there are **exactly $2^n$ real critical points**.
Since this equals the Bézout number and they are distinct, the system has its full
complex count realized by $2^n$ **simple real** solutions $\Rightarrow$ **no solutions
at infinity, all Jacobians nonzero**. These are exactly the Euler–Jacobi hypotheses.
✓ CRUX 2 holds, and — crucially — **via the convex potential, with no BKK needed.**

*(Degenerate $m$ making the affine hyperplanes non-generic: handle by a limiting
argument from generic $m$, as M–OM do for coincident vectors.)*

> **Why all $2^n$ chambers are non-empty.** Since $V$ (rows $v_j$) is invertible,
> the $n$ affine walls $\{\langle v_j,x\rangle=m_j\}$ share the single common point
> $x^\*=V^{-1}m$; the arrangement is *central* at $x^\*$, so all $2^n$ sign patterns
> occur as translated-orthant cones with apex $x^\*$. On each such cone $\Psi_m\to+\infty$
> on every wall AND at the apex (all $\log$ terms blow up) AND at infinity ($\tfrac12\|x\|^2$),
> so the minimizer is interior. ✓

> **`[NUMERICALLY VALIDATED]`** `experiments/m1_check.py` (pure Python). For random
> generic instances $n=2,3,4,5$ (4 seeds each) it finds **exactly $2^n$** real
> critical points and verifies, to $\le 10^{-7}$ (mostly machine precision
> $\sim10^{-14}$): $h(y)=0$, the Jacobian identity of §4, and eq. (3) of §5b. **All
> checks pass.**
>
> **New phenomenon surfaced by the validation (records as a finding):** when the
> shifts are large relative to the geometry, $\|x^\*\|=\|V^{-1}m\|$ is large, and
> the critical points in the "far" chambers become **severely ill-conditioned** —
> e.g. one instance had $\|x^\*\|\approx 68$ with a witness sitting $\sim p_j/\|x\|
> \approx 3\times10^{-3}$ from a wall, condition number $\sim10^{8}$, so plain Newton
> stalls at gradient $\sim10^{-8}$. The critical point *exists* (gradient descends
> monotonically to it) but is numerically delicate. **This ill-conditioning is the
> analytic signature of CRUX 0 (broken homogeneity): as $m\to$ large the structure
> degrades, and any eventual proof/quantitative bound must control $\|x^\*\|$ — likely
> the role of the $(n+1)$-homogenization or a constraint that keeps the witness in
> the unit ball.**

---

## 4. The Jacobian and the positive weight  `[CHECKED]`

From $h_i=(y_i-m_i)(Ay)_i-p_i$,
$\partial h_i/\partial y_k=\delta_{ik}(Ay)_i+(y_i-m_i)A_{ik}$, i.e.
$J_h=\operatorname{diag}\bigl((Ay)_i\bigr)+\operatorname{diag}(y_i-m_i)\,A$.
At a solution $(Ay)_i=p_i/(y_i-m_i)$, so factoring $\operatorname{diag}(y_i-m_i)$:
$$
\det J_h=\Bigl(\prod_i (y_i-m_i)\Bigr)\,
\det\!\Bigl(A+\operatorname{diag}\tfrac{p_i}{(y_i-m_i)^2}\Bigr)
=:\;P_m(y)\,/\,\mu(y),
$$
where $P_m(y):=\prod_i(y_i-m_i)$ and
$\mu(y):=\det\!\bigl(A+\operatorname{diag}\tfrac{p_i}{(y_i-m_i)^2}\bigr)^{-1}>0$
(sum of a positive-definite and a positive-semidefinite matrix). This is the exact
analogue of the M–OM weight $\mu>0$; **its positivity is what will turn an
Euler–Jacobi average into an existence statement.** ✓

---

## 5. The two genuine obstacles  `[OPEN]`

### 5a. The test polynomial / target inequality (P3)  `[OPEN]`
M–OM use $g=\Delta P$ with the identity $\Delta P=P\,(n^2-\sum_j 1/y_j^2)$, of degree
$n-2\le \sum\deg h_i-n-1=n-1$, so that Euler–Jacobi gives
$\sum_{\text{crit}}\bigl(n^2-\sum_j 1/y_j^2\bigr)\mu=0$ and $\mu>0$ forces a witness
with $\sum_j 1/y_j^2\le n^2$.

For the shifted system we need a polynomial $g(y)$, $\deg g\le n-1$, with
$$
\frac{g(y)}{\det J_h(y)}\;=\;\frac{g(y)\,\mu(y)}{P_m(y)}\;\stackrel?=\;
\Bigl(C-\textstyle\sum_j \tfrac{p_j^2}{(y_j-m_j)^2}\Bigr)\mu(y)
$$
at solutions, i.e. $g(y)=P_m(y)\bigl(C-\sum_j p_j^2/(y_j-m_j)^2\bigr)$ — but
$P_m/(y_j-m_j)^2=\prod_{l\ne j}(y_l-m_l)/(y_j-m_j)$ is **not** a polynomial, exactly
as in the centered case. M–OM resolve this through the Laplacian identity, not by
naive multiplication. **OPEN:** find the shifted analogue. Candidates to test:
- $g=\Delta P_m$ where $P_m=\prod(y_j-m_j)$ pulled back to $x$ (note $y_j=\langle v_j,x\rangle$,
  so $P_m$ as a function of $x$ is a product of **affine** forms; its $x$-Laplacian
  is computable). Conjecture: $\Delta_x P_m = P_m\bigl(\kappa-\sum_j \|v_j\|^2/(y_j-m_j)^2\bigr)$
  for some constant $\kappa$ depending on the $\langle v_i,v_j\rangle$ — **must be
  derived and checked**; the cross terms $\sum_{i\ne j}\langle v_i,v_j\rangle/((y_i-m_i)(y_j-m_j))$
  are what made the centered identity work and need re-checking with shifts.
- The correct constant $C$ (the centered "$n^2$") and whether the resulting bound is
  $\sum p_j^2/(y_j-m_j)^2\le 1$ (which would give $|y_j-m_j|\ge p_j$, the plank) — **unverified.**

### 5b. The unit-ball normalization / lost homogeneity (the heart of CRUX 0)  `[OPEN]`
Centered M–OM get $\|u\|=1$ for free: pairing $\nabla\Psi=0$ with $x$ gives
$\|x\|^2=\sum p_j=1$. With shifts, pairing (1) with $x$:
$$
\|u\|^2=\sum_j \frac{p_j\,y_j}{y_j-m_j}
=\sum_j p_j\Bigl(1+\frac{m_j}{y_j-m_j}\Bigr)
=1+\sum_j \frac{p_j\,m_j}{y_j-m_j}. \tag{3}
$$
So $\|u\|^2-1=\sum_j p_j m_j/(y_j-m_j)$ is **not** automatically $0$ or even signed.
The witness critical point need not lie on the unit sphere or even in the unit ball.
This broken homogeneity is the real content of CRUX 0 and is **unresolved**.

**Most promising route — projective homogenization (to test next):** lift the $n$
affine forms $\langle v_j,x\rangle-m_j$ to $n$ **linear** forms
$L_j(x_0,x)=\langle v_j,x\rangle-m_j x_0$ on $\mathbb R^{n+1}$, and **adjoin the
coordinate form $L_0=x_0$** to obtain $n+1$ linear forms in $\mathbb R^{n+1}$ — a
square (basis) system to which the centered M–OM machinery applies directly. Then:
- the strong inequality for the $(n+1)$ forms would read
  $\sum_{j=0}^n q_j^2/\langle V_j,U\rangle^2\le 1$ on the unit sphere $S^n$, with the
  extra $L_0=x_0$ term controlling the affine chart / the $\|x\|\le1$ membership;
- **Heuristic worth checking:** the "$+1$" extra functional may be exactly the origin
  of the **$1/(n+1)$** in Ball's corollary (translate of $\tfrac1{n+1}C$). If
  applying the $(n+1)$-vector bound reproduces Ball's $1/(n+1)$, that is the clean
  conceptual proof. **Unverified — this is the first thing to do next.**

---

## 6. Status of M1′ after this session

| Pillar | Centered (M–OM) | **Shifted (here)** |
|---|---|---|
| Critical system degree | 2 | **2** `[CHECKED]` — shift absorbed, no penalty |
| Reality (CRUX 1) | ✓ | **✓** `[CHECKED]` — $m_j$ real ⇒ harmless |
| Count $2^n$, simple, no $\infty$ (CRUX 2) | ✓ convex potential | **✓** `[CHECKED + NUMERICALLY VALIDATED]` — shifted barrier $\Psi_m$ |
| $\det J_h=P_m/\mu$, $\mu>0$ | ✓ | **✓** `[CHECKED + NUM. VALIDATED to ~1e-14]` |
| Test polynomial / target ineq (P3) | $\Delta P$ | **`[OPEN]`** — shifted Laplacian identity |
| Unit-ball normalization (CRUX 0 core) | free ($\|u\|=1$) | **`[OPEN]`** — eq. (3); try $(n+1)$-homogenization |

**Headline:** three of the four structural pillars transfer to the shifted (affine)
case essentially verbatim, AND the $(n{+}1)$-homogenization (§8) now yields a **rigorous,
numerically-validated affine plank theorem with shifts** (Proposition M1.1) — order-correct
$\sim1/n$ margin in the unit ball. **G1 is PASSED:** the engine reaches the affine case.
The remaining work is to recover the **sharp** constant $1/(n+1)$, not to establish feasibility.

## 8. A rigorous shifted plank theorem via $(n{+}1)$-homogenization  `[PROVED mod GOP + NUM. VALIDATED]`

The homogenization route of §5b **closes a genuine affine result** — not Ball's sharp
constant, but an order-correct shifted plank bound obtained directly from the engine.
This is the decisive G1 outcome: **the critical-point/Euler–Jacobi machine reaches the
shifted (affine) case**, which the Verreault survey doubted the polynomial methods could.

> **Proposition M1.1.** Let $v_1,\dots,v_n\in\mathbb R^n$ be unit vectors,
> $m_1,\dots,m_n\in\mathbb R$, and fix $q_0\in(0,1)$. Then there exists $\bar u\in\mathbb R^n$
> with
> $$\|\bar u\|\le \sqrt{\tfrac{1}{q_0^2}-1}\qquad\text{and}\qquad
> |\langle v_j,\bar u\rangle-m_j|\ \ge\ \frac{1-q_0}{n}\ \ (j=1,\dots,n).$$
> In particular, with $q_0=1/\sqrt2$: there is $\bar u$ in the **closed unit ball** with
> $$|\langle v_j,\bar u\rangle-m_j|\ \ge\ \frac{2-\sqrt2}{2n}\quad(j=1,\dots,n).$$

**Proof (modulo the proved GOP/Martínez–Ortega-Moreno strong inequality).**
In $\mathbb R^{n+1}$ (coordinates $(x_0,x)$) set the **unit** vectors $W_0=e_0$ and
$W_j=(-m_j,v_j)/\sqrt{1+m_j^2}$, and weights $q_0,\,q_j=(1-q_0)/n$, so $\sum_{a=0}^n q_a=1$.
By GOP Theorem 1 there is a unit $U=(U_0,x)\in S^{n}$ with
$\sum_{a=0}^n q_a^2/\langle W_a,U\rangle^2\le 1$. Since each summand is $\le1$:
$q_0^2/U_0^2\le1\Rightarrow U_0^2\ge q_0^2$ (take $U_0\ge q_0>0$); and
$q_j^2/\langle W_j,U\rangle^2\le1\Rightarrow |\langle v_j,x\rangle-m_jU_0|\ge q_j\sqrt{1+m_j^2}$.
Put $\bar u=x/U_0$. Then $\|\bar u\|^2=\|x\|^2/U_0^2=(1-U_0^2)/U_0^2=U_0^{-2}-1\le q_0^{-2}-1$,
and, using $U_0\le1$ and $\sqrt{1+m_j^2}\ge1$,
$|\langle v_j,\bar u\rangle-m_j|=|\langle v_j,x\rangle-m_jU_0|/U_0\ge q_j\sqrt{1+m_j^2}\ge q_j=(1-q_0)/n.$
The choice $q_0=1/\sqrt2$ gives $\sqrt{q_0^{-2}-1}=1$. $\qquad\blacksquare$

**Numerically validated** (`experiments/m1_homog.py` + verification run): over 60 random
instances $n=2,3,4,5$ with shifts up to $\pm3$, the engine's witness satisfies
$\|\bar u\|\le0.65<1$ and margin $\ge2.38\times$ the guaranteed $(1-1/\sqrt2)/n$ — no failures.

**Status / caveats.**
- This is **proved**, contingent only on GOP (itself proved, 2026). The steps above are
  elementary and were independently checked numerically. *This is the project's first theorem.*
- The constant $\tfrac{2-\sqrt2}{2n}\approx 0.293/n$ is **not sharp**: Ball's corollary gives
  $\approx 1/(n+1)$ (margin $\sim 1/n$, with $\|\bar u\|\le n/(n+1)$). Same order in $n$,
  worse constant by $\approx0.293$. **OPEN:** recover the sharp $1/(n+1)$ — candidate routes:
  (i) use the product/AM–GM (Theorem-2) form of the engine instead of the strong sum;
  (ii) the direct shifted critical system of §1–4 (which retains more structure than the
  black-box homogenization);
  (iii) optimize the lifted geometry (a better $(n+1)$-th vector / weights than $e_0,\,1/\sqrt2$).
- **G1 verdict: PASSED.** The engine demonstrably reaches the affine/shifted case with a
  rigorous, order-correct bound — CRUX 0 is *surmountable*, not fatal. The remaining work is
  about the *constant*, not feasibility.

## 9. Pursuing the sharp constant (M1″)  `[improved + structural cap proved]`

### 9.1 Improved constant via the FULL strong inequality  `[PROVED mod GOP + NUM. VALIDATED]`
Proposition M1.1 used only the per-coordinate consequence of GOP. Using the strong sum
*in full* gives a better constant. From the witness $U=(U_0,x)$, $\bar u=x/U_0$:
the $a{=}0$ term is $q_0^2/U_0^2$, and the remaining terms, after multiplying by $U_0^2$
and using $\langle v_j,x\rangle-m_jU_0=U_0(\langle v_j,\bar u\rangle-m_j)$ and $\sqrt{1+m_j^2}\ge1$,
give
$$\sum_{j=1}^n \frac{q_j^2}{(\langle v_j,\bar u\rangle-m_j)^2}\ \le\ U_0^2-q_0^2\ \le\ 1-q_0^2 .$$
Hence per coordinate $|\langle v_j,\bar u\rangle-m_j|\ge q_j/\sqrt{1-q_0^2}
=\sqrt{\tfrac{1-q_0}{1+q_0}}\,\tfrac1n$. With $q_0=1/\sqrt2$ (which gives $\|\bar u\|\le1$):
$$\boxed{\ |\langle v_j,\bar u\rangle-m_j|\ \ge\ \frac{\sqrt2-1}{n}\quad(\bar u\in\text{unit ball}).\ }$$
This **improves Proposition M1.1's constant from $\tfrac{2-\sqrt2}{2n}\approx0.293/n$ to
$\tfrac{\sqrt2-1}{n}\approx0.414/n$**. Numerically validated (24/24 instances, shifts to $\pm1.5$:
$\|\bar u\|\le1$, strong sum $\le1-q_0^2=\tfrac12$, margin $\ge(\sqrt2-1)/n$). Moreover the
displayed inequality is itself a **shifted strong-polarization bound** on $\bar u$ — see §9.3.

### 9.2 A structural cap: homogenization CANNOT reach $1/n$  `[argued]`
The guaranteed margin from this route is $\sqrt{\tfrac{1-q_0}{1+q_0}}\,\tfrac1n$, an
*increasing* function of decreasing $q_0$, while unit-ball membership requires
$\|\bar u\|\le\sqrt{q_0^{-2}-1}\le1\Rightarrow q_0\ge1/\sqrt2$. Hence the best achievable
guaranteed margin over all $q_0$ is exactly at $q_0=1/\sqrt2$:
$$\max_{q_0\ge1/\sqrt2}\sqrt{\tfrac{1-q_0}{1+q_0}}\,\tfrac1n=\sqrt{\tfrac{1-1/\sqrt2}{1+1/\sqrt2}}\,\tfrac1n
=(\sqrt2-1)\,\tfrac1n .$$
The lifting coordinate $W_0=e_0$ irreducibly consumes a $\ge1-(\sqrt2-1)=2-\sqrt2\approx0.586$
fraction of the polarization budget to buy ball membership. **So the $(n{+}1)$-homogenization
provably cannot deliver Ball's order-$1/n$ sharp plank constant** (Ball's Theorem 2, equal
weights, gives margin $1/n$ in the unit ball; the corollary's $1/(n+1)$ is the
fit-a-translate version). The gap is a constant factor $(\sqrt2-1)\approx0.414$, *not* an
order-in-$n$ gap.

### 9.3 Where the sharp constant actually lives — reframing the contribution
Two complementary facts clarify the target:
1. **For the bare plank constant, Bang's discrete lemma is already sharp.** In the
   *Euclidean* case Ball's matrix $A=(\langle v_i,v_j\rangle)=G$ is *already symmetric with
   unit diagonal*, so **no symmetrization is needed**: Bang's Lemma applies directly to $G$
   and yields margin $w_i$ ($\sum w_i=1$, e.g. $1/n$) with the point in the unit ball. This
   is the discrete $\{\pm1\}^n$ shadow of the engine's $2^n$ sign-chambers.
2. **The engine's genuinely new object is a *shifted strong* inequality**, §9.1:
   $\sum_j w_j^2/(\langle v_j,\bar u\rangle-m_j)^2\le 1$ for a point $\bar u$ in the ball
   (after rescaling $w_j$). This is *strictly stronger* than the plank statement (it bounds a
   sum of reciprocal squares, not just each term), and Bang's discrete lemma does **not** give
   it. The $(\sqrt2-1)$ factor is the price the homogenization pays in the *strong*-inequality
   constant, and optimizing/avoiding it is the real M1″/M2 question.

**Honest M1″ status.** The sharp *plank* constant ($\sim1/n$, and the $1/(n+1)$ translate
form) is attained by Bang's lemma on $G$ — a clean reproof, but discrete, not the strong
engine. The strong engine gives a *new, stronger* shifted inequality with constant
$(\sqrt2-1)/n$ via homogenization, provably capped there by §9.2. **Recovering the sharp
constant for the *strong* shifted inequality requires the direct system of §1–4 with its
test polynomial (§5a) — which avoids the homogenization's budget tax — and is the right
next target** (it also feeds directly into M2, the simplex).

## 10. The direct system, sharp (M1″ route (a))  `[major progress: §5a solved; unit-ball impasse isolated]`

Route (a) — the direct shifted system — was pushed hard. **It resolves the test-polynomial
problem (§5a) and yields the sharp margin $1/n$**, but the unit-ball placement of the witness
is a genuine obstruction (now precisely characterized).

### 10.1 The shifted Theorem A (sharp test polynomial)  `[PROVED mod EJ + NUM. VALIDATED to 1e-15]`
Take all weights $\alpha_j=1/n$ (so $s=n$), $L_j(x)=\langle v_j,x\rangle-m_j$,
$P_m=\prod_j L_j$. The $x$-Laplacian gives the polynomial identity
$\Delta P_m=\sum_{i\ne j}G_{ij}\prod_{l\ne i,j}L_l$ (degree $n-2$), i.e.
$\Delta P_m/P_m=\big\|\sum_j v_j/L_j\big\|^2-\sum_j 1/L_j^2$.
At a critical point of $\Psi_m$, $\sum_j v_j/L_j=n\,x$, so
$\Delta P_m/P_m=n^2\|x\|^2-\sum_j 1/L_j^2$; with eq. (3) ($\|x\|^2=1+\tfrac1n\sum_j m_j/L_j$),
$$\Delta P_m/P_m=n^2+n\sum_j\frac{m_j}{L_j}-\sum_j\frac1{L_j^2}.$$
The key step: the correction $g_2=\sum_j m_j\prod_{l\ne j}L_l$ (degree $n-1$) has
$g_2/P_m=\sum_j m_j/L_j$, so the test polynomial $g=\Delta P_m-n\,g_2$ (degree $\le n-1$,
within the Euler–Jacobi bound) **cancels the shift term**, giving
$$\boxed{\ \sum_{\text{crit}}\mu(x)\,\Big(n^2-\sum_j 1/L_j^2\Big)=0,\qquad \mu>0.\ }\tag{$\star\star$}$$
This is **M–OM's Theorem A verbatim but for the SHIFTED forms** — the shift is absorbed by
the correction. **Numerically validated to machine precision** ($\sim10^{-15}$) for $n=2,3,4$.
Since $\mu>0$, there is a critical point with $\sum_j 1/L_j^2\le n^2$, hence
$$|\langle v_j,x\rangle-m_j|\ \ge\ \tfrac1n\quad\text{for all }j\qquad\text{— the \emph{sharp} margin.}$$
**This closes the previously-open §5a.** It is the first derivation of a *shifted* strong
polarization identity, and it is sharp.

### 10.2 An explicit norm bound at the witness  `[PROVED]`
At the $(\star\star)$ witness, by Cauchy–Schwarz and $\sum_j 1/L_j^2\le n^2$,
$$\|x\|^2-1=\tfrac1n\sum_j\frac{m_j}{L_j}\le\tfrac1n\Big(\sum_j m_j^2\Big)^{1/2}\Big(\sum_j 1/L_j^2\Big)^{1/2}\le \tfrac1n\,\|m\|\,n=\|m\|,$$
so $\|x\|\le\sqrt{1+\|m\|}$. For $m=0$ this recovers $\|x\|=1$ (the centered M–OM case on the
sphere); the witness is in a ball whose radius excess over $1$ is controlled by the shift size.

> **Proposition M1.2 (engine, shifted, sharp margin).** For unit vectors $v_j$ and reals
> $m_j$, there is $x\in\mathbb R^n$ with $\|x\|\le\sqrt{1+\|m\|}$ and
> $|\langle v_j,x\rangle-m_j|\ge 1/n$ for all $j$.

This is a genuine new affine plank statement from the engine, **sharp in the margin**, with
an explicit (shift-dependent) norm bound.

### 10.3 The unit-ball impasse  `[characterized, numerically]`
Ball's Theorem 2 places the sharp-margin point in the **unit** ball ($\|x\|\le1$). The engine
does not, in general:
- The $(\star\star)$ witness can have $\|x\|>1$ (observed $\approx1.03$–$1.04$ for $n=3$);
- **No** critical point of $\Psi_m=\tfrac12\|x\|^2-\tfrac1n\sum\log|L_j|$ need satisfy *both*
  margin $\ge1/n$ and $\|x\|\le1$ (explicit failures: $n=3$, seeds 0,1).
- A **unit-ball-barrier** potential $\Phi=-\beta\log(1-\|x\|^2)-\tfrac1n\sum\log|L_j|$ keeps
  critical points inside the ball but its critical points are *not* the max-margin point
  (a maximin, not a log-potential critical point): observed best in-ball critical margin as
  low as $0.73/n$ even though $M^\*\!=\max_{\|x\|\le1}\min_j|L_j|\approx1.7/n$ exists.

**Root cause.** The engine's power is the *strong* inequality at an *unconstrained* critical
point; the unit-ball constraint is exactly what Bang's discrete lemma handles (via
$\sum\lambda_j^2\le1/n$ with small $\lambda_j=\theta_j=1/n$), whereas the continuous critical
points have large $\lambda_j=(1/n)/L_j$ near the walls. The barrier route turns the critical
system *rational* (not polynomial), which is precisely where the **toric/BKK Euler–Jacobi**
(CRUX 3, the M2 machinery) would be needed — so the in-ball sharp question merges into M2.

### 10.4 Verdict on route (a)
- **Win:** $(\star\star)$ — the shifted strong inequality, sharp margin $1/n$, test polynomial
  solved, validated. Plus the explicit norm bound (Prop. M1.2). These are real, citable results.
- **Open:** the *unit-ball* sharp constant via the continuous engine. It resists $\Psi_m$ and
  the ball-barrier; it appears to require either Bang's discrete lemma (Plan B) or the toric
  Euler–Jacobi on the rational ball-barrier system (which is the M2 toolset).
- **Recommendation:** bank $(\star\star)$ + Prop. M1.2 as the engine's genuine new contribution;
  use Bang's lemma on $G$ for the sharp *unit-ball* plank (Plan B, clean); and carry the
  ball-barrier/toric-EJ idea into M2, where the same machinery is needed for the simplex.

## 7. Immediate next steps (M1′ continuation)
1. Compute $\Delta_x P_m$ for $P_m(x)=\prod_j(\langle v_j,x\rangle-m_j)$ explicitly;
   check whether $\Delta_x P_m/P_m$ has the form $\kappa-\sum_j \|v_j\|^2/(y_j-m_j)^2
   + (\text{cross terms})$, and whether the cross terms vanish/control as in M–OM.
2. Set up the $(n+1)$-form homogenization $\{L_0=x_0,\,L_j=\langle v_j,x\rangle-m_jx_0\}$,
   run the centered strong-polarization bound, and check whether it yields the
   shifted plank with the $1/(n+1)$ constant.
3. Read Ambrus appendix + Ortega-Moreno 2111.03961/1906.04126 in parallel
   (informs both the normalization and the eventual M2 simplex step).
4. ~~Numerically validate §1–§4~~ **DONE** — `experiments/m1_check.py`, all checks pass
   for $n=2,3,4,5$; surfaced the large-shift ill-conditioning. *Next:* extend the
   script to empirically search for the right test polynomial $g$ / constant $C$ of
   §5a (evaluate candidate Laplacian identities at the computed critical points).
