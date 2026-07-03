#!/usr/bin/env python3
"""
r15_equality.py -- R15-1d: classify the equality case Sigma r = 1 for the
sandwich tau0 = (13/25, 1/2, 1/2).

Structural reduction (proved in notes/58-R15):
  * balanced 3-plank coverings all have Sigma r > 1 STRICTLY (any covering
    config lies in a leaf; not P2/P4 since proper & balanced; not P3 since it
    covers; so P1, whose closed box has min Sigma r > 1 -> the config's
    Sigma r > 1).  So equality never occurs in the balanced regime.
  * extreme regime (Thm R13): equality only trivial (one full plank, rest 0).
  * hence Sigma r = 1 with a proper 3-plank covering is impossible; the only
    remaining equality candidates are 2-PLANK tight coverings (third empty).

This script settles the 2-plank question EXACTLY for the three pairs:
  minimize |I_i| + |I_j| over coverings {u_i in I_i} u {u_j in I_j} >= Delta.
Gardner (Thm 3.1) gives min >= 1.  We compute the exact min over PROPER
coverings (both intervals with positive length < 1) and check whether 1 is
attained properly.

Coverage test: the image of Delta under (u_i, u_j) is a triangle T' in the
(u_i,u_j)-square; covering <=> T' avoids the 4 open complement corners of the
two slabs.  Exact via polygon clipping.  Candidate optima come from a finite
exact breakpoint set (vertex-image coords, slab-boundary/edge couplings),
so the reported minimum is exact.
"""

import itertools
from fractions import Fraction as F

TAU = (F(13, 25), F(1, 2), F(1, 2))
# vertex values (A,B,C)
U = [(TAU[0], F(0), F(1)), (F(0), F(1), TAU[1]), (F(1), TAU[2], F(0))]


def image_triangle(i, j):
    """Vertices of image of Delta under (u_i, u_j): images of A, B, C."""
    return [(U[i][v], U[j][v]) for v in range(3)]   # v=0:A,1:B,2:C


def clip_hp(poly, a, b, c, keep_le):
    if not poly:
        return poly
    out = []
    n = len(poly)
    for k in range(n):
        P, Q = poly[k], poly[(k + 1) % n]
        sP = a*P[0] + b*P[1] + c
        sQ = a*Q[0] + b*Q[1] + c
        if not keep_le:
            sP, sQ = -sP, -sQ
        if sP <= 0:
            out.append(P)
        if (sP < 0 < sQ) or (sQ < 0 < sP):
            t = sP/(sP - sQ)
            out.append((P[0] + t*(Q[0]-P[0]), P[1] + t*(Q[1]-P[1])))
    res = []
    for p in out:
        if not res or p != res[-1]:
            res.append(p)
    if len(res) > 1 and res[0] == res[-1]:
        res.pop()
    return res


def area2(poly):
    if len(poly) < 3:
        return F(0)
    s = F(0)
    for k in range(len(poly)):
        x1, y1 = poly[k]; x2, y2 = poly[(k+1) % len(poly)]
        s += x1*y2 - x2*y1
    return abs(s)


def covers(T, ai, bi, aj, bj):
    """T' avoids all 4 open complement corners of slabs [ai,bi]x[aj,bj]?"""
    corners = [
        # (clip conditions selecting the open corner, as closed >-tests)
        [(1, 0, -ai, False), (0, 1, -aj, False)],   # u_i>bi? no: build below
    ]
    # LL {u_i<ai, u_j<aj}: keep u_i<=ai and u_j<=aj, area>0 => meets
    tests = [
        [(1, 0, -ai, True), (0, 1, -aj, True)],    # LL
        [(1, 0, -bi, False), (0, 1, -aj, True)],   # LR: u_i>=bi, u_j<=aj
        [(1, 0, -ai, True), (0, 1, -bj, False)],   # UL
        [(1, 0, -bi, False), (0, 1, -bj, False)],  # UR
    ]
    for conds in tests:
        poly = list(T)
        for (a, b, c, le) in conds:
            poly = clip_hp(poly, a, b, c, le)
            if not poly:
                break
        if area2(poly) > 0:
            return False
    return True


def min_width(i, j):
    T = image_triangle(i, j)
    xs = sorted({p[0] for p in T} | {F(0), F(1)})
    ys = sorted({p[1] for p in T} | {F(0), F(1)})
    # coupled breakpoints: edge lines of T evaluated at candidate x's / y's
    edges = [(T[a], T[b]) for a, b in ((0, 1), (1, 2), (2, 0))]
    xcand = set(xs); ycand = set(ys)
    for (P, Q) in edges:
        if P[0] != Q[0]:
            m = (Q[1]-P[1])/(Q[0]-P[0])
            for x in list(xs):
                ycand.add(P[1] + m*(x - P[0]))
        if P[1] != Q[1]:
            m = (Q[0]-P[0])/(Q[1]-P[1])
            for y in list(ys):
                xcand.add(P[0] + m*(y - P[1]))
    xcand = sorted(x for x in xcand if 0 <= x <= 1)
    ycand = sorted(y for y in ycand if 0 <= y <= 1)
    best_any = None; best_proper = None
    for ai, bi in itertools.combinations_with_replacement(xcand, 2):
        for aj, bj in itertools.combinations_with_replacement(ycand, 2):
            if covers(T, ai, bi, aj, bj):
                w = (bi - ai) + (bj - aj)
                if best_any is None or w < best_any[0]:
                    best_any = (w, ai, bi, aj, bj)
                proper = 0 < bi - ai < 1 and 0 < bj - aj < 1
                if proper and (best_proper is None or w < best_proper[0]):
                    best_proper = (w, ai, bi, aj, bj)
    return best_any, best_proper


if __name__ == '__main__':
    names = {(1, 2): "(u2,u3)", (0, 2): "(u1,u3)", (0, 1): "(u1,u2)"}
    print(f"sandwich tau = {TAU}")
    all_trivial = True
    for (i, j) in ((0, 1), (0, 2), (1, 2)):
        ba, bp = min_width(i, j)
        print(f"pair {names[(i,j)]}: min width (any) = {ba[0]} = "
              f"{float(ba[0]):.4f} at I{i+1}=[{ba[1]},{ba[2]}], "
              f"I{j+1}=[{ba[3]},{ba[4]}]")
        if bp is None:
            print(f"    NO proper covering (one interval must be [0,1]): "
                  f"tight => trivial only")
        else:
            print(f"    min width over PROPER coverings = {bp[0]} = "
                  f"{float(bp[0]):.4f}"
                  + ("  ** proper tight covering exists! **"
                     if bp[0] <= 1 else "  (> 1: no proper tight covering)"))
            if bp[0] <= 1:
                all_trivial = False
    print()
    if all_trivial:
        print("CONCLUSION: for every pair, tight (width=1) 2-plank coverings")
        print("are ONLY trivial (one full plank). Combined with the balanced")
        print("strictness and Thm R13: C_3(sandwich) = 1 is attained ONLY by")
        print("the trivial coverings (one full plank, the other two empty).")
    else:
        print("CONCLUSION: a proper tight 2-plank covering exists -- equality")
        print("set includes it; list above.")
