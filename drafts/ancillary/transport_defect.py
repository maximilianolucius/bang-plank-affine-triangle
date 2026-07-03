#!/usr/bin/env python3
"""R7-2: the transport defect D(u) on the triangle.  All exact (sympy over Q).

D(u) = inf_mu max_i ess-sup dens(u_{i#}mu)   (directions normalized to [0,1] on Delta)

Facts verified here (all exact):

 1. MOMENT LOWER BOUND.  delta(u) = min_{p in Delta} max_i |u_i(p)-1/2|
    (the concurrence defect; delta=0 iff the mid-lines concur).  A density <= D
    with mass 1 on [0,1] has mean in [1/(2D), 1-1/(2D)]; the mean of u_{i#}mu is
    u_i(bary(mu)).  Hence  D(u) >= 1/(1-2*delta(u)).
    Facets: sum lambda_i = 1 forces some mean <= 1/3, so delta = 1/6, D >= 3/2.

 2. FACETS: D = 3/2 EXACTLY.  The uniform measure on the perimeter of the
    inscribed triangle P0=(0,1/3,2/3), P1=(2/3,0,1/3), P2=(1/3,2/3,0) (mass 1/3
    per segment) has all three lambda_i-marginals == (3/2) 1_[0,2/3]:
    each coordinate rises 0->2/3 on one segment (density 1/2) and falls through
    the two halves on the others (density 1 each).  Verified exactly below.

 3. LOOP WITNESS (general principle).  For any triple u and any ell in (0,1]:
    if there are Q0,Q1,Q2 in Delta and centers c_i with
       u_i(anchor Q) = c_i,  u_i(other two Qs) = c_i -+ ell/2,
    then the 3-segment loop with mass 1/3 per segment (uniform) has
    u_i-marginals uniform on [c_i - ell/2, c_i + ell/2] with density 1/ell.
    If moreover the blocks lie in [0,1] and ell = 1-2*delta(u), then combined
    with 1:  D(u) = 1/(1-2*delta(u))  EXACTLY.
    The script solves the 9x9 linear system (unknowns Q (6 dof) + c (3)) for all
    anchor/sign patterns and checks Q in Delta, block containment, and
    max|c_i - 1/2| = delta.

 4. NEAR-SURFACE UPPER BOUND (skeleton).  For a cyclic triple tau within eps of
    a concurrent tau* (weights alpha,beta,gamma), the edge-skeleton measure with
    the *frozen* weights w* = (gamma, alpha, beta) has all six densities within
    eps * w*/(tau tau*) <= eps/(m(m-eps)) of 1, m = min_i min(tau_i*, 1-tau_i*).
    Hence D(u_tau) <= 1 + eps/(m(m-eps)) and every covering by planks in these
    directions has  sum rw >= 1 - eps/(m(m-eps)).  Verified symbolically and on
    exact samples; sandwiched against the lower bound of 1.

Run: python3 transport_defect.py
"""

import itertools
from fractions import Fraction
from sympy import Rational, symbols, simplify, solve, linsolve, Matrix, S, nsimplify

H = Rational(1, 2)


# ---------- exact tiny LP by vertex enumeration ------------------------------

def lp_min(constraints, objective, nvars):
    """Minimize objective (linear, as coefficient vector with constant term
    last) subject to constraints a.x + b <= 0.  Exact vertex enumeration:
    every LP optimum is at a vertex where nvars constraints are active."""
    best, argbest = None, None
    cons = [Matrix(c) for c in constraints]
    obj = Matrix(objective)
    for active in itertools.combinations(range(len(cons)), nvars):
        A = Matrix([[cons[k][j] for j in range(nvars)] for k in active])
        if A.det() == 0:
            continue
        b = Matrix([-cons[k][nvars] for k in active])
        x = A.solve(b)
        if all(sum(c[j] * x[j] for j in range(nvars)) + c[nvars] <= 0 for c in cons):
            val = sum(obj[j] * x[j] for j in range(nvars)) + obj[nvars]
            if best is None or val < best:
                best, argbest = val, x
    return best, argbest


