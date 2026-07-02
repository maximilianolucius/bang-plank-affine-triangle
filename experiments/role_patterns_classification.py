"""R6-5: exhaustive classification of the 216 role assignments of three normalized
directions on the triangle (notes/50-R6-5; Theorem thm:char in the paper).

A normalized direction is (v0, v1, tau): value 0 at vertex v0, 1 at v1, tau at the
third. For each of the 6^3 ordered role patterns, decide when the mid-level lines
{u_i = 1/2} concur at a point of the plane (barycentric sum = 1).

Findings (all exact, sympy):
  - full edges pairwise distinct (48 patterns): concurrence <=> a 2-parameter
    surface in tau; modulo per-direction flips (u -> 1-u, tau -> 1-tau) all these
    patterns are the cyclic one: covered by Thm 6.3/6.6 (measure mu_p, tight).
  - exactly two directions share a full edge (144 patterns): the concurrence
    condition R(tau)=0 either has NO roots with tau in (0,1)^3 (forms -(t-1)/2t,
    -t/2, -1/2, det V=0 inconsistent) or forces tau_j + tau_k = 1, which after a
    flip makes the two sharing directions IDENTICAL (degenerate, not a triple of
    distinct directions). Hence such triples never concur; consistently no witness
    measure exists (barycenter argument: E[u_i]=E[u_j]=1/2 forces supp mu inside
    the shared edge, where the third direction is not onto [0,1]).
  - all three share one full edge (24 patterns): mid-lines always concur at the
    midpoint of that edge; the uniform measure ON the edge is a witness, and
    sum rw >= 1 follows from covering the edge alone (trivial 1-D case).
Conclusion: a triple of pairwise non-parallel directions admits a uniform-marginal
witness measure iff its mid-level lines concur (Theorem thm:char).
"""
import sympy as sp
from itertools import product

t1, t2, t3 = sp.symbols('t1 t2 t3', positive=True)
taus = [t1, t2, t3]
pA, pB, pC = sp.symbols('pA pB pC')
specs = [(a, b) for a in range(3) for b in range(3) if a != b]


def row(spec, tau):
    v0, v1 = spec
    r = [None] * 3
    r[v0], r[v1] = sp.Integer(0), sp.Integer(1)
    r[3 - v0 - v1] = tau
    return r


def classify():
    results = {}
    for combo in product(specs, repeat=3):
        n_edges = len({frozenset(s) for s in combo})
        V = sp.Matrix([row(s, taus[i]) for i, s in enumerate(combo)])
        p = sp.Matrix([pA, pB, pC])
        eqs = list(V * p - sp.Matrix([sp.Rational(1, 2)] * 3)) + [pA + pB + pC - 1]
        sol = sp.solve(eqs, [pA, pB, pC], dict=True)
        if sol:
            status = 'always concurrent (given tau relation trivial or none)'
        elif V.det() == 0:
            status = 'detV=0, inconsistent: never concurrent'
        else:
            psol = V.LUsolve(sp.Matrix([sp.Rational(1, 2)] * 3))
            R = sp.factor(sp.simplify(psol[0] + psol[1] + psol[2] - 1))
            status = f'concurrent iff {R} = 0'
        results.setdefault((n_edges, status), []).append(combo)
    return results


if __name__ == '__main__':
    for (n, st), combos in sorted(classify().items()):
        print(f'full-edges={n} | {st} | n={len(combos)} | e.g. {combos[0]}')
