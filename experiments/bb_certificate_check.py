#!/usr/bin/env python3
"""
bb_certificate_check.py -- INDEPENDENT verifier for the balanced-regime
emptiness certificate of C_3(tau0), tau0 = (13/25, 1/2, 1/2).

de Bruijn criterion: this file shares NO code with the searcher
(c3_balanced_bb.py).  It re-derives the triangle geometry, the threshold
w0(tau), and every prune rule from scratch, in exact rational arithmetic
(fractions.Fraction; zero floats, hardware-independent).  It reconstructs
each box from the tree shape alone (the certificate stores no boxes), so a
box-arithmetic bug in the searcher would be caught here.

What it verifies:
  (TILING)  the leaves partition [0,1]^6: the certificate is a preorder
            traversal of a binary tree whose root is the cube and every
            internal node splits one coordinate at a strictly interior point
            into [lo,mid] and [mid,hi].  Reconstructing boxes top-down and
            consuming the whole stream with an empty final stack proves the
            leaves cover the cube with measure-zero overlaps.
  (PRUNES)  every leaf is validly pruned by its recorded rule + witness:
            P1  min_box Sigma r > 1               (no config has Sigma r<=1)
            P2  some i: min_box r_i >= 1-w0        (extreme regime, Thm R13)
            P4  some i: box forces plank i empty   (<=2 planks, Thm 3.1)
            P3  the enlarged config [l_i^-, h_i^+] fails to cover Delta,
                witnessed by an uncovered edge or a positive-area sign cell.
  (SCOPE)   the header tau matches the claimed tau0 and the header w0/BAL
            match this checker's own independent computation.

Final authority: prints 'CERTIFICATE VALID' iff all checks pass.
"""

import sys
import hashlib
from fractions import Fraction as F


def parse_frac(tok):
    return F(tok)


# ---- independent triangle geometry (barycentric; point = (lam1, lam2)) ----
CORNERS = [(F(1), F(0)), (F(0), F(1)), (F(0), F(0))]     # A, B, C
EDGES = [(0, 1), (1, 2), (2, 0)]


def directions(tau):
    t1, t2, t3 = tau
    # vertex values at (A, B, C) of the cyclic triple
    return [(t1, F(0), F(1)), (F(0), F(1), t2), (F(1), t3, F(0))]


def ulin(V):
    """u_i(lam1,lam2) = a*lam1 + b*lam2 + c  (lam3 = 1 - lam1 - lam2)."""
    out = []
    for (va, vb, vc) in V:
        out.append((va - vc, vb - vc, vc))
    return out


def w0_of(tau):
    def one(t1, t2, t3):
        return F(1, 2) * min(t1, 1 - t1, (1 - t2) * t1 / (1 + t1),
                             t3 * (1 - t1) / (2 - t1))
    t1, t2, t3 = tau
    return min(one(t1, t2, t3), one(t2, t3, t1), one(t3, t1, t2))


# ---- independent polygon clipping / area (Sutherland-Hodgman, exact) ----
def clip_halfplane(poly, a, b, c, keep_le):
    """Keep {a x + b y + c <= 0} if keep_le else {>= 0}."""
    if not poly:
        return poly
    out = []
    n = len(poly)
    for k in range(n):
        P, Q = poly[k], poly[(k + 1) % n]
        sP = a * P[0] + b * P[1] + c
        sQ = a * Q[0] + b * Q[1] + c
        if not keep_le:
            sP, sQ = -sP, -sQ
        if sP <= 0:
            out.append(P)
        if (sP < 0 < sQ) or (sQ < 0 < sP):
            t = sP / (sP - sQ)
            out.append((P[0] + t * (Q[0] - P[0]), P[1] + t * (Q[1] - P[1])))
    res = []
    for p in out:
        if not res or p != res[-1]:
            res.append(p)
    if len(res) > 1 and res[0] == res[-1]:
        res.pop()
    return res


def twice_area(poly):
    if len(poly) < 3:
        return F(0)
    s = F(0)
    for k in range(len(poly)):
        x1, y1 = poly[k]
        x2, y2 = poly[(k + 1) % len(poly)]
        s += x1 * y2 - x2 * y1
    return abs(s)


# ---- prune validators (each independent) ----
def check_P1(box):
    smin = sum(max(F(0), box[2 * i + 1][0] - box[2 * i][1]) for i in range(3))
    return smin > 1


def check_P2(box, i, BAL):
    return box[2 * i + 1][0] - box[2 * i][1] >= BAL


def check_P4(box, i):
    return box[2 * i][0] > box[2 * i + 1][1]


def enlarged(box):
    """Widest planks over the box; None if forced empty (shouldn't happen at
    a P3 leaf since P4 has priority)."""
    lh = []
    for i in range(3):
        lo, hi = box[2 * i][0], box[2 * i + 1][1]
        lh.append((lo, hi) if lo <= hi else None)
    return lh


def check_P3_edge(box, ei, V):
    lh = enlarged(box)
    a, b = EDGES[ei]
    segs = []
    for i in range(3):
        if lh[i] is None:
            continue
        va, vb = V[i][a], V[i][b]
        lo, hi = lh[i]
        if va == vb:
            if lo <= va <= hi:
                segs.append((F(0), F(1)))
            continue
        t0 = (lo - va) / (vb - va)
        t1 = (hi - va) / (vb - va)
        s0, s1 = (t0, t1) if t0 <= t1 else (t1, t0)
        s0, s1 = max(s0, F(0)), min(s1, F(1))
        if s0 <= s1:
            segs.append((s0, s1))
    segs.sort()
    reach = F(0)
    for s0, s1 in segs:
        if s0 > reach:
            return True          # gap: edge uncovered
        reach = max(reach, s1)
    return reach < 1             # tail uncovered


