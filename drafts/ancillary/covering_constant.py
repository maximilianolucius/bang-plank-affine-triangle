#!/usr/bin/env python3
"""
covering_constant.py -- R12-C1: the covering-constant program C(u).

C_K(u)  = inf{sum rw : coverings of K by planks parallel to u_1..u_n}
C_3(u)  = same with exactly one plank per direction (n=3 on the triangle).
Trivially 1/D_K(u) <= C_K(u) <= C_3(u)... no: C_K <= C_3 <= 1 (one full plank
covers).  Bang's affine conjecture for these directions <=> C_K(u) = 1.

This script (all exact unless labelled float-guided):
 1. EXACT coverage oracle for one-plank-per-direction configurations
    (l_i, h_i): a point is uncovered iff it lies in one of the 8 open sign
    cells; cell nonemptiness inside Delta is an exact Chebyshev LP
    (vertex enumeration, fractions).  Edge coverage double-checked by exact
    1-D interval arithmetic.
 2. The canonical MMM covering for cyclic tau (Prop A.1 solution [lam,rho]):
    exact value  Sigma rw = Sigma(rho-lam) =: 1 + E(tau), the margin check
    (cells empty), and a symbolic formula/factorization of the excess E(tau).
 3. Edge-coverage LP lower bound  LB_edge(u) = min{Sigma r : per-edge trace
    lengths can reach 1}  (necessary conditions; exact tiny LP).
 4. Float-guided hunt: minimize Sigma r over (l,h) with coverage; candidates
    exactified (rationalize + verify with the exact oracle) -> certified
    UPPER bounds for C_3.  ANTI-SENSATION PROTOCOL: any certified covering
    with Sigma r < 1 would refute Bang's affine conjecture -- it would be
    triple-checked (oracle + independent edge check + fresh recomputation)
    and reported as 'requires independent audit', never as a claim.
"""

import itertools
import random
from fractions import Fraction as F

import numpy as np
from scipy.optimize import linprog, minimize
import sympy as sp

from supD_dual_hunt import solve3, uval, cyclic, class_b, moment_bound

CORNERS = [(F(1), F(0), F(0)), (F(0), F(1), F(0)), (F(0), F(0), F(1))]
EDGES = [(0, 1), (1, 2), (2, 0)]


# ---------------------------------------------------------------- oracle
def cell_depth_exact(V, lh, sigma):
    """Exact Chebyshev depth of sign cell sigma inside Delta:
    max t s.t. lam in Delta and (lo: u_i <= l_i - t) / (hi: u_i >= h_i + t).
    Returns the exact max t (cell has an uncovered point iff t > 0)."""
    cons = []  # a.(l1,l2,t) <= b
    for i in range(3):
        v = V[i]
        a1, a2, c0 = v[0]-v[2], v[1]-v[2], v[2]
        li, hi = lh[i]
        if sigma[i] == 0:   # u_i + t <= l_i
            cons.append(([a1, a2, F(1)], li - c0))
        else:               # -u_i + t <= -h_i
            cons.append(([-a1, -a2, F(1)], c0 - hi))
    cons += [([F(-1), F(0), F(0)], F(0)), ([F(0), F(-1), F(0)], F(0)),
             ([F(1), F(1), F(0)], F(1))]
    best = None
    for idx in itertools.combinations(range(len(cons)), 3):
        M = [list(cons[k][0]) for k in idx]
        x = solve3(M, [cons[k][1] for k in idx])
        if x is None:
            continue
        if all(sum(a*xx for a, xx in zip(c[0], x)) <= c[1] for c in cons):
            if best is None or x[2] > best:
                best = x[2]
    return best  # None = infeasible (empty even at t -> -inf impossible here)


def covers_exact(V, lh):
    """True iff the three planks {u_i in [l_i,h_i]} cover Delta (exact)."""
    for sigma in itertools.product((0, 1), repeat=3):
        d = cell_depth_exact(V, lh, sigma)
        if d is not None and d > 0:
            return False, (sigma, d)
    return True, None


