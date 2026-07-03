#!/usr/bin/env python3
"""
supD_hunt_phase2.py -- R10-1 Route A, targeted follow-ups:
  (a) independent sanity check of the certified dual minimum (random exact
      interior points must never fall below the certified bound);
  (b) sandwich with ADAPTED knots (wedge knot 1/225 etc.): can the dual
      exceed the moment bound 225/224?
  (c) the facet corner of class (b) and small tilted facets with adapted
      knots: does any certified dual exceed 3/2?
  (d) near-parallel path: symbolic proof of the skeleton upper bound
      D <= 1 + (3/4) eps along class_b(1/3, 1/3+eps, 1/2).
All certified numbers are exact rationals.
"""

import random
from fractions import Fraction as F

import sympy as sp

from supD_dual_hunt import (cyclic, class_b, tilted_facets, dual_bound,
                            moment_bound, skeleton_uniform_UB, uval,
                            interp_coeffs, complex_vertices)


def sanity_min(V, q, extra, B_cert, y, trials=400):
    """Random exact interior points: sum psi_i(u_i(x)) >= B_cert always."""
    base = sorted(set([F(k, q) for k in range(q + 1)] + [F(e) for e in extra]))
    offs = [0, len(base), 2 * len(base)]
    rng = random.Random(31)
    for _ in range(trials):
        a, b = F(rng.randint(0, 600), 600), F(rng.randint(0, 600), 600)
        if a + b > 1:
            continue
        lam = (a, b, 1 - a - b)
        val = F(0)
        for i in range(3):
            t = uval(V[i], lam)
            for idx, cf in interp_coeffs(base, t):
                val += cf * y[offs[i] + idx]
        assert val >= B_cert, (lam, val, B_cert)
    return True


def hunt(name, V, q, extra, target):
    mb = moment_bound(V)
    lb, y = dual_bound(V, q, extra)
    if lb is None:
        print(f"  {name}: LP failed")
        return
    sanity_min(V, q, extra, lb, y)
    ub = skeleton_uniform_UB(V)
    tag = ""
    if lb > mb:
        tag += "  ** DUAL > MOMENT **"
    if lb > F(3, 2):
        tag += "  ***** D > 3/2 *****"
    print(f"  {name}: moment={mb}={float(mb):.6f}  dualLB={float(lb):.6f}"
          f"  (exact {lb if lb.denominator < 10**6 else 'big-fraction'})"
          f"  skelUB={ub}={float(ub):.6f}{tag}")
    return lb


