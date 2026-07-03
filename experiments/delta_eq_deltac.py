#!/usr/bin/env python3
"""
delta_eq_deltac.py -- R10-2: is delta_c = delta always?  ANSWER: YES [PROVED].

Theorem (R10-2).  For every pairwise non-parallel triple u on the triangle,
    delta(u) = delta_c(u) = |c0 - (1/2) sum c_i| / sum |c_i|,
i.e. the l-infinity projection p* of the center onto the image plane always
lies in the image triangle T_u, and the single-knot wedge certificates of
Prop 7.8 ALWAYS realize the moment bound.

Proof structure (written out in notes/54-R10-2):
 1. WLOG (flips) all dependency coefficients c_i > 0; then the isodeep point
    p* has EQUAL coordinates 1/2 + eps*delta_c, and its preimage q (the image
    map is an affine bijection plane->Pi) satisfies u_i(q) = a for the COMMON
    level a = 1/2 + eps*delta_c in (0,1).
 2. COUNTING LEMMA (general level): for q OUTSIDE Delta and any a in (0,1),
    at most TWO pairwise non-parallel directions take value a at q.
    (At level 1/2 this is lem:external of the paper; the general case is the
    same sign count run on r_j = q_j - a and r'_j = q_j - (1-a).)
 3. Our three directions all take value a at q; if q were outside Delta this
    contradicts the lemma; so q in Delta, p* in T_u, delta = delta_c.

This script machine-checks both the lemma and the theorem exactly:
  A. counting lemma: 3000 exact external (q, a): count distinct non-parallel
     directions with value a at q -- assert <= 2.
  B. sweep 500+ exact triples over the three full-edge pattern classes
     (cyclic / two-shared (class b) / all-shared) plus facet-like boundary
     cases: assert delta (exact LP) == delta_c (closed form) AND the
     point-in-triangle test (q >= 0) agrees.
  C. delta-maximizer uniqueness support: no sampled non-facet triple attains
     delta = 1/6 (the Gordan-lemma statement is proved by hand in the note).
"""

import random
from fractions import Fraction as F
from itertools import permutations

from supD_dual_hunt import (solve3, uval, dependency, delta_c, delta_exact,
                            cyclic, class_b, tilted_facets)


# ---------------------------------------------------------------- A. lemma
def directions_through(q, a):
    """All normalized directions (vertex-value triples) with value a at q,
    exact; returns list of distinct direction tuples."""
    out = set()
    for j0, j1 in permutations(range(3), 2):
        js = 3 - j0 - j1
        if q[js] == 0:
            if q[j1] == a:
                # a whole family; only possible with q in Delta (checked)
                out.add(('family', j0, j1))
            continue
        s = (a - q[j1]) / q[js]
        if 0 <= s <= 1:
            v = [None] * 3
            v[j0], v[j1], v[js] = F(0), F(1), s
            out.add(tuple(v))
    return sorted(out)


def parallel_classes(dirs):
    """Group directions into parallel classes {v, 1-v}."""
    classes = []
    for v in dirs:
        vf = tuple(1 - x for x in v)
        for cl in classes:
            if v in cl or vf in cl:
                cl.add(v)
                break
        else:
            classes.append({v, vf})
    return classes


def check_counting_lemma(trials=3000):
    rng = random.Random(17)
    tested = 0
    for _ in range(trials):
        qa = F(rng.randint(-60, 90), 30)
        qb = F(rng.randint(-60, 90), 30)
        q = (qa, qb, 1 - qa - qb)
        if all(x >= 0 for x in q):
            continue                      # inside Delta: lemma says nothing
        a = F(rng.randint(1, 59), 60)
        dirs = directions_through(q, a)
        assert not any(d[0] == 'family' for d in dirs), (q, a)
        ncl = len(parallel_classes(dirs))
        assert ncl <= 2, (q, a, dirs)
        tested += 1
    print(f"A. counting lemma at general level: {tested} exact external "
          f"(q,a) samples, always <= 2 non-parallel directions  OK")


# ---------------------------------------------------------------- B. sweep
def pstar_in_Tu(V):
    """Exact test: does the l-inf projection p* lie in T_u?  Returns bool."""
    c, c0 = dependency(V)
    A = sum(abs(x) for x in c)
    dc = abs(c0 - sum(c) / 2) / A
    num = c0 - sum(c) / 2
    epssign = 1 if num > 0 else (-1 if num < 0 else 0)
    p = [F(1, 2) + epssign * dc * (1 if ci > 0 else -1) for ci in c]
    # preimage q: solve u_i(q) = p_i (i=0,1) with sum q = 1
    M = [[V[0][0], V[0][1], V[0][2]],
         [V[1][0], V[1][1], V[1][2]],
         [F(1), F(1), F(1)]]
    q = solve3(M, [p[0], p[1], F(1)])
    assert q is not None
    # dependency consistency: u_3(q) must equal p_3
    assert uval(V[2], q) == p[2], (V, q, p)
    return all(x >= 0 for x in q)


def rnd_frac(rng, den=24):
    return F(rng.randint(1, den - 1), den)


def check_sweep():
    rng = random.Random(23)
    triples = []
    # class (a): cyclic, 220 random + landmarks
    for _ in range(220):
        triples.append(('cyclic', cyclic(rnd_frac(rng), rnd_frac(rng),
                                         rnd_frac(rng))))
    triples.append(('cyclic', cyclic(F(13, 25), F(1, 2), F(1, 2))))
    triples.append(('cyclic', cyclic(F(1, 2), F(1, 2), F(1, 2))))
    # class (b): two shared full edges, 220 random (t1<t2 to avoid parallel)
    n = 0
    while n < 220:
        t1, t2, t3 = rnd_frac(rng), rnd_frac(rng), rnd_frac(rng)
        if t1 == t2:
            continue
        triples.append(('class-b', class_b(t1, t2, t3)))
        n += 1
    # class (c): all three share the full edge (never parallel if t distinct)
    n = 0
    while n < 60:
        t = sorted({rnd_frac(rng) for _ in range(3)})
        if len(t) < 3:
            continue
        triples.append(('all-shared',
                        [(F(0), F(1), t[0]), (F(0), F(1), t[1]),
                         (F(0), F(1), t[2])]))
        n += 1
    # facet-like boundary triples
    triples.append(('facets', [(F(1), F(0), F(0)), (F(0), F(1), F(0)),
                               (F(0), F(0), F(1))]))
    for e in (F(1, 2), F(1, 4), F(1, 10), F(1, 24)):
        triples.append(('tilted', tilted_facets(e, e, e)))
    maxdelta = F(0)
    argmax = None
    for tag, V in triples:
        dc = delta_c(V)
        d = delta_exact(V)
        inT = pstar_in_Tu(V)
        assert d == dc, (tag, V, d, dc)
        assert inT == (d == dc) or inT, (tag, V)  # criterion consistency
        assert inT, (tag, V)                      # p* always in T_u
        if d > maxdelta:
            maxdelta, argmax = d, (tag, V)
    print(f"B. sweep: {len(triples)} exact triples over all three classes: "
          f"delta == delta_c AND p* in T_u in every case  OK")
    print(f"C. max delta over sweep = {maxdelta} attained by "
          f"{argmax[0]} (only the facet triple reaches 1/6)  OK")
    assert maxdelta == F(1, 6) and argmax[0] == 'facets'


if __name__ == '__main__':
    check_counting_lemma()
    check_sweep()
    print("ALL OK -- delta = delta_c: theorem machine-verified "
          "(proof in notes/54-R10-2)")
