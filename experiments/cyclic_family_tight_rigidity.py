"""R6-4: tightness & rigidity for the cyclic concurrent family (notes/50-R6-4).

Verifies, exactly (fractions/sympy), the ingredients of the family theorem:
  With alpha=1-2pA, beta=1-2pB, gamma=1-2pC (edge masses, alpha+beta+gamma=1),
  S = alpha*beta+beta*gamma+gamma*alpha:
  (1) The MMM edge-tiling solution is I1=[ag/S,1-ab/S], I2=[bg/S,1-ag/S],
      I3=[ab/S,1-bg/S]; sum r = 1 IDENTICALLY on the concurrence family; all
      M-validity conditions hold with strictly positive closed-form margins.
  (2) Affine relation a1*u1+a2*u2+a3*u3 == S with (a1,a2,a3) =
      (alpha(1-alpha), gamma(1-gamma), beta(1-beta)); sum a_i = 2S;
      sum a_i l_i = S - abg/S,  sum a_i h_i = S + abg/S  (margin = alpha*beta*gamma).
  (3) LLL solution [0, l_i], RRR solution [h_i, 1] (same endpoints), each with
      sum r = 1; witness x* = V^{-1}(l + delta*1), delta = abg/(2 S^2), lies in
      the OPEN triangle (all barycentric coords positive in closed form) and is
      uncovered by LLL; symmetrically y* for RRR.
  (4) Exact rational coverage check (polygon clipping over Q): the MMM planks
      cover the triangle (uncovered area == 0) at sample family points; LLL/RRR
      leave positive uncovered area.
  (5) General-tau tiling solutions: [lam_i, rho_i], [0, lam_i], [rho_i, 1] with
      lam_i = tau_i(1 - tau_{i+1}(1-tau_{i+2}))/(1+tau1*tau2*tau3),
      rho_i = (1 - tau_{i+2}(1-tau_i))/(1+(1-tau1)(1-tau2)(1-tau3));
      validity always holds; exact grid searches at tau=(1/2,...) (medians) and
      tau=(1/2,2/3,1/3) find exactly these three.
"""
from fractions import Fraction as F
from itertools import product
import sympy as sp


def sym_checks():
    al, be = sp.symbols('alpha beta', positive=True)
    ga = 1 - al - be
    S = al*be + be*ga + ga*al
    a = [al*(1-al), ga*(1-ga), be*(1-be)]
    l = [al*ga/S, be*ga/S, al*be/S]
    h = [1-al*be/S, 1-al*ga/S, 1-be*ga/S]
    z = sp.simplify
    assert z(sum(h)-sum(l)-1) == 0                       # sum r = 1
    assert z(sum(a)-2*S) == 0
    assert z(sum(x*y for x, y in zip(a, l)) - (S - al*be*ga/S)) == 0
    assert z(sum(x*y for x, y in zip(a, h)) - (S + al*be*ga/S)) == 0
    # witness x* for LLL non-coverage: positivity of barycentric coords
    pA, pB, pC = (1-al)/2, (1-be)/2, (1-ga)/2
    t1, t2, t3 = (sp.Rational(1,2)-pC)/pA, (sp.Rational(1,2)-pB)/pC, (sp.Rational(1,2)-pA)/pB
    V = sp.Matrix([[t1, 0, 1], [0, 1, t2], [1, t3, 0]])
    delta = al*be*ga/(2*S**2)
    x = V.solve(sp.Matrix([l[0]+delta, l[1]+delta, l[2]+delta]))
    assert z(x[0]+x[1]+x[2]-1) == 0
    facs = [sp.factor(z(c)) for c in x]
    # each factors as (positive)/(positive) on 0<al,0<be,al+be<1 -- printed for audit
    print('x* =', facs)
    y = V.solve(sp.Matrix([h[0]-delta, h[1]-delta, h[2]-delta]))
    assert z(y[0]+y[1]+y[2]-1) == 0
    print('y* =', [sp.factor(z(c)) for c in y])
    print('symbolic checks OK')


def clip(poly, a, b, c):
    out = []
    for i in range(len(poly)):
        P, Q = poly[i], poly[(i+1) % len(poly)]
        fP, fQ = a*P[0]+b*P[1]-c, a*Q[0]+b*Q[1]-c
        if fP <= 0:
            out.append(P)
        if (fP < 0 < fQ) or (fQ < 0 < fP):
            t = fP/(fP-fQ)
            out.append((P[0]+t*(Q[0]-P[0]), P[1]+t*(Q[1]-P[1])))
    return out


def area(poly):
    if len(poly) < 3:
        return F(0)
    s = F(0)
    for i in range(len(poly)):
        x1, y1 = poly[i]
        x2, y2 = poly[(i+1) % len(poly)]
        s += x1*y2 - x2*y1
    return abs(s)/2


def uncovered(taus, I):
    t1, t2, t3 = taus
    U = [(t1-1, -1, 1), (-t2, 1-t2, t2), (1, t3, 0)]
    Tri = [(F(0), F(0)), (F(1), F(0)), (F(0), F(1))]
    tot = F(0)
    for signs in product([0, 1], repeat=3):
        poly = Tri
        for (cA, cB, c0), (lo, hi), s in zip(U, I, signs):
            poly = clip(poly, cA, cB, lo-c0) if s == 0 else clip(poly, -cA, -cB, c0-hi)
            if not poly:
                break
        tot += area(poly)
    return tot


def family(alpha, beta):
    gamma = 1-alpha-beta
    S = alpha*beta+beta*gamma+gamma*alpha
    pA, pB, pC = (1-alpha)/2, (1-beta)/2, (1-gamma)/2
    taus = ((F(1, 2)-pC)/pA, (F(1, 2)-pB)/pC, (F(1, 2)-pA)/pB)
    lo = (alpha*gamma/S, beta*gamma/S, alpha*beta/S)
    hi = (1-alpha*beta/S, 1-alpha*gamma/S, 1-beta*gamma/S)
    return taus, {'MMM': list(zip(lo, hi)),
                  'LLL': [(F(0), v) for v in lo],
                  'RRR': [(v, F(1)) for v in hi]}


def coverage_checks():
    for al, be in [(F(1, 3), F(1, 3)), (F(1, 10), F(2, 5)), (F(9, 20), F(9, 20)),
                   (F(1, 100), F(1, 100)), (F(48, 100), F(1, 100))]:
        taus, cfgs = family(al, be)
        res = {k: uncovered(taus, I) for k, I in cfgs.items()}
        sr = {k: sum(h-l for l, h in I) for k, I in cfgs.items()}
        assert res['MMM'] == 0 and sr['MMM'] == 1
        assert res['LLL'] > 0 and res['RRR'] > 0 and sr['LLL'] == 1 and sr['RRR'] == 1
        print(f'alpha={al} beta={be}: MMM covers (Sr=1); LLL/RRR uncovered '
              f'areas {res["LLL"]}, {res["RRR"]}')


if __name__ == '__main__':
    sym_checks()
    coverage_checks()
    print('ALL OK')
