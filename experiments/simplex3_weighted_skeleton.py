#!/usr/bin/env python3
"""R7-1: weighted 1-skeleton witness measures on the 3-simplex (and d>=4 obstruction).

Question (auditorias/51 SR7-1 / auditorias/52 R7-1): does the unequal-edge-mass
mechanism of Thm 6.3 extend to Delta^d, d>=3?  Exact linear algebra over Q / Q(sigma).

Setup.  Delta^3 = conv(e1..e4).  A normalized direction u is given by its vertex
values (min 0, max 1 attained).  A skeleton measure is sum_e w_e * (uniform in the
parameter on edge e), w_e >= 0, sum w_e = 1.  Pushforward of the edge {j,k} piece
under u: uniform on [u_j, u_k] with density w_e/|u_k - u_j| if u_j != u_k, and an
ATOM of mass w_e at the common value if u_j = u_k (an atom is incompatible with a
uniform marginal unless w_e = 0).

Families tested (all with mid-hyperplanes {u_i = 1/2} concurrent at the centroid):
 (A) literal notes/47 cyclic medians: m_i(e_i)=1/2, m_i(e_{i+1})=0, m_i(e_{i-1})=1,
     rest 1/2.  In d=3 this family is DEGENERATE: m_3 = 1 - m_1, m_4 = 1 - m_2
     (flip pairs; only two directions up to flip).  Skeleton system still solvable:
     a 1-parameter family of witnesses.
 (B) non-degenerate cyclic medians: u_i(e_i)=0, u_i(e_{i+1})=1, rest 1/2
     (4 pairwise non-parallel directions).  Verdict: UNIQUE skeleton witness
     w_{13} = w_{24} = 1/2, all other edges forced to 0 by the atom constraint.
 (C) cyclic sigma-family: u_i(e_i)=0, u_i(e_{i+1})=1, u_i(e_{i+2})=sigma,
     u_i(e_{i+3})=1-sigma, sigma in (0,1).  (sigma=1/2 is (B).)  Verdict: for EVERY
     sigma a skeleton witness exists, with closed forms
        a(s) = (1-s)(1-2s) / (2(s^2-4s+2))   on the four cycle edges {i,i+1},
        b(s) = s(2-3s)     / (2(s^2-4s+2))   on the two diagonals {13},{24},
     (0<s<1/2; s>1/2 by the reflection symmetry), all weights > 0, and the solution
     is the UNIQUE skeleton witness.  Concurrence of the four mid-planes for the
     general cyclic family u_i = (0,1,sigma,rho) forces rho = 1-sigma and p = centroid
     (circulant argument), also verified here.
 (D) d >= 4 obstruction: for the cyclic medians of Delta^d (values 0,1 at e_i,e_{i+1},
     rest 1/2), EVERY edge {j,k} of Delta^d is constant for some direction, hence
     every skeleton measure is forced to 0 on every edge: no 1-skeleton witness
     exists for d >= 4.  (Mass must move to 2-faces; open.)  Verified d = 4..7.

Everything exact (sympy Rationals / symbolic sigma).  Run: python3 <file>.
"""

import itertools
from sympy import Rational, symbols, simplify, linsolve, Matrix, factor, S, solve

H = Rational(1, 2)


# ---------- generic machinery ----------------------------------------------

def edge_list(n):
    return [frozenset(e) for e in itertools.combinations(range(n), 2)]


def marginal_conditions(vertex_vals, n):
    """Exact conditions for: sum of edge pushforwards has density 1 on [0,1]
    for every direction.  vertex_vals[i][j] = u_i(e_j).
    Returns (linear equations in w_e, forced-zero edges from atoms)."""
    edges = edge_list(n)
    w = symbols(f'w0:{len(edges)}', nonnegative=True)
    widx = {e: w[k] for k, e in enumerate(edges)}
    eqs, forced_zero = [], set()
    for vals in vertex_vals:
        # breakpoints of the piecewise-constant marginal
        bps = sorted(set(vals) | {S(0), S(1)})
        for e in edges:
            j, k = sorted(e)
            if simplify(vals[j] - vals[k]) == 0:
                forced_zero.add(e)                      # atom -> weight 0
        for lo, hi in zip(bps[:-1], bps[1:]):
            mid = (lo + hi) / 2
            dens = S(0)
            for e in edges:
                j, k = sorted(e)
                a, b = vals[j], vals[k]
                if simplify(a - b) == 0:
                    continue
                lo_e, hi_e = min(a, b), max(a, b)
                if simplify(lo_e - mid) < 0 and simplify(mid - hi_e) < 0:
                    dens += widx[e] / (hi_e - lo_e)
            eqs.append(simplify(dens - 1))
    for e in forced_zero:
        eqs.append(widx[e])
    return w, edges, eqs


