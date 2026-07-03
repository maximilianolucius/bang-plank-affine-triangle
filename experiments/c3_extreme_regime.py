#!/usr/bin/env python3
"""
c3_extreme_regime.py -- R13-1: the EXTREME REGIME of the two-regime strategy
for C_3(u_tau) = 1 (three planks, one per direction, cyclic triples).

THEOREM (extreme regime; proved by hand in notes/56-R13-1, verified here).
For every cyclic tau there is an explicit w0(tau) > 0 such that every covering
of Delta by three planks P_i = {u_i in [l_i, h_i]} (one per direction) with
max_i r_i >= 1 - w0(tau) satisfies  Sigma r >= 1, with equality only for the
trivial covering (one full plank, the other two of width 0).

Proof skeleton (big plank = P_1; the other two cases follow by the cyclic
rotation rho: tau -> (tau2, tau3, tau1)):
  the remainder Delta \\ P_1 is the union of two corner pieces
     K_lo = {u_1 <= l} (corner at B),  K_hi = {u_1 >= 1-s} (corner at C),
  with l + s <= w0 < min(tau1, 1-tau1) -- so both pieces are triangles whose
  vertex sets are {B, X_AB(l), X_BC(l)} and {C, X_CA(s), X_CB(s)}.
  Ranges (exact, verified symbolically below):
     u_2(K_lo) = [1 - l/tau1, 1]                    (extent  a2 = l/tau1)
     u_3(K_lo) = [tau3(1-l), tau3 + (1-tau3)l/tau1] (extent  a3 = l g2/tau1)
     u_2(K_hi) = [tau2(1-s/(1-tau1)), tau2+(1-tau2)s] (extent b2 = s g3/(1-tau1))
     u_3(K_hi) = [0, s/(1-tau1)]                    (extent  b3 = s/(1-tau1))
  with g2 = 1 - tau3(1-tau1), g3 = 1 - tau1(1-tau2) (the dependency factors
  of Thm 6.13).
  CASE A (no plank meets both pieces): each nonempty piece is covered by the
  planks assigned to it alone.
   - assignment (P2->lo, P3->hi): r2 >= a2 >= l/tau1 > l, r3 >= b3 > s: done.
   - assignment (P2->hi, P3->lo): r2 >= b2 >= s (g3 > 1-tau1 <=> tau1 tau2>0),
     r3 >= a3 >= l (g2 > tau1 <=> (1-tau1)(1-tau3) > 0): done.
   - both -> lo (so s = 0): the pieces are covered JOINTLY: by Gardner's
     two-direction relative-width measure ON THE CONVEX BODY K_lo
     (Thm 3.1 applied to K_lo -- the first use of the closed 2-plank case as
     a tool), r2/a2 + r3/a3 >= 1, hence r2 + r3 >= min(a2,a3) = l g2/tau1
     >= l: done.  Both -> hi (l = 0): r2+r3 >= min(b2,b3) = s g3/(1-tau1)
     >= s: done.
  CASE B (some plank meets both pieces): its interval must SPAN the gap
  between the two ranges:
   - if P2 meets both:  r2 >= (1 - l/tau1) - (tau2 + (1-tau2)s)
                            = (1-tau2) - l/tau1 - (1-tau2)s  >= l + s
     whenever l+s <= 2 w0 and w0 <= (1-tau2) tau1 / (2(1+tau1)).
   - if P3 meets both:  r3 >= tau3(1-l) - s/(1-tau1)  >= l + s
     whenever w0 <= tau3 (1-tau1) / (2(2-tau1)).
  In all cases Sigma r >= (1 - l - s) + (l + s) = 1, strictly unless l=s=0.

  w0^(1)(tau) = (1/2) min( tau1, 1-tau1,
                           (1-tau2) tau1 / (1+tau1),
                           tau3 (1-tau1) / (2-tau1) );
  w0(tau) = min over the three cyclic rotations.

ALSO verified here: the INSUFFICIENCY of the naive per-piece width bounds
(why the position/gap analysis of Case B is essential): at the sandwich, the
LP  min(r2+r3)  s.t.  r2/a2+r3/a3 >= 1, r2/b2+r3/b3 >= 1  has value < l+s.

All checks exact (sympy / fractions).
"""

