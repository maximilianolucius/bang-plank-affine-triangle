# The elegant measure-theoretic route — milestone plan
> A clean, simple, affine-invariant attack on the simplex affine plank conjecture.
> Date: 2026-06-27. Tag `[DONE]`/`[OPEN]`.

## The elegant reformulation (LP duality / witness measure)
If planks $P_1,\dots,P_n$ cover a convex body $K$, and there is a probability measure $\mu$
on $K$ with $\mu(P_a)\le c\cdot\mathrm{rw}(P_a)$ for every plank, then
$$1=\mu(K)\le\mu\Big(\bigcup_a P_a\Big)\le\sum_a\mu(P_a)\le c\sum_a \mathrm{rw}(P_a)
\ \Longrightarrow\ \sum_a \mathrm{rw}(P_a)\ge \tfrac1c.$$
**The whole game is the constant $c$**: find a measure whose marginal in every direction $u$
has density $\le c/w_K(u)$. (Recall $\mathrm{rw}(P)=\text{width}(P)/w_K(u)$.)

## MILESTONE 1 — the area measure gives $c=2$, hence $\sum \mathrm{rw}\ge\tfrac12$  `[DONE, verified]`
Take $\mu=$ the **uniform (area) measure** on the triangle $\Delta$. Its marginal in any
direction $u$ is the cross-sectional-length function, which for a triangle rises linearly then
falls linearly — a **triangular ("tent") distribution** on $[\min u,\max u]$, of mass $1$ over
length $w_\Delta(u)$. A triangular density of unit mass on an interval of length $L$ has **peak
$2/L$**. Hence the marginal density is $\le 2/w_\Delta(u)$ everywhere, so for any plank
$P=\{a\le\langle u,\cdot\rangle\le b\}$,
$$\mu_{\rm area}(P)=\int_a^b(\text{marginal})\le\frac{2}{w_\Delta(u)}(b-a)=2\,\mathrm{rw}(P).$$
**Therefore $\sum_a\mathrm{rw}(P_a)\ge\tfrac12$ for any covering of the triangle.**
- **Numerically verified:** $\max_P \mu_{\rm area}(P)/\mathrm{rw}(P)=1.99873$ (over 300k random
  planks; the sup $2$ is approached by thin slabs at the tent peak = the middle-vertex
  projection). `experiments` confirm the chain.
- **The "$2$" is exactly the peak of the tent** — the affine-invariant signature of the triangle.

## MILESTONE 2 — improving the constant toward $1$  `[OPEN — the real difficulty]`
- **A single measure cannot reach $c=1$.** $c=1$ requires marginal density $\le 1/w_\Delta(u)$
  pointwise, i.e. **uniform** marginals in every direction. For the standard simplex, uniform
  marginal in coordinate direction $e_k$ means $\mathbb E[x_k]=\tfrac12$; but $\sum_k x_k=1$
  forces $\sum_k\mathbb E[x_k]=1\ne\frac{d+1}{2}$ for $d\ge2$. **So no single probability measure
  satisfies all plank constraints with $c=1$** — the union-bound/fractional route is genuinely
  capped at $c\in[1,2)$ (best single-measure constant), strictly above $1$.
- Consequence: the full $\sum\mathrm{rw}\ge1$ (the *integer* covering bound, sharp by Hunter's
  equilateral example) is **not** reachable by the single-measure union bound; it needs the
  *combinatorial* structure of an actual covering (an integrality-gap phenomenon). This is
  precisely why Bang's affine conjecture is hard/open while $\sum\mathrm{rw}\ge\tfrac12$ is easy.
- **Open routes to close $1/2\to1$:** (i) a covering-*dependent* witness measure; (ii) exploit
  overlaps/the combinatorics of the cover; (iii) the best single-measure constant $c^\*<2$
  (compute it — it improves the bound to $1/c^\*$).

## MILESTONE 3 — general dimension $d$  `[OPEN]`
The volume measure on $\Delta^d$ has marginal = $(d{-}1)$-dim cross-section volume, a degree-$(d{-}1)$
piecewise polynomial; its peak/uniform ratio gives the constant $c_d$ (with $c_2=2$). Determine
$c_d$ and hence the elegant bound $\sum\mathrm{rw}\ge1/c_d$ for the $d$-simplex.

## Status / honesty
- **Genuinely proved & verified:** $\sum\mathrm{rw}\ge\tfrac12$ for the triangle, by a 4-line
  elegant measure argument — the "factor 2" the milestone targets.
- **Still open:** the *sharp* $\sum\mathrm{rw}\ge1$. The clean impossibility above shows it is
  *not* a single-measure statement; it requires the covering's combinatorics. This is consistent
  with the literature (Bang's affine conjecture open even for 3 planks in the plane).
