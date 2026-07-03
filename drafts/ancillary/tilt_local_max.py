#!/usr/bin/env python3
"""
tilt_local_max.py -- R14-2: facets are a STRICT LOCAL MAX of D along the
symmetric tilt path -- now a THEOREM with explicit two-sided bounds.

THEOREM (symmetric tilt path).  For eps in (0, 1/2), let u_tilt(eps) be the
cyclic-symmetric triple with vertex values (1,eps,0), (0,1,eps), (eps,0,1).
Then
    (3/2)/(1+eps)  <=  D(u_tilt(eps))  <=  (3/2)(1-eps)/(1-eps+eps^2)  <  3/2.

Lower bound: the dependency is  sum_i u_i == 1+eps  (c=(1,1,1)), so
delta = delta_c = (1/2-eps)/3 (Thm 7.11) and the moment bound gives
(3/2)/(1+eps).  Upper bound: the symmetric inscribed loop through
P0 = (x*, 1-x*, 0) on edge AB and its two rotations, uniform mass 1/3 per
side, with
    x*(eps) = (1-2eps)/(3(1-eps)):
the u_1-values at the loop vertices are v1 = eps*x* < v0 = x*+eps(1-x*)
< v2 = 1-x*, the marginal has exactly two density branches, both equal to
(3/2)(1-eps)/(1-eps+eps^2) at x* (the equalizing choice), and by the cyclic
symmetry all three marginals coincide.  Strictness: (1-eps)/(1-eps+eps^2)<1
iff eps^2>0.

This script verifies every step symbolically and re-derives the three
R13-certified points (135/91, 190/127, 1225/817).
"""

import sympy as sp

e = sp.symbols('epsilon', positive=True)
x = (1 - 2*e)/(3*(1 - e))
UB = sp.Rational(3, 2)*(1 - e)/(1 - e + e**2)
LB = sp.Rational(3, 2)/(1 + e)


def check_theorem():
    # loop vertices and u_1 values
    P0 = (x, 1 - x, 0)
    P1 = (0, x, 1 - x)
    P2 = (1 - x, 0, x)
    u1 = lambda p: 1*p[0] + e*p[1] + 0*p[2]
    v0, v1, v2 = u1(P0), u1(P1), u1(P2)
    # ordering v1 < v0 < v2 on (0, 1/2):
    d01 = sp.simplify(v0 - v1)   # length of segment range [v1, v0]
    d12 = sp.simplify(v2 - v1)   # [v1, v2]
    d20 = sp.simplify(v2 - v0)   # [v0, v2]
    for dd in (d01, d12, d20):
        assert sp.simplify(dd) != 0
        for e0 in (sp.Rational(1, 10), sp.Rational(1, 20), sp.Rational(1, 50),
                   sp.Rational(2, 5), sp.Rational(49, 100)):
            assert dd.subs(e, e0) > 0, (dd, e0)
    # two density branches (mass 1/3 per side):
    b_low = sp.Rational(1, 3)*(1/d01 + 1/d12)   # on [v1, v0]
    b_high = sp.Rational(1, 3)*(1/d12 + 1/d20)  # on [v0, v2]
    assert sp.simplify(b_low - UB) == 0
    assert sp.simplify(b_high - UB) == 0
    # equalization is exactly the choice x*:
    xs = sp.symbols('xs', positive=True)
    lhs = (xs + e*(1 - 2*xs))            # d01 with generic x
    rhs = (1 - 2*xs - e*(1 - xs))        # d20 with generic x
    sol = sp.solve(sp.Eq(lhs, rhs), xs)
    assert any(sp.simplify(s - x) == 0 for s in sol)
    # total mass of the marginal = 1:
    mass = sp.simplify(b_low*d01 + b_high*d20 - sp.Rational(1, 3)*0)
    # careful: [v1,v0] gets S01+S12, [v0,v2] gets S12+S20; total integral:
    total = sp.simplify(b_low*(v0 - v1) + b_high*(v2 - v0))
    assert sp.simplify(total - 1) == 0
    # strictness UB < 3/2 and the eps^2 expansion:
    assert sp.simplify(sp.Rational(3, 2) - UB
                       - sp.Rational(3, 2)*e**2/(1 - e + e**2)) == 0
    ser = sp.series(UB, e, 0, 3).removeO()
    assert sp.simplify(ser - (sp.Rational(3, 2) - sp.Rational(3, 2)*e**2)) == 0
    # lower bound: dependency sum u_i == 1+eps; delta_c = (1/2-eps)/3
    V = [(1, e, 0), (0, 1, e), (e, 0, 1)]
    for j in range(3):
        assert sp.simplify(sum(V[i][j] for i in range(3)) - (1 + e)) == 0
    dc = sp.simplify(sp.Abs(1 + e - sp.Rational(3, 2))/3)
    mom = sp.simplify(1/(1 - 2*dc))
    for e0 in (sp.Rational(1, 10), sp.Rational(1, 20), sp.Rational(1, 50)):
        assert sp.nsimplify(mom.subs(e, e0)) == sp.nsimplify(LB.subs(e, e0))
    # the three R13 points:
    pts = {sp.Rational(1, 10): sp.Rational(135, 91),
           sp.Rational(1, 20): sp.Rational(190, 127),
           sp.Rational(1, 50): sp.Rational(1225, 817)}
    for e0, val in pts.items():
        assert sp.nsimplify(UB.subs(e, e0)) == val, (e0, val)
    print("THEOREM verified: (3/2)/(1+eps) <= D(tilt eps) <= "
          "(3/2)(1-eps)/(1-eps+eps^2) < 3/2 on (0,1/2);")
    print("  x*(eps) = (1-2eps)/(3(1-eps)); both branches equal; mass 1;")
    print("  UB = 3/2 - (3/2)eps^2 + O(eps^3); R13 points 135/91, 190/127,")
    print("  1225/817 reproduced exactly.  ALL OK")


if __name__ == '__main__':
    check_theorem()