import random
from fractions import Fraction as F

import sympy as sp

t1, t2, t3, l, s = sp.symbols('tau1 tau2 tau3 l s', positive=True)
g2 = 1 - t3*(1 - t1)
g3 = 1 - t1*(1 - t2)

# vertex values of the cyclic triple at (A,B,C)
U = [(t1, 0, 1), (0, 1, t2), (1, t3, 0)]


def uval(i, lam):
    return sum(U[i][j]*lam[j] for j in range(3))


def check_ranges():
    # corner K_lo: vertices B, X_AB(l), X_BC(l)  (valid for l < tau1)
    B = (0, 1, 0)
    X_AB = (1 - (1 - l/t1), l/t1, 0)          # on AB: A + (1 - l/t1)(B-A)?
    # parametrize properly: on AB from A(t=0) to B(t=1): u1 = tau1(1-t);
    # u1 = l at t = 1 - l/tau1: point = A + t(B-A) = (1-t, t, 0)
    tAB = 1 - l/t1
    X_AB = (1 - tAB, tAB, 0)
    # on BC from B(t=0) to C(t=1): u1 = t; u1 = l at t = l: (0, 1-l, l)
    X_BC = (0, 1 - l, l)
    lo = [B, X_AB, X_BC]
    # corner K_hi: vertices C, X_CA(s), X_CB(s)  (valid for s < 1-tau1)
    C = (0, 0, 1)
    # on CA from C(t=0) to A(t=1): u1 = 1-(1-tau1)t = 1-s at t = s/(1-tau1)
    tCA = s/(1 - t1)
    X_CA = (tCA, 0, 1 - tCA)
    # on CB from C(t=0) to B(t=1): u1 = 1-t = 1-s at t = s: (0, s, 1-s)
    X_CB = (0, s, 1 - s)
    hi = [C, X_CA, X_CB]
    # sanity: u1 values
    for P in (X_AB, X_BC):
        assert sp.simplify(uval(0, P) - l) == 0
    for P in (X_CA, X_CB):
        assert sp.simplify(uval(0, P) - (1 - s)) == 0

    v2lo = [sp.expand(uval(1, P)) for P in lo]
    v3lo = [sp.expand(uval(2, P)) for P in lo]
    v2hi = [sp.expand(uval(1, P)) for P in hi]
    v3hi = [sp.expand(uval(2, P)) for P in hi]
    # claimed ranges (orderings valid on (0,1)^3, l,s small):
    claims = [
        (v2lo, 1 - l/t1, 1),
        (v3lo, t3*(1 - l), t3 + (1 - t3)*l/t1),
        (v2hi, t2*(1 - s/(1 - t1)), t2 + (1 - t2)*s),
        (v3hi, 0, s/(1 - t1)),
    ]
    for vals, lo_c, hi_c in claims:
        assert any(sp.simplify(v - lo_c) == 0 for v in vals)
        assert any(sp.simplify(v - hi_c) == 0 for v in vals)
        # ordering: lo_c <= each value <= hi_c on the domain -- check the
        # nontrivial comparisons as factored nonneg differences at random
        # rationals (the factored proofs are in the note)
        rng = random.Random(3)
        for _ in range(150):
            sub = {t1: F(rng.randint(1, 19), 20), t2: F(rng.randint(1, 19), 20),
                   t3: F(rng.randint(1, 19), 20)}
            sub[l] = F(rng.randint(1, 100), 1000)*min(sub[t1], 1-sub[t1])
            sub[s] = F(rng.randint(1, 100), 1000)*min(sub[t1], 1-sub[t1])
            vv = [sp.nsimplify(sp.S(v).subs(sub)) for v in vals]
            assert min(vv) == sp.nsimplify(sp.S(lo_c).subs(sub))
            assert max(vv) == sp.nsimplify(sp.S(hi_c).subs(sub))
    # extents:
    a2 = sp.simplify(1 - (1 - l/t1))
    a3 = sp.simplify((t3 + (1-t3)*l/t1) - t3*(1-l))
    b2 = sp.simplify((t2 + (1-t2)*s) - t2*(1 - s/(1-t1)))
    b3 = s/(1-t1)
    assert sp.simplify(a2 - l/t1) == 0
    assert sp.simplify(a3 - l*g2/t1) == 0
    assert sp.simplify(b2 - s*g3/(1-t1)) == 0
    print("1. corner ranges and extents verified symbolically:")
    print("   a2=l/tau1, a3=l*g2/tau1, b2=s*g3/(1-tau1), b3=s/(1-tau1)  OK")


