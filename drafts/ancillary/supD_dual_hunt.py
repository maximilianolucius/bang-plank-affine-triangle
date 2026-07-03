#!/usr/bin/env python3
"""
supD_dual_hunt.py -- R10-1 Route A: certified multi-knot dual lower bounds for
D(u), and skeleton upper bounds, hunting for (alpha) D > 3/2 and (beta) any
D > moment bound 1/(1-2*delta).

METHOD (per auditorias/58): psi_i piecewise linear on rational knots; the
function sum_i psi_i(u_i(x)) is piecewise AFFINE on the cell complex cut by the
level lines {u_i = knot}, so its minimum over Delta is attained at a vertex of
the complex (pairwise intersections of level lines and their crossings with
the edges of Delta, plus the corners) -- all exact rationals.  A float LP
(scipy) only GUIDES the search for good psi; the reported bound is re-derived
EXACTLY in fractions: rationalize psi, rescale to total integral exactly 1,
take the exact minimum over all complex vertices.  By weak duality
(Thm 7.6 of the paper) any admissible psi certifies a rigorous lower bound --
there is no grid on the dual side that can lie.

Upper bounds: (a) uniform-per-edge skeleton LP, exact by vertex enumeration
(3 weight variables); (b) piecewise-constant edge densities, float-guided and
then certified exactly (any admissible measure certifies an upper bound).

Everything reported as 'CERTIFIED' below is exact rational arithmetic.
"""

import itertools
from fractions import Fraction as F
from bisect import bisect_right

import numpy as np
from scipy.optimize import linprog

# ----------------------------------------------------------------------
# exact linear algebra (fractions)
# ----------------------------------------------------------------------

def solve3(M, b):
    """Solve 3x3 exact; M rows of Fractions. Returns None if singular."""
    a, bb, c = M[0], M[1], M[2]
    det = (a[0]*(bb[1]*c[2]-bb[2]*c[1]) - a[1]*(bb[0]*c[2]-bb[2]*c[0])
           + a[2]*(bb[0]*c[1]-bb[1]*c[0]))
    if det == 0:
        return None
    x = []
    for k in range(3):
        Mk = [row[:] for row in M]
        for r in range(3):
            Mk[r][k] = b[r]
        a2, b2, c2 = Mk
        dk = (a2[0]*(b2[1]*c2[2]-b2[2]*c2[1]) - a2[1]*(b2[0]*c2[2]-b2[2]*c2[0])
              + a2[2]*(b2[0]*c2[1]-b2[1]*c2[0]))
        x.append(F(dk, 1) / det)
    return x


def uval(v, lam):
    return v[0]*lam[0] + v[1]*lam[1] + v[2]*lam[2]


def cross(a, b):
    return [a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0]]


def dependency(V):
    """(c, c0) with sum c_i u_i == c0 on the plane.  Normalized c0=1 when
    possible; degenerate families (all u_i vanishing at a common point of the
    plane) have a homogeneous dependency c0=0, found via the kernel."""
    M = [[V[i][j] for i in range(3)] for j in range(3)]  # rows: vertices
    c = solve3(M, [F(1), F(1), F(1)])
    if c is not None:
        return c, F(1)
    for r1, r2 in ((0, 1), (0, 2), (1, 2)):
        k = cross(M[r1], M[r2])
        if any(x != 0 for x in k):
            assert all(sum(M[j][i]*k[i] for i in range(3)) == 0
                       for j in range(3)), "rank defect inconsistent"
            return [F(x) for x in k], F(0)
    raise AssertionError("pairwise parallel directions?")


def delta_c(V):
    c, c0 = dependency(V)
    A = sum(abs(x) for x in c)
    return abs(c0 - sum(c) / 2) / A


def moment_bound(V):
    d = delta_c(V)          # = delta(u) by the R10-2 theorem; certified lower
    return 1 / (1 - 2 * d)


def delta_exact(V):
    """Exact delta(u) by vertex enumeration (variables lam1, lam2, z)."""
    cons = []  # a.x <= b  with x=(l1,l2,z)
    for v in V:
        a1, a2 = v[0]-v[2], v[1]-v[2]
        cons.append(([a1, a2, F(-1)], F(1, 2) - v[2]))
        cons.append(([-a1, -a2, F(-1)], v[2] - F(1, 2)))
    cons += [([F(-1), F(0), F(0)], F(0)), ([F(0), F(-1), F(0)], F(0)),
             ([F(1), F(1), F(0)], F(1))]
    best = None
    for idx in itertools.combinations(range(len(cons)), 3):
        M = [list(cons[i][0]) for i in idx]
        x = solve3(M, [cons[i][1] for i in idx])
        if x is None:
            continue
        if all(sum(a*xx for a, xx in zip(cc[0], x)) <= cc[1] for cc in cons):
            if best is None or x[2] < best:
                best = x[2]
    return best


