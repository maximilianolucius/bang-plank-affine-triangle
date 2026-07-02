# Theorem — 3 facet planks + 1 tilted (symmetric subcase)
> Date: 2026-06-29. **Status: PROVED** (self-contained).

## Statement

Let \(\Delta=\{x\in\mathbb R^3: x_i\ge0,\ \sum_i x_i=1\}\). Fix \(t\in(0,1)\) and \(r\in(0,\tfrac13]\).

**Facet planks:** \(P_i=\{x\in\Delta: x_i\in[0,r]\}\), \(i=1,2,3\).  
**Tilted plank:** \(P_4=\{x\in\Delta: f_4(x)\in I_4\}\) where \(f_4(x)=t x_2+x_3\) and \(I_4=[c,c+r_4]\) is an interval of length \(r_4\).

If \(P_1\cup P_2\cup P_3\cup P_4\supseteq\Delta\), then
\[
r_1+r_2+r_3+r_4 = 3r+r_4 \ \ge\ 1.
\]

This is a **sharp partial case** of Bang's affine plank conjecture for the triangle (the subfamily “3 coordinate slabs anchored at 0 + one tilted direction \((0,t,1)\)”).

---

## Proof

### Step 1 — Partition of \(\Delta\) [PROVED]

Define
\[
R_f=\{x\in\Delta:\ x_i>r\ \forall i=1,2,3\}.
\]
Then \(\Delta\) is the disjoint union of \(R_f\) and \(\Delta\setminus R_f\), and
\[
\Delta\setminus R_f = \{x\in\Delta:\ \exists i,\ x_i\le r\} = \bigcup_{i=1}^3 \{x\in\Delta: x_i\le r\}.
\]
Each facet plank \(P_i\) equals \(\{x\in\Delta: x_i\le r\}\), so the three facets cover \(\Delta\setminus R_f\) **exactly**.

Therefore a point in \(R_f\) is not covered by any facet plank and must lie in \(P_4\):
\[
R_f\subseteq \{x\in\Delta: f_4(x)\in I_4\}.
\]

### Step 2 — Span identity on \(R_f\) [PROVED]

The set \(R_f\) is a (small) triangle with vertices
\[
V_1=(1-2r,r,r),\quad V_2=(r,1-2r,r),\quad V_3=(r,r,1-2r)
\]
(feasible since \(r\le\tfrac13\)).

Since \(f_4\) is affine, \(\max_{R_f} f_4-\min_{R_f} f_4\) occurs at vertices. Compute:
\[
f_4(V_1)=r(1+t),\quad f_4(V_2)=t+r(1-2t),\quad f_4(V_3)=1-r(2-t).
\]
**Claim:** \(f_4(V_1)\le f_4(V_2)\le f_4(V_3)\).

*Proof of ordering.* For \(r\le\tfrac12\): \(f_4(V_1)-f_4(V_2)=t(2r-1)\le0\).  
And \(f_4(V_3)-f_4(V_1)=1-3r\) (independent of \(t\)), which is \(\ge0\) for \(r\le\tfrac13\).  
Also \(f_4(V_3)-f_4(V_2)=1-3r+t(3r-1)\ge1-3r\ge0\) when \(r\le\tfrac13\). ∎

Hence
\[
\max_{x\in R_f} f_4(x)-\min_{x\in R_f} f_4(x)
= f_4(V_3)-f_4(V_1)=(1-r(2-t))-r(1+t)=1-3r.
\]

### Step 3 — Width of the tilted plank [PROVED]

On \(\Delta\), \(f_4(e_1)=0\) and \(f_4(e_3)=1\), so after normalization \(w_\Delta(f_4)=1\) and the relative width of \(P_4\) equals \(r_4\).

If \(R_f\subseteq\{f_4\in I_4\}\), then \(r_4\ge \max_{R_f}f_4-\min_{R_f}f_4=1-3r\).

### Step 4 — Conclusion [PROVED]

\[
3r+r_4 \ge 3r+(1-3r)=1.\qquad\blacksquare
\]

---

## Remarks

1. **Independence of \(t\).** The span \(1-3r\) does not depend on \(t\in(0,1)\); only the optimal center \(c\) of \(I_4\) does.

2. **Sharpness.** At \(r=\tfrac13\), \(R_f=\emptyset\) and the facet bound alone gives \(3r=1\) (facet-parallel theorem). For \(r<\tfrac13\), tight examples approach \(r_4=1-3r\).

3. **What this does NOT prove.** The general subfamily with arbitrary facet intervals \(I_i=[a_i,a_i+r_i]\) and arbitrary \(t\) remains open. Numerically, \(r_1+r_2+r_3+\mathrm{span}(f_4(R_f))\) can be **<1** even when \(R_f\neq\emptyset\), but covering the full triangle still appears to require \(\sum\ge1\) — the extra cost comes from covering \(\Delta\setminus R_f\) with shifted facet slabs, not from \(R_f\) alone.

4. **Relation to m≥4 general case.** Four unrelated tilted directions are not covered by this theorem.