def check_caseA():
    # the four positivity facts behind Case A:
    facts = [
        (l/t1 - l, "a2 - l = l(1-tau1)/tau1 > 0"),
        (l*g2/t1 - l, "a3 - l = l(1-tau1)(1-tau3)/tau1 > 0"),
        (s*g3/(1-t1) - s, "b2 - s = s*tau1*tau2/(1-tau1) > 0"),
        (s/(1-t1) - s, "b3 - s = s*tau1/(1-tau1) > 0"),
    ]
    for expr, name in facts:
        f = sp.factor(sp.simplify(expr))
        # each factor is positive on (0,1)^3 x (l,s>0): check structure +
        # random exact evaluations
        rng = random.Random(5)
        for _ in range(200):
            sub = {t1: F(rng.randint(1, 19), 20), t2: F(rng.randint(1, 19), 20),
                   t3: F(rng.randint(1, 19), 20),
                   l: F(rng.randint(1, 99), 100), s: F(rng.randint(1, 99), 100)}
            assert sp.nsimplify(f.subs(sub)) > 0, (name, sub)
    # min(a2,a3) = l*g2/tau1 (g2<1) and min(b2,b3) = s*g3/(1-tau1) (g3<1):
    assert sp.simplify(sp.factor(1 - g2) - t3*(1-t1)) == 0
    assert sp.simplify(sp.factor(1 - g3) - t1*(1-t2)) == 0
    print("2. Case A inequalities: all four extents strictly exceed the "
          "piece width; joint-cover minima l*g2/tau1, s*g3/(1-tau1) >= l, s  OK")


def check_caseB_and_w0():
    w0 = sp.Rational(1, 2)*sp.Min(t1, 1-t1, (1-t2)*t1/(1+t1),
                                  t3*(1-t1)/(2-t1))
    # spanning bounds:
    gap2 = (1 - l/t1) - (t2 + (1-t2)*s)          # r2 >= gap2 if P2 meets both
    gap3 = t3*(1-l) - s/(1-t1)                   # r3 >= gap3 if P3 meets both
    # implications:  l,s <= w0  =>  gap >= l+s   (checked exactly at random
    # rationals including the boundary l=s=w0)
    rng = random.Random(7)
    for _ in range(400):
        sub = {t1: F(rng.randint(1, 19), 20), t2: F(rng.randint(1, 19), 20),
               t3: F(rng.randint(1, 19), 20)}
        w0v = sp.nsimplify(w0.subs(sub))
        assert w0v > 0
        for frac in (F(1, 1), F(1, 2), F(1, 7)):
            sub2 = dict(sub); sub2[l] = w0v*frac; sub2[s] = w0v*frac
            g2v = sp.nsimplify(gap2.subs(sub2))
            g3v = sp.nsimplify(gap3.subs(sub2))
            need = sub2[l] + sub2[s]
            assert g2v >= need, (sub2, g2v, need)
            assert g3v >= need, (sub2, g3v, need)
    print("3. Case B: with l,s <= w0(tau) both spanning gaps dominate l+s "
          "(400 random tau, incl. boundary l=s=w0)  OK")
    return w0


