#!/usr/bin/env python3
"""
defect_duality.py -- Round 9 (R9-B1/B2/B3): exact verification of the duality
theory for the transport defect D(u), the wedge certificates, the facet dual
certificate, the centroid bound delta(u) <= 1/6, the no-external-concurrence
counting lemma, the facet-defect value (d+1)/2 on Delta^d, and the B4 region
algebra.

All arithmetic is exact (sympy Rational / symbols).  No floats decide anything.

Conventions (paper):
  Delta = {lam in R^3 : lam_i >= 0, sum lam_i = 1};
  a direction u is given by its vertex values v = (v_A, v_B, v_C) in [0,1]^3
  with min v = 0, max v = 1;  u(lam) = <v, lam>.
  Cyclic triple: u1=(tau1,0,1), u2=(0,1,tau2), u3=(1,tau3,0).

Checks:
  1. facet dual certificate  psi(t) = (1 - 3t/2)_+  : mass 1, value 3/2.
  2. affine dependency (c, c0) for a triple; wedge-certificate value
     A/(2*min(K1,K2)) = 1/(1-2*delta_c); theta* <= 1; K1,K2 > 0.
  3. exact delta(u) via vertex-enumeration LP; verify delta_c <= delta,
     delta <= 1/6 (centroid), and compare delta vs delta_c on a batch.
  4. sandwich tau=(13/25,1/2,1/2): c prop (75,76,74), c0=113, K2=112, A=225,
     wedge value = 225/224 (= moment bound), theta*=224/225; explicit dual
     psi_i feasibility: mass identity and the telescoping constant K2.
  5. external concurrence: for q outside Delta (with sum q = 1), the patterns
     (j0, j1) whose direction has mid-line through q are exactly the pairs
     with (q_{j0}-1/2)(q_{j1}-1/2) >= 0; count non-flip-equivalent solutions
     (must be < 3 for external q; 3 possible only for q in Delta).
  6. centroid: u(G) = (0+s+1)/3 in [1/3, 2/3]; hence delta(u) <= 1/6 for ANY
     finite family; equality needs s in {0,1} (facet-like directions).
  7. Delta^d facet cycle, d = 2..7: P_k = cyclic shifts of (0,1,...,d)/m,
     m = d(d+1)/2, each of the d+1 edges mass 1/(d+1) uniform; every
     coordinate marginal == ((d+1)/2) * 1_{[0, 2/(d+1)]}.  Hence
     D_d(facets) <= (d+1)/2; the moment bound (delta = (d-1)/(2(d+1)))
     gives >= (d+1)/2: equality.
  8. B4 region: eps(m) = k m^2/(1+k m), k = (2*sqrt(3)-3)/6, satisfies
     1 + eps/(m(m-eps)) = 1/(4*sqrt(3)-6); and eps(1/2) > 1/60.
"""

from fractions import Fraction as F
from itertools import combinations, permutations
import random

import sympy as sp

S = sp.S
HALF = S(1) / 2


# ----------------------------------------------------------------------
# generic helpers
# ----------------------------------------------------------------------

def cyclic_vertex_values(tau):
    """Vertex-value vectors (rows: u1,u2,u3; cols: A,B,C) of a cyclic triple."""
    t1, t2, t3 = [S(t) for t in tau]
    return [(t1, S(0), S(1)), (S(0), S(1), t2), (S(1), t3, S(0))]