def solve_family(name, vertex_vals, n=4):
    w, edges, eqs = marginal_conditions(vertex_vals, n)
    sol = linsolve(eqs, list(w))
    print(f'--- family {name}: solution set (w order {[tuple(sorted(e)) for e in edges]})')
    print('   ', sol)
    return w, edges, sol


# ---------- (A) literal notes/47 medians ------------------------------------

def family_A():
    vals = []
    for i in range(4):
        v = [H] * 4
        v[(i + 1) % 4] = S(0)
        v[(i - 1) % 4] = S(1)
        vals.append(v)
    # degeneracy check: m3 = 1 - m1, m4 = 1 - m2
    assert all(simplify(vals[2][j] - (1 - vals[0][j])) == 0 for j in range(4))
    assert all(simplify(vals[3][j] - (1 - vals[1][j])) == 0 for j in range(4))
    print('(A) degenerate: m3 = 1-m1, m4 = 1-m2  [flip pairs, 2 effective directions]')
    w, edges, sol = solve_family('A (literal notes/47)', vals)
    # expect a 1-parameter family; check the t=1/4 point: uniform on the 4-cycle
    (expr,) = sol
    subs_pt = {s: Rational(1, 4) for s in expr.free_symbols}
    pt = [x.subs(subs_pt) for x in expr]
    print('    sample witness (free param = 1/4):',
          {tuple(sorted(e)): v for e, v in zip(edges, pt) if v != 0})
    assert all(v >= 0 for v in pt) and sum(pt) == 1


# ---------- (B)/(C) non-degenerate cyclic family -----------------------------

def cyclic_vals(sigma):
    vals = []
    for i in range(4):
        v = [None] * 4
        v[i] = S(0)
        v[(i + 1) % 4] = S(1)
        v[(i + 2) % 4] = sigma
        v[(i + 3) % 4] = 1 - sigma
        vals.append(v)
    return vals


def pairwise_nonparallel(vals):
    """u_i, u_j parallel iff vertex-value vectors are affinely related."""
    for i in range(4):
        for j in range(i + 1, 4):
            vi, vj = Matrix(vals[i]), Matrix(vals[j])
            M = Matrix.hstack(vi, vj, Matrix([1] * 4))
            if M.rank() < 3:
                return False, (i, j)
    return True, None


def family_B():
    vals = cyclic_vals(H)
    ok, bad = pairwise_nonparallel(vals)
    assert ok, f'parallel pair {bad}'
    print('(B) medians sigma=1/2: pairwise non-parallel OK')
    w, edges, sol = solve_family('B (cyclic medians)', vals)
    (expr,) = sol
    assert not expr.free_symbols, 'expected UNIQUE solution'
    got = {tuple(sorted(e)): v for e, v in zip(edges, expr)}
    assert got == {(0, 2): H, (1, 3): H, (0, 1): 0, (0, 3): 0, (1, 2): 0, (2, 3): 0}
    print('    UNIQUE witness: w_{13} = w_{24} = 1/2, all other edges 0 (atoms)')


