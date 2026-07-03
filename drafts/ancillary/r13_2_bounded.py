#!/usr/bin/env python3
"""
r13_2_bounded.py -- R13-2 (bounded carryover): (a) fine upper bounds near the
facet triple via ADAPTED symmetric loops (is D(tilt) < 3/2? -> local-max
evidence); (b) one denser attempt at the exact sandwich D (dual with more
knots vs piecewise skeleton).

(a) The tilt triple V_eps = [(1,e,0),(0,1,e),(e,0,1)] is invariant under the
vertex rotation A->B->C->A.  Measures: uniform mass 1/3 on each side of the
loop V0 -> V1 -> V2 with V1 = rho(V0), V2 = rho^2(V0), V0 = (x,y,1-x-y).
By symmetry all three marginals coincide; the max marginal density is exact
for rational (x,y).  Float search guides; certification is exact ->
CERTIFIED upper bounds on D(tilt).

(b) dual_bound with q=75 adapted knots (lower bound) and skeleton_pw_UB with
q=60 (upper bound) on the sandwich.
"""

import random
from fractions import Fraction as F

from scipy.optimize import minimize
import numpy as np

from supD_dual_hunt import (cyclic, tilted_facets, dual_bound, moment_bound,
                            skeleton_pw_UB, skeleton_uniform_UB)


def rho(p):
    x, y, z = p
    return (z, x, y)


def loop_max_density(V, P0):
    """Exact max marginal density of the symmetric loop measure through
    P0, rho(P0), rho^2(P0) for direction V[0] (all directions equal by
    symmetry).  P0 exact rationals; returns None if degenerate."""
    pts = [P0, rho(P0), rho(rho(P0))]
    def u(p):
        return sum(V[0][j]*p[j] for j in range(3))
    segs = []
    for k in range(3):
        a, b = u(pts[k]), u(pts[(k+1) % 3])
        if a == b:
            return None
        lo, hi = min(a, b), max(a, b)
        segs.append((lo, hi, F(1, 3)/(hi-lo)))
    cuts = sorted({c for lo, hi, _ in segs for c in (lo, hi)})
    dens = F(0)
    for lo, hi in zip(cuts[:-1], cuts[1:]):
        d = sum(w for a, b, w in segs if a <= lo and hi <= b)
        dens = max(dens, d)
    return dens


def adapted_loop_UB(eps, seed=1):
    V = tilted_facets(eps, eps, eps)
    Vf = [[float(x) for x in v] for v in V]
    def obj(xy):
        x, y = xy
        z = 1.0-x-y
        if min(x, y, z) < 1e-6:
            return 10.0
        P0 = (F(x).limit_denominator(10**6), F(y).limit_denominator(10**6),
              None)
        P0 = (P0[0], P0[1], 1-P0[0]-P0[1])
        d = loop_max_density(V, P0)
        return float(d) if d is not None else 10.0
    best = None
    rng = random.Random(seed)
    starts = [(0.0001, 1/3), (0.05, 0.35), (0.1, 0.3)] + \
             [(rng.random()*0.4, 0.2+rng.random()*0.3) for _ in range(6)]
    for x0 in starts:
        r = minimize(obj, x0, method='Nelder-Mead',
                     options=dict(maxiter=600, fatol=1e-12))
        if best is None or r.fun < best[0]:
            best = (r.fun, r.x)
    # exactify
    x = F(float(best[1][0])).limit_denominator(2000)
    y = F(float(best[1][1])).limit_denominator(2000)
    x = max(F(0), min(F(1), x)); y = max(F(0), min(F(1), y))
    P0 = (x, y, 1-x-y)
    d = loop_max_density(V, P0)
    return d, P0


if __name__ == '__main__':
    print("=== (a) adapted symmetric loops near the facets ===")
    print("  facets (eps=0) sanity: loop through (0,1/3,2/3):",
          loop_max_density(tilted_facets(0, 0, 0),
                           (F(0), F(1, 3), F(2, 3))), "(expect 3/2)")
    for eps in (F(1, 10), F(1, 20), F(1, 50)):
        ub, P0 = adapted_loop_UB(eps)
        mb = moment_bound(tilted_facets(eps, eps, eps))
        flag = "  ** UB < 3/2 **" if ub < F(3, 2) else ""
        print(f"  tilt eps={eps}: certified loop UB = {ub} = {float(ub):.6f}"
              f" at P0={P0}; moment LB = {float(mb):.6f}{flag}")

    print("=== (b) sandwich: denser dual LB vs piecewise skeleton UB ===")
    Vs = cyclic(F(13, 25), F(1, 2), F(1, 2))
    extra = (F(1, 225), F(2, 225), F(3, 225), F(224, 225), F(223, 225),
             F(222, 225), F(13, 25), F(12, 25), F(1, 50), F(49, 50))
    lb, _ = dual_bound(Vs, 75, extra)
    print(f"  dual q=75+adapted: certified LB = {float(lb):.7f} "
          f"(moment 225/224 = {float(F(225,224)):.7f})")
    ubu = skeleton_uniform_UB(Vs)
    ubp = skeleton_pw_UB(Vs, 60)
    print(f"  skeleton uniform UB = {ubu} = {float(ubu):.7f}; "
          f"piecewise (q=60) UB = "
          f"{float(ubp):.7f}" if ubp else "  piecewise UB failed")
    print("done")