# ----------------------------------------------------------------------
# multi-knot dual: certified lower bound
# ----------------------------------------------------------------------

CORNERS = [(F(1), F(0), F(0)), (F(0), F(1), F(0)), (F(0), F(0), F(1))]

def complex_vertices(V, knots):
    """All vertices of the arrangement {u_i = k} inside Delta (exact)."""
    pts = set(CORNERS)
    # level line  u_i = t  <->  (v0-v2) l1 + (v1-v2) l2 = t - v2  (l3=1-l1-l2)
    def line(i, t):
        v = V[i]
        return ([v[0]-v[2], v[1]-v[2]], t - v[2])
    # pairwise intersections
    for i, j in itertools.combinations(range(3), 2):
        for ti in knots[i]:
            Li = line(i, ti)
            for tj in knots[j]:
                Lj = line(j, tj)
                M = [[Li[0][0], Li[0][1], F(0)],
                     [Lj[0][0], Lj[0][1], F(0)],
                     [F(0), F(0), F(1)]]
                x = solve3(M, [Li[1], Lj[1], F(0)])
                if x is None:
                    continue
                l1, l2 = x[0], x[1]
                l3 = 1 - l1 - l2
                if l1 >= 0 and l2 >= 0 and l3 >= 0:
                    pts.add((l1, l2, l3))
    # crossings with the three edges
    edges = [(CORNERS[0], CORNERS[1]), (CORNERS[1], CORNERS[2]),
             (CORNERS[2], CORNERS[0])]
    for i in range(3):
        v = V[i]
        for t in knots[i]:
            for P, Q in edges:
                a, b = uval(v, P), uval(v, Q)
                if a == b:
                    continue
                s = (t - a) / (b - a)
                if 0 <= s <= 1:
                    pts.add(tuple(P[k] + s*(Q[k]-P[k]) for k in range(3)))
    return sorted(pts)


def interp_coeffs(knots_i, t):
    """psi(t) as linear combination of knot values: [(index, coeff), ...]."""
    ks = knots_i
    if t <= ks[0]:
        return [(0, F(1))]
    if t >= ks[-1]:
        return [(len(ks)-1, F(1))]
    r = bisect_right(ks, t) - 1
    if ks[r] == t:
        return [(r, F(1))]
    h = ks[r+1] - ks[r]
    w = (t - ks[r]) / h
    return [(r, 1-w), (r+1, w)]


def dual_bound(V, q, extra=(), verbose=False):
    """Certified lower bound on D(V) from piecewise-linear psi with knots
    {0,1/q,...,1} union extra (per direction, same set).  Exact result."""
    base = sorted(set([F(k, q) for k in range(q+1)] + [F(e) for e in extra]))
    knots = [base, base, base]
    offs = [0, len(base), 2*len(base)]
    nv = 3*len(base)
    verts = complex_vertices(V, knots)
    # rows of the vertex constraints: sum_i psi_i(u_i(x)) >= B
    rows = []
    for lam in verts:
        row = {}
        for i in range(3):
            t = uval(V[i], lam)
            for idx, cf in interp_coeffs(knots[i], t):
                row[offs[i]+idx] = row.get(offs[i]+idx, F(0)) + cf
        rows.append(row)
    # trapezoid weights for the mass
    mass_w = [F(0)]*nv
    for i in range(3):
        ks = knots[i]
        for r in range(len(ks)-1):
            h = ks[r+1]-ks[r]
            mass_w[offs[i]+r] += h/2
            mass_w[offs[i]+r+1] += h/2
    # float LP: max B  s.t.  B - row.y <= 0 ; mass.y = 1 ; y >= 0
    A_ub = np.zeros((len(rows), nv+1))
    for rix, row in enumerate(rows):
        for k, cf in row.items():
            A_ub[rix, k] = -float(cf)
        A_ub[rix, nv] = 1.0
    b_ub = np.zeros(len(rows))
    A_eq = np.zeros((1, nv+1)); A_eq[0, :nv] = [float(x) for x in mass_w]
    b_eq = [1.0]
    cobj = np.zeros(nv+1); cobj[nv] = -1.0
    bounds = [(0, None)]*nv + [(None, None)]
    res = linprog(cobj, A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=b_eq,
                  bounds=bounds, method='highs')
    if not res.success:
        return None, None
    # exactify: rationalize psi, rescale mass to exactly 1, certify exactly
    y = [max(F(0), F(float(v)).limit_denominator(10**8)) for v in res.x[:nv]]
    mass = sum(w*yy for w, yy in zip(mass_w, y))
    if mass <= 0:
        return None, None
    y = [yy/mass for yy in y]
    B_cert = min(sum(cf*y[k] for k, cf in row.items()) for row in rows)
    if verbose:
        print(f"    dual LP: {len(verts)} vertices, {nv} vars, "
              f"float opt {-res.fun:.6f}, certified {B_cert} "
              f"= {float(B_cert):.6f}")
    return B_cert, y