def dependency(V):
    """(c1,c2,c3,c0), integer-normalized, with sum_i c_i * u_i == c0 on the
    plane of Delta.  V = list of three vertex-value triples."""
    c1, c2, c3, c0 = sp.symbols('c1 c2 c3 c0')
    eqs = [sp.Eq(c1 * V[0][j] + c2 * V[1][j] + c3 * V[2][j], c0)
           for j in range(3)]
    sol = sp.solve(eqs, [c1, c2, c3], dict=True)
    assert len(sol) == 1, "directions pairwise parallel? no unique dependency"
    s = sol[0]
    vals = [sp.simplify(s[c1]), sp.simplify(s[c2]), sp.simplify(s[c3]), c0]
    # normalize: set c0 -> lcm of denominators after c0=1 substitution
    vals = [sp.nsimplify(v.subs(c0, 1)) for v in vals[:3]] + [S(1)]
    dens = [sp.fraction(sp.together(v))[1] for v in vals]
    L = sp.ilcm(*[sp.Integer(d) for d in dens]) if all(d.is_Integer for d in dens) else 1
    return [sp.simplify(v * L) for v in vals[:3]] + [S(L)]


def wedge_value(V):
    """Wedge-certificate value 1/(1-2 delta_c) and delta_c for a triple."""
    c1, c2, c3, c0 = dependency(V)
    A = sum(abs(c) for c in (c1, c2, c3))
    P = sum(c for c in (c1, c2, c3) if c > 0)
    N = sum(-c for c in (c1, c2, c3) if c < 0)
    K1, K2 = c0 + N, P - c0
    assert K1 > 0 and K2 > 0, (K1, K2)
    assert sp.simplify(K1 + K2 - A) == 0
    kappa = min(K1, K2)
    theta = 2 * kappa / A
    assert theta <= 1
    delta_c = sp.Rational(sp.Abs(c0 - (c1 + c2 + c3) / 2), A)
    val = sp.Rational(A, 2 * kappa)
    assert sp.simplify(val - 1 / (1 - 2 * delta_c)) == 0
    return val, delta_c, (c1, c2, c3, c0), theta


# ----------------------------------------------------------------------
# exact delta(u) by vertex enumeration (LP: min z, |u_i(lam)-1/2| <= z, lam in Delta)
# ----------------------------------------------------------------------

def delta_exact(V):
    """Exact concurrence defect for a family of directions (vertex values V)."""
    # variables x = (lam1, lam2, z); lam3 = 1 - lam1 - lam2.
    # constraints (all as  a.x <= b):
    #   for each i:  u_i - 1/2 <= z  and  1/2 - u_i <= z
    #   lam1 >= 0, lam2 >= 0, lam1 + lam2 <= 1     ; minimize z.
    cons = []
    for v in V:
        vA, vB, vC = [S(t) for t in v]
        # u(lam) = vC + (vA - vC) lam1 + (vB - vC) lam2
        cons.append(((vA - vC, vB - vC, S(-1)), HALF - vC))
        cons.append(((-(vA - vC), -(vB - vC), S(-1)), vC - HALF))
    cons.append(((S(-1), S(0), S(0)), S(0)))
    cons.append(((S(0), S(-1), S(0)), S(0)))
    cons.append(((S(1), S(1), S(0)), S(1)))
    best = None
    n = len(cons)
    for idx in combinations(range(n), 3):
        Mrows = [cons[i][0] for i in idx]
        bvec = [cons[i][1] for i in idx]
        M = sp.Matrix(Mrows)
        if M.det() == 0:
            continue
        x = M.solve(sp.Matrix(bvec))
        # feasibility
        ok = all(sum(a * xx for a, xx in zip(c[0], x)) <= c[1] + 0 for c in cons)
        if ok:
            z = x[2]
            if best is None or z < best:
                best = z
    assert best is not None
    return sp.nsimplify(best)


# ----------------------------------------------------------------------
# 1. facet dual certificate
# ----------------------------------------------------------------------