def edges_covered_exact(V, lh):
    """Independent exact check: traces cover each closed edge."""
    for (a, b) in EDGES:
        segs = []
        for i in range(3):
            va, vb = V[i][a], V[i][b]
            li, hi = lh[i]
            if va == vb:
                if li <= va <= hi:
                    segs.append((F(0), F(1)))
                continue
            t0 = (li - va)/(vb - va)
            t1 = (hi - va)/(vb - va)
            lo, hi2 = min(t0, t1), max(t0, t1)
            lo, hi2 = max(lo, F(0)), min(hi2, F(1))
            if lo <= hi2:
                segs.append((lo, hi2))
        segs.sort()
        reach = F(0)
        for lo, hi2 in segs:
            if lo > reach:
                return False, (a, b, reach)
            reach = max(reach, hi2)
        if reach < 1:
            return False, (a, b, reach)
    return True, None


# ------------------------------------------------- MMM canonical covering
def mmm_intervals(tau):
    t1, t2, t3 = [F(t) for t in tau]
    P = t1*t2*t3
    Q = (1-t1)*(1-t2)*(1-t3)
    tt = [t1, t2, t3]
    lam = [tt[i]*(1 - tt[(i+1) % 3]*(1 - tt[(i+2) % 3]))/(1+P)
           for i in range(3)]
    rho = [(1 - tt[(i+2) % 3]*(1 - tt[i]))/(1+Q) for i in range(3)]
    return list(zip(lam, rho))


def mmm_excess_symbolic():
    t1, t2, t3 = sp.symbols('t1 t2 t3', positive=True)
    P = t1*t2*t3
    Q = (1-t1)*(1-t2)*(1-t3)
    tt = [t1, t2, t3]
    lam = [tt[i]*(1 - tt[(i+1) % 3]*(1-tt[(i+2) % 3]))/(1+P) for i in range(3)]
    rho = [(1 - tt[(i+2) % 3]*(1-tt[i]))/(1+Q) for i in range(3)]
    E = sp.factor(sp.simplify(sum(rho) - sum(lam) - 1))
    return E


# ------------------------------------------------- edge-coverage LP bound
def edge_lp_lower(V):
    """min Sigma r s.t. for each edge, the maximal possible total trace
    length reaches 1: sum_i r_i/|slope_i(edge)| >= 1 (slope in the edge
    parameter; direction constant on the edge => its plank can cover the
    whole edge only if the edge value is inside; treat as coefficient inf ->
    skip; none of our triples has constant edges).  Exact tiny LP by vertex
    enumeration on (r1,r2,r3)."""
    cons = []
    for (a, b) in EDGES:
        row = []
        for i in range(3):
            va, vb = V[i][a], V[i][b]
            assert va != vb, "constant edge: handle separately"
            row.append(1/abs(vb - va))
        cons.append((row, F(1)))     # row . r >= 1
    best = None
    for idx in itertools.combinations(range(3), 3):
        M = [list(cons[k][0]) for k in idx]
        x = solve3(M, [cons[k][1] for k in idx])
        if x is None:
            continue
        if all(xx >= 0 for xx in x) and \
           all(sum(a*xx for a, xx in zip(c[0], x)) >= c[1] for c in cons):
            v = sum(x)
            if best is None or v < best:
                best = v
    # also vertices with some r_i = 0 (boundary of positivity)
    for zeros in itertools.combinations(range(3), 1):
        for pair in itertools.combinations(range(3), 2):
            M = [list(cons[k][0]) for k in pair]
            zrow = [F(0)]*3
            zrow[zeros[0]] = F(1)
            M.append(zrow)
            x = solve3(M, [cons[pair[0]][1], cons[pair[1]][1], F(0)])
            if x is None:
                continue
            if all(xx >= 0 for xx in x) and \
               all(sum(a*xx for a, xx in zip(c[0], x)) >= c[1] for c in cons):
                v = sum(x)
                if best is None or v < best:
                    best = v
    return best


# ------------------------------------------------- float-guided hunt
_TRIPLES = list(itertools.combinations(range(6), 3))