def check_P3_cell(box, sigma, ULIN):
    lh = enlarged(box)
    poly = list(CORNERS)
    for i in range(3):
        if lh[i] is None:
            continue
        a, b, c = ULIN[i]
        lo, hi = lh[i]
        if sigma[i] == 0:                    # u_i < lo  ->  u_i - lo <= 0
            poly = clip_halfplane(poly, a, b, c - lo, True)
        else:                                # u_i > hi  ->  u_i - hi >= 0
            poly = clip_halfplane(poly, a, b, c - hi, False)
        if not poly:
            return False
    return twice_area(poly) > 0


# ---- certificate parser + tree walker ----
def check(path, tau0=(F(13, 25), F(1, 2), F(1, 2))):
    with open(path) as f:
        lines = f.read().split('\n')
    hdr = {}
    it = iter(lines)
    for line in it:
        if line.startswith('#') or line == '':
            continue
        if line == 'BEGIN':
            break
        parts = line.split()
        hdr[parts[0]] = parts[1:]

    tau = tuple(parse_frac(x) for x in hdr['TAU'])
    assert tau == tuple(tau0), f"header tau {tau} != claimed {tau0}"
    V = directions(tau)
    UL = ulin(V)
    BAL_hdr = parse_frac(hdr['BAL'][0])
    W0_hdr = parse_frac(hdr['W0'][0])
    W0 = w0_of(tau)                          # independent recomputation
    BAL = 1 - W0
    assert W0 == W0_hdr, f"w0 mismatch: checker {W0} vs header {W0_hdr}"
    assert BAL == BAL_hdr, f"BAL mismatch: {BAL} vs {BAL_hdr}"

    # collect the token lines after BEGIN, stop at END
    toks = []
    for line in it:
        if line == 'END':
            break
        if line.strip():
            toks.append(line.split())

    # preorder walk: stack of boxes to assign to the next token
    root = tuple((F(0), F(1)) for _ in range(6))
    stack = [root]
    counts = dict(S=0, L1=0, L2=0, L3E=0, L3C=0, L4=0)
    for tok in toks:
        if not stack:
            raise AssertionError("token stream longer than tree (extra tokens)")
        box = stack.pop()
        kind = tok[0]
        if kind == 'S':
            k = int(tok[1]); mid = parse_frac(tok[2])
            lo, hi = box[k]
            assert lo < mid < hi, f"non-interior split: {lo} < {mid} < {hi} false"
            left = list(box); left[k] = (lo, mid)
            right = list(box); right[k] = (mid, hi)
            stack.append(tuple(right))       # right below
            stack.append(tuple(left))        # left popped next (preorder)
            counts['S'] += 1
        elif kind == 'L1':
            assert check_P1(box), f"P1 invalid at {box}"
            counts['L1'] += 1
        elif kind == 'L2':
            i = int(tok[1])
            assert check_P2(box, i, BAL), f"P2 invalid at {box}, i={i}"
            counts['L2'] += 1
        elif kind == 'L4':
            i = int(tok[1])
            assert check_P4(box, i), f"P4 invalid at {box}, i={i}"
            counts['L4'] += 1
        elif kind == 'L3E':
            ei = int(tok[1])
            assert check_P3_edge(box, ei, V), f"P3-edge invalid at {box}, e={ei}"
            counts['L3E'] += 1
        elif kind == 'L3C':
            sigma = tuple(int(ch) for ch in tok[1])
            assert check_P3_cell(box, sigma, UL), \
                f"P3-cell invalid at {box}, sigma={sigma}"
            counts['L3C'] += 1
        else:
            raise AssertionError(f"unknown token {kind}")
    assert not stack, f"tree incomplete: {len(stack)} unexpanded boxes remain"

    n_leaf = sum(v for k, v in counts.items() if k != 'S')
    n_int = counts['S']
    assert n_leaf == n_int + 1, \
        f"binary-tree identity fails: leaves {n_leaf} != internals+1 {n_int+1}"

    h = hashlib.sha256(open(path, 'rb').read()).hexdigest()
    print(f"tau = {tau}, w0 = {W0} (recomputed), BAL = {BAL}")
    print(f"tree: {n_int} internal splits, {n_leaf} leaves "
          f"(binary-tree identity leaves = internals + 1: OK)")
    print(f"leaf rules: P1={counts['L1']} P2={counts['L2']} "
          f"P3edge={counts['L3E']} P3cell={counts['L3C']} P4={counts['L4']}")
    print(f"certificate SHA-256: {h}")
    print("TILING: leaves partition [0,1]^6 (every split strictly interior; "
          "stream consumed; stack empty).")
    print("PRUNES: every leaf validly discharged by its rule + exact witness.")
    print("CERTIFICATE VALID")
    return True


if __name__ == '__main__':
    path = sys.argv[1] if len(sys.argv) > 1 else 'c3_sandwich_certificate.txt'
    check(path)