def check_facet_dual():
    t = sp.symbols('t', nonnegative=True)
    psi = sp.Max(0, 1 - 3 * t / 2)
    mass = 3 * sp.integrate(1 - 3 * t / 2, (t, 0, sp.Rational(2, 3)))
    assert sp.simplify(mass - 1) == 0
    # minorant identity: sum_i (1 - 3 lam_i / 2) = 3 - 3/2 = 3/2 on Delta
    l1, l2 = sp.symbols('l1 l2', nonnegative=True)
    l3 = 1 - l1 - l2
    lin = sum(1 - 3 * l / 2 for l in (l1, l2, l3))
    assert sp.simplify(lin - sp.Rational(3, 2)) == 0
    # pointwise psi >= linear  and spot checks with random rationals
    rng = random.Random(9)
    for _ in range(200):
        a = F(rng.randint(0, 60), 60)
        b = F(rng.randint(0, 60 - a.numerator * 60 // a.denominator or 1), 60)
        if a + b > 1:
            continue
        lam = [S(a.numerator) / a.denominator, S(b.numerator) / b.denominator]
        lam.append(1 - lam[0] - lam[1])
        val = sum(sp.Max(0, 1 - 3 * l / 2) for l in lam)
        assert val >= sp.Rational(3, 2)
    print("1. facet dual certificate psi=(1-3t/2)_+ : mass=1, value>=3/2  OK")


# ----------------------------------------------------------------------
# 4. sandwich wedge certificate
# ----------------------------------------------------------------------

def check_sandwich():
    V = cyclic_vertex_values((sp.Rational(13, 25), HALF, HALF))
    val, delta_c, (c1, c2, c3, c0), theta = wedge_value(V)
    assert (c1, c2, c3, c0) == (75, 76, 74, 113), (c1, c2, c3, c0)
    assert val == sp.Rational(225, 224), val
    assert delta_c == sp.Rational(1, 450), delta_c
    assert theta == sp.Rational(224, 225), theta
    # explicit dual: mirror family (kappa = K2): phi_i(t) = 1-t for c_i>0
    # telescoping constant: sum_i c_i * (1 - u_i(lam)) == K2 = P - c0 = 112
    l1, l2 = sp.symbols('l1 l2')
    l3 = 1 - l1 - l2
    lam = (l1, l2, l3)
    consts = []
    for c, v in zip((c1, c2, c3), V):
        u = sum(vv * ll for vv, ll in zip(v, lam))
        consts.append(c * (1 - u))
    assert sp.simplify(sum(consts) - 112) == 0
    # masses: w = 2/(A theta^2); sum_i w c_i theta^2/2 = w theta^2 A/2 = 1
    A = 225
    w = 2 / (A * theta ** 2)
    assert sp.simplify(w * theta ** 2 * A / 2 - 1) == 0
    # certificate value: w (A theta - K2) = A/(2 K2) = 225/224
    assert sp.simplify(w * (A * theta - 112) - sp.Rational(225, 224)) == 0
    # moment bound comparison: delta = delta_c here
    d = delta_exact(V)
    assert d == sp.Rational(1, 450), d
    print("4. sandwich tau=(13/25,1/2,1/2): c=(75,76,74|113), wedge=225/224 "
          "= moment bound, theta=224/225, dual mass/constant identities  OK")


# ----------------------------------------------------------------------
# 3. delta vs delta_c on a batch; centroid bound
# ----------------------------------------------------------------------

def check_delta_batch():
    rng = random.Random(7)
    triples = [
        (HALF, HALF, HALF),
        (sp.Rational(13, 25), HALF, HALF),
        (sp.Rational(9, 10), sp.Rational(9, 10), sp.Rational(9, 10)),
        (sp.Rational(1, 10), sp.Rational(4, 5), sp.Rational(3, 5)),
        (sp.Rational(5, 9), sp.Rational(4, 5), sp.Rational(1, 6)),
        (sp.Rational(99, 100), sp.Rational(1, 100), HALF),
    ]
    for _ in range(6):
        triples.append(tuple(sp.Rational(rng.randint(1, 19), 20) for _ in range(3)))
    strict = []
    for tau in triples:
        V = cyclic_vertex_values(tau)
        val, delta_c, cdep, theta = wedge_value(V)
        d = delta_exact(V)
        assert delta_c <= d, (tau, delta_c, d)
        assert d <= sp.Rational(1, 6), (tau, d)          # centroid bound
        if delta_c != d:
            strict.append((tau, delta_c, d))
    # facet triple: delta = delta_c = 1/6
    Vf = [(S(1), S(0), S(0)), (S(0), S(1), S(0)), (S(0), S(0), S(1))]
    valf, dcf, cf, thf = wedge_value(Vf)
    assert dcf == sp.Rational(1, 6) and valf == sp.Rational(3, 2)
    assert delta_exact(Vf) == sp.Rational(1, 6)
    df = delta_exact(Vf)
    print(f"3. batch of {len(triples)} cyclic triples: delta_c <= delta <= 1/6 "
          f"OK; strict delta_c < delta in {len(strict)} cases"
          + (f" (e.g. {strict[0]})" if strict else " (equality throughout)"))
    print("   facet triple: delta = delta_c = 1/6, wedge value = 3/2  OK")
    return strict


# ----------------------------------------------------------------------
# 5. no external concurrence (sign-counting lemma)
# ----------------------------------------------------------------------

def patterns_through(q):
    """Ordered patterns (j0, j1) with a normalized direction whose mid-line
    passes through q (q in the plane sum=1, exact rationals).
    Returns list of (j0, j1, s)."""
    out = []
    for j0, j1 in permutations(range(3), 2):
        js = 3 - j0 - j1
        # u(q) = q_{j1} + s q_{js} = 1/2
        if q[js] == 0:
            if q[j1] == HALF:
                out.append((j0, j1, None))  # any s: degenerate family
            continue
        s = (HALF - q[j1]) / q[js]
        if 0 <= s <= 1:
            out.append((j0, j1, sp.nsimplify(s)))
    return out


def check_external():
    rng = random.Random(11)
    for _ in range(300):
        # random external rational point on the plane sum=1
        a = sp.Rational(rng.randint(-40, 60), 20)
        b = sp.Rational(rng.randint(-40, 60), 20)
        q = (a, b, 1 - a - b)
        if all(x >= 0 for x in q):
            continue  # inside: skip
        pats = patterns_through(q)
        # group into flip classes: (j0,j1) ~ (j1,j0)
        classes = {frozenset((p[0], p[1])) for p in pats}
        assert len(classes) <= 2, (q, pats)
        # sign criterion: pair {j,k} solvable iff (q_j-1/2)(q_k-1/2) >= 0
        for p in pats:
            assert (q[p[0]] - HALF) * (q[p[1]] - HALF) >= 0, (q, p)
    # and an inside point admits 3 classes (e.g. centroid)
    G = (sp.Rational(1, 3),) * 3
    assert len({frozenset((p[0], p[1])) for p in patterns_through(G)}) == 3
    print("5. external q: at most 2 flip-classes of mid-lines through q "
          "(300 random external points); sign criterion verified  OK")


# ----------------------------------------------------------------------
# 6. centroid bound (symbolic)
# ----------------------------------------------------------------------

def check_centroid():
    s = sp.symbols('s')
    val = (0 + s + 1) / 3
    lo = sp.simplify(val.subs(s, 0) - sp.Rational(1, 3))
    hi = sp.simplify(val.subs(s, 1) - sp.Rational(2, 3))
    assert lo == 0 and hi == 0
    # so for s in [0,1]: u(G) in [1/3, 2/3], |u(G)-1/2| <= 1/6.
    print("6. centroid: u(G)=(1+s)/3 in [1/3,2/3] for s in [0,1]; "
          "delta(u) <= 1/6 for ANY finite family  OK")


# ----------------------------------------------------------------------
# 7. facet cycle on Delta^d : marginals == (d+1)/2 on [0, 2/(d+1)]
# ----------------------------------------------------------------------

def check_facet_cycle(dmax=7):
    for d in range(2, dmax + 1):
        n = d + 1
        m = sp.Rational(d * (d + 1), 2)
        base = [sp.Rational(k, 1) / m for k in range(n)]     # (0,1,...,d)/m
        assert sum(base) == 1
        # P_k = shift^k(base):  (P_k)_j = base[(j-k) mod n]
        P = [[base[(j - k) % n] for j in range(n)] for k in range(n)]
        mass = sp.Rational(1, n)
        top = sp.Rational(2, d + 1)
        assert base[-1] == top
        for j in range(n):
            # segments of coordinate j along the cycle P_0 -> P_1 -> ... -> P_0
            segs = []
            for k in range(n):
                a, b = P[k][j], P[(k + 1) % n][j]
                assert a != b
                segs.append((min(a, b), max(a, b), mass / abs(b - a)))
            # breakpoints
            pts = sorted(set([x for s0 in segs for x in (s0[0], s0[1])]))
            assert pts[0] == 0 and pts[-1] == top
            for lo, hi in zip(pts[:-1], pts[1:]):
                dens = sum(s0[2] for s0 in segs if s0[0] <= lo and hi <= s0[1])
                assert dens == sp.Rational(d + 1, 2), (d, j, lo, hi, dens)
            # total mass of the marginal
            tot = sum((s0[1] - s0[0]) * s0[2] for s0 in segs)
            assert tot == 1
    print(f"7. Delta^d facet cycle, d=2..{dmax}: all coordinate marginals "
          "== ((d+1)/2) 1_[0,2/(d+1)]  =>  D_d(facets) = (d+1)/2  OK")


# ----------------------------------------------------------------------
# 8. B4 region algebra
# ----------------------------------------------------------------------

def check_region():
    m, eps = sp.symbols('m epsilon', positive=True)
    k = (2 * sp.sqrt(3) - 3) / 6
    target = 1 / (4 * sp.sqrt(3) - 6)
    assert sp.simplify(1 + k - target) == 0
    eps_m = k * m ** 2 / (1 + k * m)
    expr = 1 + eps_m / (m * (m - eps_m))
    assert sp.simplify(expr - target) == 0
    # Cor 27/29 box is inside: eps(1/2) > 1/60  <=>  58 k > 4  <=> 10092 > 9801
    val = eps_m.subs(m, HALF)
    assert sp.simplify(val - sp.Rational(1, 60)) > 0
    print("8. B4 region: eps(m)=k m^2/(1+k m), k=(2sqrt3-3)/6 gives "
          "D-bound = 1/(4sqrt3-6) exactly; eps(1/2) > 1/60  OK")


# ----------------------------------------------------------------------
# 2. wedge machinery consistency on the facet triple (family-1 wedge)
# ----------------------------------------------------------------------

def check_facet_wedge():
    Vf = [(S(1), S(0), S(0)), (S(0), S(1), S(0)), (S(0), S(0), S(1))]
    val, delta_c, (c1, c2, c3, c0), theta = wedge_value(Vf)
    assert (c1, c2, c3, c0) == (1, 1, 1, 1)
    assert val == sp.Rational(3, 2) and theta == sp.Rational(2, 3)
    # family-1 wedge with theta=2/3, w=2/(A theta^2)=3/2:
    # psi_i(t) = (3/2)(2/3 - t)_+ = (1 - 3t/2)_+  -- matches check 1
    w = sp.Rational(2, 1) / (3 * theta ** 2)
    assert w == sp.Rational(3, 2)
    print("2. facet wedge: c=(1,1,1|1), theta*=2/3, w=3/2, psi=(1-3t/2)_+ "
          "(same certificate as check 1)  OK")


if __name__ == '__main__':
    check_facet_dual()
    check_facet_wedge()
    strict = check_delta_batch()
    check_sandwich()
    check_external()
    check_centroid()
    check_facet_cycle()
    check_region()
    print("ALL OK")
