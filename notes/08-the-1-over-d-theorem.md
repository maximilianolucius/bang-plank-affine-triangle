# The elegant 1/d theorem (Milestone 1, locked & rigorous)
> An elegant single-measure proof of $\sum \mathrm{rw}\ge 1/d$ for the affine plank problem,
> sharp at the simplex. For $d=2$: $\sum\mathrm{rw}\ge\tfrac12$ (Hint 1). Verified numerically.
> Date: 2026-06-27.

## Theorem
Let $K\subset\mathbb R^d$ be a convex body covered by planks $P_1,\dots,P_n$ (plank $P_a$ has
unit normal $u_a$ and width $w_a$; relative width $\mathrm{rw}(P_a)=w_a/w_K(u_a)$, where
$w_K(u)=\max_{x\in K}\langle u,x\rangle-\min_{x\in K}\langle u,x\rangle$). Then
$$\sum_{a=1}^n \mathrm{rw}(P_a)\ \ge\ \frac1d.$$
For $d=2$ this is $\sum\mathrm{rw}\ge\tfrac12$. The constant $1/d$ is sharp for the simplex.

## Proof (5 lines)
Let $\mu$ be the **uniform (Lebesgue) probability measure on $K$**.

**Step 1 — marginal peak bound.** Fix a direction $u$; normalize so $\langle u,\cdot\rangle$
ranges over $[0,w]$, $w=w_K(u)$. The marginal density of $\mu$ is $f(t)=V(t)/\mathrm{vol}(K)$,
where $V(t)=\mathrm{vol}_{d-1}\big(K\cap\{\langle u,\cdot\rangle=t\}\big)$. By the
**Brunn–Minkowski inequality**, $V^{1/(d-1)}$ is concave on $[0,w]$.

**Lemma.** If $f\ge0$ on $[0,w]$, $\int_0^w f=1$, and $g:=f^{1/(d-1)}$ is concave, then
$\max f\le d/w$.
*Proof.* Let $t^\*$ be where $g$ peaks, $g(t^\*)=g^\*$. By concavity and $g\ge0$,
$g(t)\ge g^\*\,h(t)$ where $h$ is the tent ($h(0)=h(w)=0$, $h(t^\*)=1$, linear). Hence
$f=g^{d-1}\ge (g^\*)^{d-1}h^{d-1}=(\max f)\,h^{d-1}$, so
$1=\int f\ge (\max f)\int_0^w h^{d-1}=(\max f)\big(\tfrac{t^\*}{d}+\tfrac{w-t^\*}{d}\big)
=(\max f)\,\tfrac{w}{d}$. Thus $\max f\le d/w$. $\square$

So $f(t)\le d/w_K(u)$ everywhere.

**Step 2 — per-plank bound.** For $P=\{a\le\langle u,\cdot\rangle\le b\}$,
$$\mu(P)=\int_a^b f\ \le\ \frac{d}{w_K(u)}\,(b-a)=d\cdot \mathrm{rw}(P).$$

**Step 3 — union bound over the covering.**
$$1=\mu(K)\le \mu\Big(\bigcup_a P_a\Big)\le\sum_a\mu(P_a)\le d\sum_a\mathrm{rw}(P_a)
\ \Longrightarrow\ \sum_a\mathrm{rw}(P_a)\ge\frac1d.\qquad\blacksquare$$

## Sharpness & the constant
Equality in the Lemma holds iff $g$ is the tent, i.e. $V(t)\propto h(t)^{d-1}$ — the
cross-sections shrink like a **cone/simplex**. Indeed the simplex realizes $c_d=d$:
- $d=2$ triangle: $c=2$ (numerically $1.993$). $d=3$ simplex: $c=3$ (num. $2.909$).
- Non-simplices are better: disk $c=4/\pi\approx1.27$ (num. $1.30$); square $c=2$ only along
  the diagonal, $c=1$ along axes.

So $\sum\mathrm{rw}\ge1/c_K$ with $c_K=\max_u(\text{marginal peak})\cdot w_K(u)\le d$, the max
$=d$ attained at the simplex. The simplex is the **extremal (hardest)** body for this method.

## Remarks
- This is an **elegant, self-contained, single-measure** proof of the classical $1/d$ bound for
  the affine plank problem (cf. John's theorem $+$ Bang $\to 1/d$, and Chambers–Mouille/Bezdek–
  Litvak). It uses **no** John ellipsoid and **no** Bang's lemma — only Brunn–Minkowski and a
  one-line peak estimate. The "factor $d$" $=$ the marginal-peak/uniform ratio (the "$2$" for
  $d=2$).
- **Numerically validated:** $\max_P\mu(P)/\mathrm{rw}(P)$ matches $c_d$ across bodies/dims.
- **Why this caps at $1/d$ (not $1$):** $\mu(P)\le 1\cdot\mathrm{rw}(P)$ for all $P$ would force
  uniform marginals in all directions, impossible for $d\ge2$ ($\mathbb E[x_k]=\tfrac12$ vs
  $\sum x_k=1$). The single-measure/union-bound route is genuinely limited to $1/c\in[1/d,1)$;
  the sharp $\sum\mathrm{rw}\ge1$ (Bang, open) needs the covering's combinatorics. (Milestone 2.)