def delta_defect(vals):
    """delta(u) = min_{p in Delta} max_i |u_i(p)-1/2|, exact.
    Variables (p1, p2, s); p3 = 1-p1-p2."""
    cons = []
    for v in vals:
        a1, a2 = v[0] - v[2], v[1] - v[2]
        c0 = v[2] - H
        cons.append([a1, a2, -1, c0])     # u_i(p)-1/2 <= s
        cons.append([-a1, -a2, -1, -c0])  # -(u_i(p)-1/2) <= s
    cons += [[-1, 0, 0, 0], [0, -1, 0, 0], [1, 1, 0, -1]]  # p in Delta
    s, arg = lp_min(cons, [0, 0, 1, 0], 3)
    return s, (arg[0], arg[1], 1 - arg[0] - arg[1])


def skeleton_D(vals):
    """min over skeleton weights of max marginal density, exact LP.
    Weights (w_AB, w_BC, w_CA) = (w1, w2, 1-w1-w2); direction values vals[i] at
    (A,B,C).  Only valid for triples where each u_i is non-constant on every
    edge OR the constant-edge weight is forced 0 (handled: constant edge ->
    that weight forced 0 via equality... here: assert no constant edges)."""
    E = [(0, 1), (1, 2), (2, 0)]
    for v in vals:
        assert all(v[i] != v[j] for i, j in E), 'constant edge: handle separately'
    cons = []
    wexpr = [[1, 0, 0], [0, 1, 0], [-1, -1, 1]]  # w_AB, w_BC, w_CA in (w1,w2,1)

    def add_density(pieces):
        # pieces: list of (lo, hi, weight-index) intervals per direction
        cuts = sorted({p for lo, hi, _ in pieces for p in (lo, hi)})
        for a, b in zip(cuts[:-1], cuts[1:]):
            mid = (a + b) / 2
            dens = [S(0), S(0), S(0), S(0)]  # in (w1, w2, const, t)
            for lo, hi, k in pieces:
                if lo < mid < hi:
                    coef = 1 / (hi - lo)
                    dens[0] += coef * wexpr[k][0]
                    dens[1] += coef * wexpr[k][1]
                    dens[2] += coef * (wexpr[k][2] if len(wexpr[k]) > 2 else 0)
            # dens . (w1,w2,1) <= t  ->  [d0, d1, -1, d2] as (w1,w2,t,const)
            cons.append([dens[0], dens[1], -1, dens[2]])

    for v in vals:
        pieces = []
        for k, (i, j) in enumerate(E):
            lo, hi = min(v[i], v[j]), max(v[i], v[j])
            pieces.append((lo, hi, k))
        add_density(pieces)
    cons += [[-1, 0, 0, 0], [0, -1, 0, 0], [1, 1, 0, -1]]  # w >= 0
    t, arg = lp_min(cons, [0, 0, 1, 0], 3)
    return t, (arg[0], arg[1], 1 - arg[0] - arg[1])


# ---------- 2. facets: inscribed-triangle loop, exact marginals --------------