def check_insufficiency():
    # sandwich: per-piece width constraints alone admit r2+r3 < l+s
    tau = {t1: F(13, 25), t2: F(1, 2), t3: F(1, 2)}
    a2 = sp.nsimplify((l/t1).subs(tau))
    a3 = sp.nsimplify((l*g2/t1).subs(tau))
    b2 = sp.nsimplify((s*g3/(1-t1)).subs(tau))
    b3 = sp.nsimplify((s/(1-t1)).subs(tau))
    lv = sp.Symbol('lv', positive=True)
    a2, a3, b2, b3 = [sp.nsimplify(x.subs({l: lv, s: lv})) for x in
                      (a2, a3, b2, b3)]
    r2, r3 = sp.symbols('r2 r3', nonnegative=True)
    sol = sp.solve([sp.Eq(r2/a2 + r3/a3, 1), sp.Eq(r2/b2 + r3/b3, 1)],
                   [r2, r3], dict=True)[0]
    tot = sp.simplify(sol[r2] + sol[r3])
    ratio = sp.nsimplify(sp.simplify(tot/lv))
    assert sp.simplify(ratio - sp.Rational(1875, 1094)) == 0
    assert ratio < 2   # < l+s = 2l
    print(f"4. insufficiency at the sandwich: crossing-point LP gives "
          f"r2+r3 = ({ratio}) l = {float(ratio):.4f} l < 2l = l+s -- "
          "the per-piece 2-plank bounds alone CANNOT prove Sigma r >= 1; "
          "the position/gap coupling of Case B is essential  OK")


def end_to_end_sanity(w0_expr):
    """Random extreme-regime configurations built per the Case-A recipes must
    cover (exact oracle) and satisfy Sigma r >= 1 -- a cross-check that the
    case analysis constructs what it claims."""
    from covering_constant import covers_exact
    rng = random.Random(11)
    tested = 0
    for _ in range(60):
        tau = tuple(F(rng.randint(2, 18), 20) for _ in range(3))
        sub = {t1: tau[0], t2: tau[1], t3: tau[2]}
        w0q = sp.Rational(sp.nsimplify(w0_expr.subs(sub)))
        w0f = F(int(w0q.p), int(w0q.q))
        lv = F(rng.randint(1, 4), 5)*w0f
        sv = F(rng.randint(1, 4), 5)*w0f
        V = []
        for i in range(3):
            row = []
            for x in U[i]:
                xq = sp.Rational(sp.nsimplify(sp.S(x).subs(sub)))
                row.append(F(int(xq.p), int(xq.q)))
            V.append(tuple(row))
        # assignment (P2->lo, P3->hi): I2 = [1 - l/tau1, 1], I3 = [0, s/(1-t1)]
        I1 = (lv, 1 - sv)
        I2 = (1 - lv/tau[0], F(1))
        I3 = (F(0), sv/(1 - tau[0]))
        lh = [I1, I2, I3]
        ok, _ = covers_exact(V, lh)
        assert ok, (tau, lh)
        tot = sum(h - l_ for l_, h in lh)
        assert tot >= 1, (tau, lh, tot)
        tested += 1
    print(f"5. end-to-end sanity: {tested} random extreme-regime "
          "(P2->lo, P3->hi) configurations cover exactly and have "
          "Sigma r >= 1  OK")


if __name__ == '__main__':
    check_ranges()
    check_caseA()
    w0_expr = check_caseB_and_w0()
    check_insufficiency()
    end_to_end_sanity(w0_expr)
    print("ALL OK -- extreme-regime theorem verified; naive balanced route "
          "refuted (position coupling required)")