def family_C():
    s = symbols('sigma', positive=True)
    vals = cyclic_vals(s)
    ok, bad = pairwise_nonparallel(vals)
    assert ok, f'parallel pair {bad}'
    # exact conditions on the strip 0 < s < 1/2 (piece order fixed there)
    edges = edge_list(4)
    w = symbols('w0:6', nonnegative=True)
    widx = {e: w[k] for k, e in enumerate(edges)}
    eqs = []
    for vals_i in vals:
        bps = [S(0), s, 1 - s, S(1)]
        for lo, hi in zip(bps[:-1], bps[1:]):
            dens = S(0)
            for e in edges:
                j, k = sorted(e)
                a, b = vals_i[j], vals_i[k]
                lo_e, hi_e = min(a, b, key=lambda x: x.subs(s, Rational(1, 4))), \
                             max(a, b, key=lambda x: x.subs(s, Rational(1, 4)))
                # containment decided symbolically on 0<s<1/2
                left = simplify(lo_e - lo)
                right = simplify(hi - hi_e)
                if left.subs(s, Rational(1, 4)) <= 0 and right.subs(s, Rational(1, 4)) <= 0:
                    dens += widx[e] / (hi_e - lo_e)
            eqs.append(simplify(dens - 1))
    sol = linsolve(eqs, list(w))
    (expr,) = sol
    assert not expr.free_symbols - {s}, 'expected unique solution for generic sigma'
    a_pred = (1 - s) * (1 - 2 * s) / (2 * (s ** 2 - 4 * s + 2))
    b_pred = s * (2 - 3 * s) / (2 * (s ** 2 - 4 * s + 2))
    got = {tuple(sorted(e)): factor(simplify(v)) for e, v in zip(edges, expr)}
    for e in [(0, 1), (1, 2), (2, 3), (0, 3)]:
        assert simplify(got[e] - a_pred) == 0, (e, got[e])
    for e in [(0, 2), (1, 3)]:
        assert simplify(got[e] - b_pred) == 0, (e, got[e])
    assert simplify(4 * a_pred + 2 * b_pred - 1) == 0
    print('(C) sigma-family, 0<sigma<1/2: UNIQUE skeleton witness, closed forms')
    print('    cycle edges  a(s) =', factor(a_pred))
    print('    diagonals    b(s) =', factor(b_pred))
    # positivity on (0,1/2): s^2-4s+2 has roots 2+-sqrt2, positive on (0, 0.58..)
    for sval in [Rational(1, 100), Rational(1, 4), Rational(49, 100)]:
        av, bv = a_pred.subs(s, sval), b_pred.subs(s, sval)
        assert av > 0 and bv > 0, sval
    print('    positivity spot-checked exactly at s = 1/100, 1/4, 49/100')
    # sanity at sigma=1/2: a -> 0, b -> 1/2 (family B)
    assert a_pred.subs(s, H) == 0 and b_pred.subs(s, H) == H
    # necessity: general cyclic (sigma,rho) concur iff rho = 1-sigma, p = centroid
    rho = symbols('rho', positive=True)
    vals2 = []
    for i in range(4):
        v = [None] * 4
        v[i], v[(i + 1) % 4], v[(i + 2) % 4], v[(i + 3) % 4] = S(0), S(1), s, rho
        vals2.append(v)
    V = Matrix(vals2)
    p = Matrix(symbols('p0:4'))
    system = list(V * p - Matrix([H] * 4)) + [sum(p) - 1]
    con = solve(system, list(p) + [rho], dict=True)
    assert len(con) == 1 and simplify(con[0][rho] - (1 - s)) == 0
    assert all(simplify(con[0][pi] - Rational(1, 4)) == 0 for pi in p)
    print('    concurrence for cyclic (sigma,rho) forces rho = 1-sigma, p = centroid')


# ---------- (D) d>=4: every edge killed --------------------------------------

def family_D():
    for d in range(4, 8):
        n = d + 1
        killed = set()
        for i in range(n):
            half = set(range(n)) - {i, (i + 1) % n}
            for e in itertools.combinations(sorted(half), 2):
                killed.add(frozenset(e))
        allE = set(edge_list(n))
        assert killed == allE, (d, allE - killed)
        print(f'(D) d={d}: all {len(allE)} edges constant for some direction '
              f'-> no 1-skeleton witness')


if __name__ == '__main__':
    family_A()
    family_B()
    family_C()
    family_D()
    print('ALL OK')