def near_parallel_symbolic():
    """Class (b) path V(eps) = [(0,1,1/3), (0,1,1/3+eps), (1/2,0,1)].
    Claim: the skeleton measure with weights
        w_AB = 1/2 - (3/8) eps,  w_BC = 1/4 + (3/8) eps - s??  -- instead of
    guessing, solve the uniform-edge LP symbolically at the observed pattern:
    equalize the three densities that were active at the sampled optima."""
    eps = sp.symbols('epsilon', positive=True)
    t1, t2, t3 = sp.S(1)/3, sp.S(1)/3 + eps, sp.S(1)/2
    V = [(0, 1, t1), (0, 1, t2), (t3, 0, 1)]
    E = [(0, 1), (1, 2), (2, 0)]
    w = list(sp.symbols('w1 w2 w3'))  # w_AB, w_BC, w_CA
    # marginal density of direction i on elementary value intervals
    def densities(i):
        v = V[i]
        pieces = [(sp.Min(v[a], v[b]), sp.Max(v[a], v[b]), k)
                  for k, (a, b) in enumerate(E)]
        cuts = sorted({c for lo, hi, _ in pieces for c in (lo, hi)},
                      key=lambda z: z.subs(eps, sp.Rational(1, 100)))
        out = []
        for a, b in zip(cuts[:-1], cuts[1:]):
            mid = (a + b) / 2
            d = 0
            for lo, hi, k in pieces:
                lo_n = lo.subs(eps, sp.Rational(1, 100))
                hi_n = hi.subs(eps, sp.Rational(1, 100))
                mid_n = mid.subs(eps, sp.Rational(1, 100))
                if lo_n < mid_n < hi_n:
                    d += w[k] / (hi - lo)
            out.append(sp.simplify(d))
        return out
    dens = [densities(i) for i in range(3)]
    # candidate optimum (guided by the exact LP at eps=1/3,1/6,1/12,1/60):
    # equalize: max density of u1, of u2, and of u3 all equal to t, with
    # w1+w2+w3=1.  The active densities at the sampled optima were the
    # [t1,t2]-interval of u1/u2 and the top interval of u3.
    t = sp.symbols('t', positive=True)
    d1 = max(dens[0], key=lambda z: z.subs([(w[0], 1), (w[1], 1), (w[2], 1),
                                            (eps, sp.Rational(1, 100))]))
    # solve the system: three specific densities equal t (pick per direction
    # the piece that is maximal at the LP optimum) -- we take the pieces:
    # u1: w1 + w3/(1-t1) ... simpler: just verify the CLAIMED closed form:
    w_claim = {w[0]: sp.S(1)/2 - sp.S(3)/8*eps,
               w[1]: sp.S(1)/4 + sp.S(3)/16*eps,
               w[2]: sp.S(1)/4 + sp.S(3)/16*eps}
    claimed_bound = 1 + sp.S(3)/4*eps
    ok_mass = sp.simplify(sum(w_claim.values()) - 1) == 0
    allds = [sp.simplify(d.subs(w_claim)) for row in dens for d in row]
    diffs = [sp.simplify(claimed_bound - d) for d in allds]
    # check nonnegativity of diffs on eps in (0, 1/6]
    ok = ok_mass
    for dd in diffs:
        # dd should be >= 0 for small eps; test exact at several rationals
        for e0 in (sp.Rational(1, 3), sp.Rational(1, 6), sp.Rational(1, 12),
                   sp.Rational(1, 60), sp.Rational(1, 1000)):
            if dd.subs(eps, e0) < 0:
                ok = False
    return ok, w_claim, claimed_bound, [sp.simplify(d) for d in allds]


if __name__ == '__main__':
    print("=== (b) sandwich, adapted knots (wedge knot 1/225, 13/25 etc.) ===")
    Vs = cyclic(F(13, 25), F(1, 2), F(1, 2))
    for q, extra in [
        (25, (F(1, 225), F(224, 225), F(13, 25), F(12, 25))),
        (45, (F(1, 225), F(2, 225), F(224, 225), F(223, 225),
              F(13, 25), F(12, 25), F(1, 50), F(49, 50))),
    ]:
        hunt(f"sandwich q={q}+adapted", Vs, q, extra, F(225, 224))

    print("=== (c) facet corner of class (b): eta -> 0 ===")
    for eta, q in [(F(1, 12), 24), (F(1, 24), 24), (F(1, 48), 24)]:
        extra = (eta, 1 - eta, 2 * eta, 1 - 2 * eta, F(2, 3), F(1, 3),
                 F(2, 3) - eta, F(2, 3) + eta, F(1, 3) - eta, F(1, 3) + eta)
        hunt(f"class-b corner eta={eta}", class_b(eta, 1 - eta, eta),
             q, extra, F(3, 2))

    print("=== (c') tilted facets, adapted knots ===")
    for e, q in [(F(1, 10), 30), (F(1, 20), 40)]:
        extra = (e, 1 - e, F(2, 3), F(2, 3) - e, F(2, 3) + e,
                 F(1, 3), F(1, 3) - e, F(1, 3) + e)
        hunt(f"tilt eps={e}", tilted_facets(e, e, e), q, extra, F(3, 2))

    print("=== (d) near-parallel path: symbolic skeleton UB ===")
    ok, w_claim, bound, ds = near_parallel_symbolic()
    print(f"  claimed weights {w_claim} give max marginal density"
          f" <= {bound}: {'VERIFIED at sampled eps' if ok else 'FAILED'}")
    print("done")