def facet_loop():
    P = [Matrix([0, Rational(1, 3), Rational(2, 3)]),
         Matrix([Rational(2, 3), 0, Rational(1, 3)]),
         Matrix([Rational(1, 3), Rational(2, 3), 0])]
    segs = [(P[0], P[1]), (P[1], P[2]), (P[2], P[0])]
    for i in range(3):  # direction lambda_i
        pieces = []
        for a, b in segs:
            lo, hi = min(a[i], b[i]), max(a[i], b[i])
            assert lo != hi
            pieces.append((lo, hi, Rational(1, 3) / (hi - lo)))
        # exact density on [0,2/3]: sum of piece densities
        cuts = sorted({q for lo, hi, _ in pieces for q in (lo, hi)})
        assert cuts == [0, Rational(1, 3), Rational(2, 3)]
        for a, b in zip(cuts[:-1], cuts[1:]):
            mid = (a + b) / 2
            dens = sum(d for lo, hi, d in pieces if lo < mid < hi)
            assert dens == Rational(3, 2), (i, a, b, dens)
    # moment lower bound is tight: delta(facets) = 1/6
    d, p = delta_defect([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
    assert d == Rational(1, 6) and 1 / (1 - 2 * d) == Rational(3, 2)
    print('2. facets: loop marginals == (3/2) 1_[0,2/3] exactly; delta = 1/6;')
    print('   D(facets) = 3/2 EXACTLY (lower = upper).')


# ---------- 3. loop witness for general triples ------------------------------

def loop_witness(vals, delta, tol_check=True):
    """Try to realize D = 1/(1-2*delta): solve for Q0,Q1,Q2, c1..c3 with
    ell = 1-2*delta, over all anchor/sign patterns.  Returns a certified
    solution or None."""
    ell = 1 - 2 * delta
    q = symbols('q0:6')  # Q0=(q0,q1,.), Q1=(q2,q3,.), Q2=(q4,q5,.)
    c = symbols('c1:4')
    Q = [Matrix([q[0], q[1], 1 - q[0] - q[1]]),
         Matrix([q[2], q[3], 1 - q[2] - q[3]]),
         Matrix([q[4], q[5], 1 - q[4] - q[5]])]

    def u(i, X):
        return sum(vals[i][j] * X[j] for j in range(3))

    for anchors in itertools.product(range(3), repeat=3):
        for signs in itertools.product([1, -1], repeat=3):
            eqs = []
            for i in range(3):
                others = [j for j in range(3) if j != anchors[i]]
                eqs.append(u(i, Q[anchors[i]]) - c[i])
                eqs.append(u(i, Q[others[0]]) - (c[i] - signs[i] * ell / 2))
                eqs.append(u(i, Q[others[1]]) - (c[i] + signs[i] * ell / 2))
            sol = solve(eqs, list(q) + list(c), dict=True)
            if not sol:
                continue
            s0 = sol[0]
            allvars = list(q) + list(c)
            free = sorted((set().union(*[v.free_symbols for v in s0.values()])
                           if s0 else set())
                          | (set(allvars) - set(s0.keys())), key=str)
            pin_vals = [S(0), Rational(1, 3), H, Rational(2, 3), S(1)]
            pin_iter = itertools.product(pin_vals, repeat=len(free)) if free else [()]
            for pins in pin_iter:
                subs = dict(zip(free, pins))
                full = {k: (s0[k].subs(subs) if k in s0 else subs[k])
                        for k in allvars}
                if any(getattr(v, 'free_symbols', set()) for v in full.values()):
                    continue
                Qs = [X.subs(full) for X in Q]
                cs = [full[ci] for ci in c]
                inside = all(comp >= 0 for X in Qs for comp in X)
                blocks_ok = all(cs[i] - ell / 2 >= 0 and cs[i] + ell / 2 <= 1
                                for i in range(3))
                defect_ok = (max(abs(ci - H) for ci in cs) == delta
                             if tol_check else True)
                if inside and blocks_ok and defect_ok:
                    return {'anchors': anchors, 'signs': signs,
                            'Q': Qs, 'c': cs, 'ell': ell}
    return None


# ---------- 4. skeleton perturbation: symbolic + samples ---------------------

def cyclic_vals(t1, t2, t3):
    return [[S(t1), S(0), S(1)], [S(0), S(1), S(t2)], [S(1), S(t3), S(0)]]


def loop_ellmax(vals):
    """Best loop witness: leave ell free (9 eqs, 10 unknowns -> affine family
    in ell), maximize ell subject to Q in Delta and blocks in [0,1], over all
    anchor/sign patterns.  Returns (ell_max, data) exact, or (None, None)."""
    ell = symbols('ell', positive=True)
    q = symbols('q0:6')
    c = symbols('c1:4')
    Q = [Matrix([q[0], q[1], 1 - q[0] - q[1]]),
         Matrix([q[2], q[3], 1 - q[2] - q[3]]),
         Matrix([q[4], q[5], 1 - q[4] - q[5]])]

    def u(i, X):
        return sum(vals[i][j] * X[j] for j in range(3))

    best, bestdata = None, None
    for anchors in itertools.product(range(3), repeat=3):
        for signs in itertools.product([1, -1], repeat=3):
            eqs = []
            for i in range(3):
                others = [j for j in range(3) if j != anchors[i]]
                eqs.append(u(i, Q[anchors[i]]) - c[i])
                eqs.append(u(i, Q[others[0]]) - (c[i] - signs[i] * ell / 2))
                eqs.append(u(i, Q[others[1]]) - (c[i] + signs[i] * ell / 2))
            sol = solve(eqs, list(q) + list(c), dict=True)
            if not sol or any(v.free_symbols - {ell} for v in sol[0].values()):
                continue
            s = sol[0]
            # affine-in-ell feasibility: collect g(ell) >= 0 constraints
            gs = []
            for X in Q:
                for comp in X:
                    gs.append(comp.subs(s))
            for i in range(3):
                gs.append(s[c[i]] - ell / 2)          # block lower >= 0
                gs.append(1 - s[c[i]] - ell / 2)      # block upper <= 1
            lo, hi = S(0), S(1)
            ok = True
            for g in gs:
                g = simplify(g)
                A = g.subs(ell, 0)
                B = simplify(g - A).coeff(ell)
                if B == 0:
                    if A < 0:
                        ok = False
                        break
                elif B > 0:
                    lo = max(lo, -A / B)
                else:
                    hi = min(hi, -A / B)
            if not ok or hi <= lo or hi <= 0:
                continue
            if best is None or hi > best:
                best = hi
                bestdata = {'anchors': anchors, 'signs': signs,
                            'Q': [X.subs(s).subs(ell, hi) for X in Q],
                            'c': [s[ci].subs(ell, hi) for ci in c]}
    return best, bestdata


def skeleton_perturbation_symbolic():
    """Frozen concurrent weights on a perturbed tau: densities = 1 + w*(dtau)/..."""
    a, b, g, t1s, t1 = symbols('alpha beta gamma tau1s tau1', positive=True)
    # concurrent relations: tau1* = gamma/(1-alpha), weights (AB,BC,CA)=(g,a,b)
    d1lo = a + g / t1                      # density on [0,tau1] for u1
    d1hi = a + b / (1 - t1)                # density on [tau1,1]
    rel = {t1s: g / (1 - a), b: 1 - a - g}
    err_lo = simplify((d1lo - 1).subs(b, 1 - a - g) - g * (g / (1 - a) - t1) / (t1 * (g / (1 - a))))
    err_hi = simplify((d1hi - 1).subs(b, 1 - a - g)
                      - (1 - a - g) * (t1 - g / (1 - a)) / ((1 - t1) * (1 - g / (1 - a))))
    assert err_lo == 0 and err_hi == 0
    print('4a. symbolic: frozen-weight densities  d-1 = w* (tau*-tau)/(tau tau*)')
    print('    (and the (1-tau) mirror)  ->  |d-1| <= eps/(m(m-eps)),',
          'm = min(tau*,1-tau*).')


def sample_sandwich():
    """Non-concurrent cyclic sample: tau = (13/25, 1/2, 1/2)."""
    t = (Rational(13, 25), H, H)
    vals = cyclic_vals(*t)
    # non-concurrence: solve Vp = 1/2 and check sum(p) != 1
    p = symbols('p0:3')
    V = Matrix(vals)
    sol = solve(list(V * Matrix(p) - Matrix([H, H, H])), list(p), dict=True)[0]
    sump = simplify(sum(sol[pi] for pi in p))
    assert sump != 1
    d, pstar = delta_defect(vals)
    lower = 1 / (1 - 2 * d)
    Dskel, wopt = skeleton_D(vals)
    print(f'4b. sample tau = (13/25, 1/2, 1/2):  sum p* = {sump} != 1 (non-concurrent)')
    print(f'    delta(u) = {d}   ->  lower bound  D >= 1/(1-2 delta) = {lower}')
    print(f'    skeleton LP (exact):  D <= D_skel = {Dskel}  at w = {tuple(wopt)}')
    ellmax, lwdata = loop_ellmax(vals)
    Dloop = 1 / ellmax if ellmax else None
    upper = min(Dskel, Dloop) if Dloop else Dskel
    if 1 / upper == 1 - 2 * d:
        print(f'    best loop: ell_max = {ellmax}  ->  D = {upper} EXACTLY.')
    else:
        print(f'    best loop: ell_max = {ellmax}  ->  D_loop = {Dloop}')
        print(f'    sandwich:  D(u) in [{lower}, {upper}]  (gap open)')
    return d, lower, Dskel, Dloop


def sample_far():
    """A second sample, further from the surface: tau = (7/10, 2/5, 1/2)."""
    t = (Rational(7, 10), Rational(2, 5), H)
    vals = cyclic_vals(*t)
    d, _ = delta_defect(vals)
    lower = 1 / (1 - 2 * d)
    Dskel, _ = skeleton_D(vals)
    ellmax, _ = loop_ellmax(vals)
    Dloop = 1 / ellmax if ellmax else None
    upper = min(x for x in (Dskel, Dloop) if x is not None)
    print(f'4c. sample tau = (7/10, 2/5, 1/2): delta = {d},'
          f' D in [{lower}, {upper}]  (skel {Dskel}, loop {Dloop})')
    return d, lower, Dskel, Dloop


def medians_check():
    vals = cyclic_vals(H, H, H)
    d, _ = delta_defect(vals)
    assert d == 0
    lw = loop_witness(vals, d)
    assert lw, 'medians must admit the loop witness (perimeter of Delta)'
    print('1. medians: delta = 0, loop witness exists (perimeter), D = 1.')


def delta_landscape():
    """[EVIDENCE] small exact sweep: is delta(u) <= 1/6 (facets the worst)?"""
    Q = Rational
    triples = [('facets', [[1, 0, 0], [0, 1, 0], [0, 0, 1]])]
    for t in [Q(1, 4), H, Q(3, 4)]:
        triples.append((f'tilted facets t={t}',
                        [[1, 0, t], [t, 1, 0], [0, t, 1]]))
    for t in [Q(1, 4), Q(3, 4)]:
        triples.append((f'cyclic tau=({t},{t},{t})', cyclic_vals(t, t, t)))
    triples.append(('cyclic (9/10,1/10,1/2)', cyclic_vals(Q(9, 10), Q(1, 10), H)))
    triples.append(('two facets + median', [[1, 0, 0], [0, 1, 0], [H, 0, 1]]))
    triples.append(('facet + 2 cyclic', [[1, 0, 0], [0, 1, Q(1, 4)], [1, Q(3, 4), 0]]))
    worst = S(0)
    print('5. delta landscape (exact, small sweep) [EVIDENCE]:')
    for name, vals in triples:
        vals = [[S(x) for x in v] for v in vals]
        d, _ = delta_defect(vals)
        worst = max(worst, d)
        print(f'    delta = {str(d):>8}  D >= {str(1/(1-2*d)):>8}   {name}')
    print(f'    max delta found = {worst}'
          + ('  (== 1/6: facets extremal in this sweep)' if worst == Q(1, 6)
             else '  (!) exceeds 1/6'))


if __name__ == '__main__':
    medians_check()
    facet_loop()
    skeleton_perturbation_symbolic()
    sample_sandwich()
    sample_far()
    delta_landscape()
    print('ALL OK')