def uncovered_depth_float(Vf, x):
    """max over 8 cells of the float Chebyshev depth (>=0 clipped).
    Direct vertex enumeration of the 6-constraint LP (no scipy): the
    Chebyshev optimum is at a vertex where 3 constraints are active."""
    worst = 0.0
    for sigma in itertools.product((0, 1), repeat=3):
        A, b = [], []
        for i in range(3):
            a1, a2, c0 = Vf[i][0]-Vf[i][2], Vf[i][1]-Vf[i][2], Vf[i][2]
            li, hi = x[2*i], x[2*i+1]
            if sigma[i] == 0:
                A.append((a1, a2, 1.0)); b.append(li - c0)
            else:
                A.append((-a1, -a2, 1.0)); b.append(c0 - hi)
        A += [(-1.0, 0.0, 0.0), (0.0, -1.0, 0.0), (1.0, 1.0, 0.0)]
        b += [0.0, 0.0, 1.0]
        best = None
        for (p, q, r) in _TRIPLES:
            M = np.array([A[p], A[q], A[r]])
            det = np.linalg.det(M)
            if abs(det) < 1e-13:
                continue
            xx = np.linalg.solve(M, [b[p], b[q], b[r]])
            ok = True
            for k in range(6):
                if A[k][0]*xx[0]+A[k][1]*xx[1]+A[k][2]*xx[2] > b[k]+1e-11:
                    ok = False
                    break
            if ok and (best is None or xx[2] > best):
                best = xx[2]
        if best is not None:
            worst = max(worst, best)
    return worst


def hunt(V, starts=10, seed=5):
    Vf = [[float(x) for x in v] for v in V]
    rng = random.Random(seed)

    def obj(x):
        x = np.clip(x, 0, 1)
        pen = uncovered_depth_float(Vf, x)
        s = sum(max(0.0, x[2*i+1]-x[2*i]) for i in range(3))
        return s + 60.0*pen

    best = None
    inits = [np.array([0, 1, 0, 0, 0, 0], float),
             np.array([0, 1, 0, 1, 0, 1], float)]
    mmmF = None
    try:
        mmmF = [float(z) for pair in mmm_intervals_from_V(V) for z in pair]
        inits.append(np.array(mmmF))
    except Exception:
        pass
    for _ in range(starts):
        inits.append(np.array([rng.random() for _ in range(6)]))
    for x0 in inits:
        r = minimize(obj, x0, method='Nelder-Mead',
                     options=dict(maxiter=1200, fatol=1e-11, xatol=1e-9))
        x = np.clip(r.x, 0, 1)
        if uncovered_depth_float(Vf, x) < 1e-11:
            s = sum(max(0.0, x[2*i+1]-x[2*i]) for i in range(3))
            if best is None or s < best[0]:
                best = (s, x.copy())
    return best


def mmm_intervals_from_V(V):
    # recover tau from a cyclic V (values (t1,0,1),(0,1,t2),(1,t3,0))
    return mmm_intervals((V[0][0], V[1][2], V[2][1]))


def certify_upper(V, x, pad=F(1, 100000)):
    """Rationalize a float candidate, pad outward until the exact oracle
    passes; return exact Sigma r of the certified covering (or None)."""
    for extra in [F(0), pad, 4*pad, 16*pad, 64*pad, 256*pad]:
        lh = []
        for i in range(3):
            li = max(F(0), F(float(x[2*i])).limit_denominator(10**5) - extra)
            hi = min(F(1), F(float(x[2*i+1])).limit_denominator(10**5) + extra)
            if li > hi:
                li = hi
            lh.append((li, hi))
        ok, _ = covers_exact(V, lh)
        if ok:
            ok2, _ = edges_covered_exact(V, lh)
            assert ok2, "oracle/edge check disagree"
            return sum(h-l for l, h in lh), lh
    return None, None


