"""Cross-check for the hand proof of the median edge-tiling lemma (Appendix A of
affine-plank-triangle.tex; R6-2). Exact rational search over interval endpoints on
a grid containing 1/3, 1/2, 2/3, testing the exact per-edge tiling conditions via
the trace formulas
    T_low  = [max(0,1-2h_c), 1-2l_c]   (nondegenerate iff l_c < 1/2)
    T_full = [l_f, h_f]
    T_high = [2-2h_g, min(1,2-2l_g)]   (nondegenerate iff h_g > 1/2)
with edge roles (c,f,g) = (1,2,3) on AB, (3,1,2) on BC, (2,3,1) on CA.
Output: exactly three solutions, of L/M/R type vectors LLL, MMM, RRR:
[0,1/3]^3, [1/3,2/3]^3, [2/3,1]^3 — matching the seven-case hand proof and the
independent enumerations (median_rigidity_enumeration.py,
median_edgetilings_independent.py).
"""
from fractions import Fraction as F

ROLES = [(0, 1, 2), (2, 0, 1), (1, 2, 0)]  # (low, full, high) per edge AB, BC, CA


def traces(I, edge):
    c, f, g = ROLES[edge]
    out = []
    lc, hc = I[c]
    if lc < F(1, 2):
        out.append((max(F(0), 1 - 2 * hc), 1 - 2 * lc))
    out.append(I[f])
    lg, hg = I[g]
    if hg > F(1, 2):
        out.append((2 - 2 * hg, min(F(1), 2 - 2 * lg)))
    return [(a, b) for a, b in out if b > a]


def tiles(ts):
    if sum(b - a for a, b in ts) != 1:
        return False
    ts = sorted(ts)
    cur = F(0)
    for a, b in ts:
        if a != cur:
            return False
        cur = b
    return cur == 1


def typ(iv):
    l, h = iv
    return 'L' if h <= F(1, 2) else ('R' if l >= F(1, 2) else 'M')


if __name__ == '__main__':
    N = 12
    vals = [F(k, N) for k in range(N + 1)]
    ivs = [(l, h) for l in vals for h in vals if h > l]
    sols = [(I1, I2, I3)
            for I1 in ivs for I2 in ivs for I3 in ivs
            if all(tiles(traces((I1, I2, I3), e)) for e in range(3))]
    for s in sols:
        print(s, ''.join(typ(iv) for iv in s))
    print('total:', len(sols))
    assert len(sols) == 3