# ----------------------------------------------------------------------
# skeleton upper bounds
# ----------------------------------------------------------------------

def skeleton_uniform_UB(V):
    """Exact min over uniform-per-edge weights of the max marginal density.
    Variables (w_AB, w_BC, t); w_CA = 1-w_AB-w_BC.  Vertex enumeration."""
    E = [(0, 1), (1, 2), (2, 0)]
    for v in V:
        if any(v[i] == v[j] for i, j in E):
            return None  # constant edge: skeleton infeasible (atom)
    wexpr = [[1, 0, 0], [0, 1, 0], [-1, -1, 1]]   # in (w1, w2, 1)
    cons = []
    for v in V:
        pieces = [(min(v[i], v[j]), max(v[i], v[j]), k)
                  for k, (i, j) in enumerate(E)]
        cuts = sorted({p for lo, hi, _ in pieces for p in (lo, hi)})
        for a, b in zip(cuts[:-1], cuts[1:]):
            mid = (a+b)/2
            d = [F(0), F(0), F(0)]
            for lo, hi, k in pieces:
                if lo < mid < hi:
                    cf = 1/(hi-lo)
                    for m in range(3):
                        d[m] += cf*wexpr[k][m]
            cons.append(([d[0], d[1], F(-1)], -d[2]))    # dens <= t
    cons += [([F(-1), F(0), F(0)], F(0)), ([F(0), F(-1), F(0)], F(0)),
             ([F(1), F(1), F(0)], F(1))]
    best = None
    for idx in itertools.combinations(range(len(cons)), 3):
        M = [list(cons[i][0]) for i in idx]
        x = solve3(M, [cons[i][1] for i in idx])
        if x is None:
            continue
        if all(sum(a*xx for a, xx in zip(cc[0], x)) <= cc[1] for cc in cons):
            if best is None or x[2] < best:
                best = x[2]
    return best


def skeleton_pw_UB(V, q):
    """Certified upper bound from piecewise-constant edge densities on a
    uniform parameter grid with q pieces per edge (float-guided, exact
    certification: rationalize, rescale mass, take exact sup of densities)."""
    E = [(0, 1), (1, 2), (2, 0)]
    for v in V:
        if any(v[i] == v[j] for i, j in E):
            return None
    grid = [F(k, q) for k in range(q+1)]
    nv = 3*q
    # marginal value-cuts per direction: images of grid nodes under each edge map
    cons_rows = []   # density of marginal i on elementary interval: linear in d
    for i in range(3):
        vals = set()
        for e, (aa, bb) in enumerate(E):
            va, vb = V[i][aa], V[i][bb]
            for g in grid:
                vals.add(va + g*(vb-va))
        vals = sorted(vals)
        for lo, hi in zip(vals[:-1], vals[1:]):
            mid = (lo+hi)/2
            row = {}
            for e, (aa, bb) in enumerate(E):
                va, vb = V[i][aa], V[i][bb]
                if va == vb:
                    continue
                s = (mid - va)/(vb - va)   # parameter with u_i = mid
                if 0 <= s <= 1:
                    r = min(q-1, int(s*q))
                    row[e*q+r] = row.get(e*q+r, F(0)) + abs(1/(vb-va))
            cons_rows.append(row)
    # float LP: min t s.t. row.d <= t; sum d/q = 1; d >= 0
    A_ub = np.zeros((len(cons_rows), nv+1))
    for rix, row in enumerate(cons_rows):
        for k, cf in row.items():
            A_ub[rix, k] = float(cf)
        A_ub[rix, nv] = -1.0
    b_ub = np.zeros(len(cons_rows))
    A_eq = np.zeros((1, nv+1)); A_eq[0, :nv] = 1.0/q
    cobj = np.zeros(nv+1); cobj[nv] = 1.0
    res = linprog(cobj, A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=[1.0],
                  bounds=[(0, None)]*nv + [(None, None)], method='highs')
    if not res.success:
        return None
    d = [max(F(0), F(float(v)).limit_denominator(10**8)) for v in res.x[:nv]]
    mass = sum(dd for dd in d)/q
    if mass <= 0:
        return None
    d = [dd/mass for dd in d]
    ub = max(sum(cf*d[k] for k, cf in row.items()) for row in cons_rows)
    return ub