if __name__ == '__main__':
    print("=== symbolic excess of the canonical MMM covering ===")
    E = mmm_excess_symbolic()
    print("  Sigma rw(MMM) - 1 =", E)

    flags = [
        ("sandwich (13/25,1/2,1/2)", cyclic(F(13, 25), F(1, 2), F(1, 2))),
        ("cyclic (5/9,4/5,1/6)", cyclic(F(5, 9), F(4, 5), F(1, 6))),
        ("cyclic near-facet (1/12,1/2,1/2)",
         cyclic(F(1, 12), F(1, 2), F(1, 2))),
    ]
    # symbolic proof pieces for the canonical-covering theorem:
    t1, t2, t3 = sp.symbols('t1 t2 t3', positive=True)
    P = t1*t2*t3
    Q = (1-t1)*(1-t2)*(1-t3)
    # (i) dependency coefficients are positive for ALL cyclic tau:
    #     c_i = (1 - t_{i+1}(1-t_{i+2}))/(1+P) in (0,1)  [each factor < 1]
    # (ii) margins hold for ALL cyclic tau (both strictly positive):
    fac = (1-t1*(1-t2))*(1-t3*(1-t1))*(1-t2*(1-t3))
    m1_claim = fac/(1+P)**2                       # 1 - Sigma c lam
    m2_claim = fac/((1+P)*(1+Q))                  # Sigma c rho - 1
    # (iii) excess: E = (P-Q)^2/((1+P)(1+Q))
    E_claim = (P-Q)**2/((1+P)*(1+Q))
    tt = [t1, t2, t3]
    lam_s = [tt[i]*(1-tt[(i+1) % 3]*(1-tt[(i+2) % 3]))/(1+P) for i in range(3)]
    rho_s = [(1-tt[(i+2) % 3]*(1-tt[i]))/(1+Q) for i in range(3)]
    c_s = [(1-tt[(i+1) % 3]*(1-tt[(i+2) % 3]))/(1+P) for i in range(3)]
    assert sp.simplify(1 - sum(c*l for c, l in zip(c_s, lam_s)) - m1_claim) == 0
    assert sp.simplify(sum(c*r for c, r in zip(c_s, rho_s)) - 1 - m2_claim) == 0
    assert sp.simplify(sum(rho_s) - sum(lam_s) - 1 - E_claim) == 0
    # (iv) delta closed form for cyclic: delta = |P-Q|/(2(2+P+Q))
    Sc = sp.simplify(sum(c_s))
    dc_claim = (P-Q)/(2*(2+P+Q))
    assert sp.simplify((1 - Sc/2)/Sc - dc_claim) == 0
    print("  proof pieces verified: c_i>0, both margins = positive products,")
    print("  excess E = (P-Q)^2/((1+P)(1+Q)), delta = |P-Q|/(2(2+P+Q))  OK")

    for name, V in flags:
        tau = (V[0][0], V[1][2], V[2][1])
        lh = mmm_intervals(tau)
        s = sum(h-l for l, h in lh)
        okc, _ = covers_exact(V, lh)
        oke, _ = edges_covered_exact(V, lh)
        lb_e = edge_lp_lower(V)
        print(f"  {name}: MMM covers={okc} (edges {oke}); "
              f"Sigma rw = {s} = 1 + {s-1}")
        print(f"    certified LBs for C_3: edge-LP {lb_e} = "
              f"{float(lb_e):.6f}; transport needs 1/D_UB "
              f"(e.g. sandwich: D <= 112/111 => C_3 >= 111/112)")

    print("=== float-guided hunt for cheaper coverings (exactified) ===")
    for name, V in flags:
        got = hunt(V)
        if got is None:
            print(f"  {name}: no covering found by float hunt (!?)")
            continue
        s_float, x = got
        s_cert, lh = certify_upper(V, x)
        print(f"  {name}: float best Sigma r = {s_float:.8f}; certified "
              f"covering Sigma r = {s_cert} = {float(s_cert):.8f}")
        if s_cert is not None and s_cert < 1:
            print("  *** Sigma r < 1: ANTI-SENSATION PROTOCOL ***")
            print("  *** requires triple verification + independent audit; "
                  "do NOT report as a result ***")
    print("done")
