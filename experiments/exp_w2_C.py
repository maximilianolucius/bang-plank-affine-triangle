r"""
EXP-C: escape-cell coverage certifier for m=3 planks on Delta (common-edge family),
with Farkas duals -> proof template.

Planks i=1..3: form g_i (vertex values vA,vB,vC) and interval [l_i,h_i].
A point x is UNCOVERED iff for every i, g_i(x)<l_i or g_i(x)>h_i, i.e. x lies in some
escape cell R_sigma, sigma in {-,+}^3:
    sigma_i=-: g_i(x) <= l_i ;  sigma_i=+: g_i(x) >= h_i.
Coverage <=> every R_sigma is empty.

Per-cell margin LP:  maximize t  s.t.  x in Delta  and
    sigma_i=-:  g_i(x) + t <= l_i
    sigma_i=+: -g_i(x) + t <= -h_i
t* < 0  => cell empty with margin |t*| (covered).  t*=0 => binding (tight).
The LP dual at the optimum is a Farkas certificate: nonneg multipliers on
{Delta edges, plank faces} that sum to a contradiction -> templates Sum r >= 1.
"""
import numpy as np
from scipy.optimize import linprog
from itertools import product
from fractions import Fraction as Q


def form(vA, vB, vC):
    # g(y,z) = vA + (vB-vA) y + (vC-vA) z  -> (cy,cz,const)
    return (vB - vA, vC - vA, vA)


def cell_margin(planks, sigma):
    """planks: list of (g=(cy,cz,c0), l, h). Returns (tstar, x, duals, names)."""
    # vars: y, z, t  ; maximize t = minimize -t
    A_ub = []; b_ub = []; names = []
    # Delta: -y<=0 ; -z<=0 ; y+z<=1
    A_ub += [[-1, 0, 0], [0, -1, 0], [1, 1, 0]]; b_ub += [0, 0, 1]
    names += ["y>=0", "z>=0", "y+z<=1"]
    for (g, l, h), si in zip(planks, sigma):
        cy, cz, c0 = g
        if si == '-':   # cy*y+cz*z+c0 + t <= l
            A_ub.append([cy, cz, 1]); b_ub.append(l - c0); names.append(f"g{'-'} <= l")
        else:           # -(cy*y+cz*z+c0) + t <= -h
            A_ub.append([-cy, -cz, 1]); b_ub.append(-(h - c0)); names.append(f"g{'+'} >= h")
    c = [0, 0, -1]  # minimize -t
    res = linprog(c, A_ub=A_ub, b_ub=b_ub, bounds=[(None, None)] * 3, method="highs")
    if not res.success:
        return None
    tstar = -res.fun
    duals = -res.ineqlin.marginals  # >=0 multipliers
    return tstar, res.x, duals, names, A_ub, b_ub


def coverage_report(planks, tag):
    print(f"\n### {tag}")
    R = sum(h - l for (_, l, h) in planks)
    print(f"  Sum r = {R:.6f}")
    binding = []
    maxt = -9
    for sigma in product('-+', repeat=3):
        out = cell_margin(planks, sigma)
        if out is None:
            print("   LP fail", sigma); continue
        tstar, x, duals, names, A, b = out
        maxt = max(maxt, tstar)
        if tstar > 1e-7:
            print(f"  sigma={''.join(sigma)}: NONEMPTY t*={tstar:+.4f} -> NOT covered at x={x[:2]}")
        elif tstar > -1e-7:  # binding (t*~0)
            act = [names[i] for i in range(len(names)) if abs(A[i][0]*x[0]+A[i][1]*x[1]+A[i][2]*x[2]-b[i]) < 1e-7]
            binding.append((''.join(sigma), x[:2], duals))
    covered = maxt <= 1e-7
    print(f"  COVERED={covered} (max t*={maxt:+.4f}); binding (t*=0) cells: "
          f"{[b[0] for b in binding]}")
    for sg, x, duals in binding:
        nz = [(i, round(float(d), 4)) for i, d in enumerate(duals) if d > 1e-7]
        print(f"    cell {sg} @x=({x[0]:.3f},{x[1]:.3f}) dual nz (constraint idx:mult): {nz}")
    return covered, binding


if __name__ == "__main__":
    # (i) Hunter all-facet tight: P1=x_B<=t1, P2=x_A<=t2, Q=x_C<=1-t1-t2
    t1, t2 = 1/3, 1/3
    P = [(form(0, 1, 0), 0.0, t1), (form(1, 0, 0), 0.0, t2), (form(0, 0, 1), 0.0, 1 - t1 - t2)]
    coverage_report(P, f"Hunter all-facet tight t1={t1:.3f} t2={t2:.3f}")

    # (ii) common-edge OPP facet-locus tight (a1=0 facet, a2=1/3, s=1/3): need tight placement
    #      g1=(0,1,0)=x_B, g2=(1,0,1/3), f=(0,1/3,1). Use a covering placement and check.
    a2, s = 1/3, 1/3
    # choose planks that cover: P1 = {g1 in [0, .35]}, P2={g2 in [0,.35]}, Q={f in [0, .4]}
    P = [(form(0, 1, 0), 0.0, 0.34), (form(1, 0, a2), 0.0, 0.34), (form(0, s, 1), 0.0, 0.34)]
    coverage_report(P, f"common-edge OPP a1=0,a2={a2:.2f},s={s:.2f} (placement test)")

    # (iii) slightly sub-1 attempt (should NOT cover): shrink intervals
    P = [(form(0, 1, 0), 0.0, 0.30), (form(1, 0, 0), 0.0, 0.30), (form(0, 0, 1), 0.0, 0.30)]
    coverage_report(P, "all-facet Sum r=0.90 (<1) -> must NOT cover")