# ----------------------------------------------------------------------
# triple constructors
# ----------------------------------------------------------------------

def cyclic(t1, t2, t3):
    return [(F(t1), F(0), F(1)), (F(0), F(1), F(t2)), (F(1), F(t3), F(0))]

def class_b(t1, t2, t3):
    """u1,u2 full on AB (values t1,t2 at C), u3 full on BC (t3 at A)."""
    return [(F(0), F(1), F(t1)), (F(0), F(1), F(t2)), (F(t3), F(0), F(1))]

def tilted_facets(e1, e2, e3):
    """facets (1,0,0),(0,1,0),(0,0,1) tilted cyclically by eps at one vertex."""
    return [(F(1), F(e1), F(0)), (F(0), F(1), F(e2)), (F(e3), F(0), F(1))]


def report(name, V, q=12, extra=(), pw=None):
    mb = moment_bound(V)
    lb, _ = dual_bound(V, q, extra)
    ub_u = skeleton_uniform_UB(V)
    ub_p = skeleton_pw_UB(V, pw) if pw else None
    ubs = [u for u in (ub_u, ub_p) if u is not None]
    ub = min(ubs) if ubs else None
    gap = (lb is not None and lb > mb)
    over = (lb is not None and lb > F(3, 2))
    if lb is not None and ub is not None:
        assert lb <= ub, (name, lb, ub)
    print(f"  {name}: moment={mb}={float(mb):.6f}  "
          f"dualLB={lb}={float(lb):.6f}  "
          f"skelUB={ub}={float(ub):.6f}"
          + ("  ** DUAL > MOMENT **" if gap else "")
          + ("  ***** D > 3/2 *****" if over else ""))
    return mb, lb, ub


if __name__ == '__main__':
    print("=== (ii) sandwich tau=(13/25,1/2,1/2): 225/224 <= D <= 112/111 ===")
    Vs = cyclic(F(13, 25), F(1, 2), F(1, 2))
    for q, extra, pw in [(10, (F(13, 25), F(12, 25)), None),
                         (25, (), 25), (50, (), 50)]:
        report(f"sandwich q={q}", Vs, q=q, extra=extra, pw=pw)

    print("=== (i) class (b) 'two shared full edges' sweep (moment first) ===")
    cand = []
    vals = [F(1, 12), F(1, 6), F(1, 3), F(1, 2), F(2, 3), F(5, 6), F(11, 12)]
    for t1 in vals:
        for t2 in vals:
            if t2 <= t1:
                continue
            for t3 in vals:
                V = class_b(t1, t2, t3)
                cand.append((moment_bound(V), t1, t2, t3))
    cand.sort(reverse=True)
    print(f"  {len(cand)} triples; top-5 moment bounds:")
    for mb, t1, t2, t3 in cand[:5]:
        print(f"    ({t1},{t2},{t3}): moment={mb}={float(mb):.6f}")
    print("  duals on the top candidates + spread:")
    hunted = cand[:4] + cand[len(cand)//2:len(cand)//2+2] + cand[-2:]
    for mb, t1, t2, t3 in hunted:
        report(f"clase-b ({t1},{t2},{t3})", class_b(t1, t2, t3), q=12, pw=24)

    print("=== (iii) tilted facets ===")
    for e in [F(1, 2), F(1, 4), F(1, 10)]:
        report(f"tilt eps={e}", tilted_facets(e, e, e), q=12, pw=24)

    print("=== (iv) near-parallel path in class (b): t2 -> t1 = 1/3 ===")
    for eps in [F(1, 3), F(1, 6), F(1, 12), F(1, 60)]:
        report(f"eps={eps}", class_b(F(1, 3), F(1, 3)+eps, F(1, 2)),
               q=12, pw=24)

    print("done")
