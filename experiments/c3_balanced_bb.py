#!/usr/bin/env python3
"""
c3_balanced_bb.py -- R14-1: exact branch-and-bound decision for the BALANCED
regime of C_3 at the sandwich tau = (13/25, 1/2, 1/2).

CLAIM to decide:  no (l,h) in [0,1]^6 with all r_i <= 1 - w0 covers Delta
with Sigma r <= 1.  Combined with the R13 extreme-regime theorem (which
handles max r_i >= 1 - w0, equality only trivial), an empty B&B tree proves
    C_3(sandwich) = 1, attained only by the trivial coverings
-- the first non-concurrent triple with Bang(3) proved (computer-assisted,
exact rational arithmetic throughout; certificate = the B&B tree itself).

SOUNDNESS of the three prunes (each certified exactly, in fractions):
  P1 (irrelevant): min over box of Sigma r > 1  -> no config in the box has
     Sigma r <= 1.
  P2 (extreme):    some i with min over box of r_i >= 1 - w0 -> every config
     lies in the extreme regime, already settled by the R13 theorem.
  P3 (fails):      the ENLARGED configuration I_i+ = [min l_i, max h_i]
     (superset of every plank in the box) fails to cover, certified by
     (a) an edge uncovered by the enlarged traces (exact 1-D), or
     (b) a sign cell of the enlarged configuration whose polygon inside
         Delta has POSITIVE AREA (exact clipping; a positive-area cell
         contains interior uncovered points).
     Completeness of (a)+(b) as a failure test: an uncovered point is either
     on an edge (caught by (a)) or interior, in which case its strict sign
     cell contains a disk (caught by (b)).
Otherwise split the box along its widest coordinate.

If the queue empties: THEOREM.  If the budget is hit: the surviving frontier
is saved (resumable; its location is itself diagnostic).
"""

import time
from fractions import Fraction as F

TAU = (F(13, 25), F(1, 2), F(1, 2))
SPLIT_FRAC = F(1, 2)
V = [(TAU[0], F(0), F(1)), (F(0), F(1), TAU[1]), (F(1), TAU[2], F(0))]

# ---------------------------------------------------------------- w0(tau)
def w0_one(t1, t2, t3):
    return F(1, 2)*min(t1, 1 - t1, (1 - t2)*t1/(1 + t1),
                       t3*(1 - t1)/(2 - t1))

W0 = min(w0_one(*TAU),
         w0_one(TAU[1], TAU[2], TAU[0]),
         w0_one(TAU[2], TAU[0], TAU[1]))
BAL = 1 - W0            # balanced threshold: r_i <= BAL

# ---------------------------------------------------------------- geometry
# points as (lam1, lam2); lam3 = 1 - lam1 - lam2.
TRI = [(F(1), F(0)), (F(0), F(1)), (F(0), F(0))]   # A, B, C

def ulin(i):
    """u_i(x) = a*lam1 + b*lam2 + c."""
    va, vb, vc = V[i]
    return (va - vc, vb - vc, vc)

ULIN = [ulin(i) for i in range(3)]

def ueval(i, p):
    a, b, c = ULIN[i]
    return a*p[0] + b*p[1] + c

def clip(poly, a, b, c, keep_le):
    """Clip polygon by halfplane a*x+b*y+c <= 0 (keep_le) or >= 0."""
    if not poly:
        return poly
    out = []
    n = len(poly)
    def side(p):
        s = a*p[0] + b*p[1] + c
        return s if keep_le else -s
    for k in range(n):
        P, Q = poly[k], poly[(k + 1) % n]
        sP, sQ = side(P), side(Q)
        if sP <= 0:
            out.append(P)
        if (sP < 0 < sQ) or (sQ < 0 < sP):
            t = sP/(sP - sQ)
            out.append((P[0] + t*(Q[0]-P[0]), P[1] + t*(Q[1]-P[1])))
    # dedupe consecutive
    ded = []
    for p in out:
        if not ded or p != ded[-1]:
            ded.append(p)
    if len(ded) > 1 and ded[0] == ded[-1]:
        ded.pop()
    return ded

def area2(poly):
    if len(poly) < 3:
        return F(0)
    s = F(0)
    for k in range(len(poly)):
        x1, y1 = poly[k]
        x2, y2 = poly[(k + 1) % len(poly)]
        s += x1*y2 - x2*y1
    return abs(s)

def cell_positive_area(lh_plus, sigma):
    """Does sign cell sigma of the enlarged config have positive area in
    Delta? lh_plus[i] = (lo, hi) or None (empty plank -> no constraint from
    that plank... careful: empty plank means EVERY point is 'outside' it, so
    the cell constraint for i is vacuous only in the sense that both
    lo/hi patterns merge; we treat None as: constraint always satisfied."""
    poly = TRI[:]
    for i in range(3):
        if lh_plus[i] is None:
            continue
        a, b, c = ULIN[i]
        lo, hi = lh_plus[i]
        if sigma[i] == 0:   # u_i < lo  -> keep u_i - lo <= 0
            poly = clip(poly, a, b, c - lo, True)
        else:               # u_i > hi  -> keep u_i - hi >= 0
            poly = clip(poly, a, b, c - hi, False)
        if not poly:
            return False
    return area2(poly) > 0

def edges_fail(lh_plus):
    """Some edge of Delta not covered by the enlarged traces (exact 1-D)."""
    E = [(0, 1), (1, 2), (2, 0)]
    for (a, b) in E:
        segs = []
        for i in range(3):
            if lh_plus[i] is None:
                continue
            va, vb = V[i][a], V[i][b]
            lo, hi = lh_plus[i]
            if va == vb:
                if lo <= va <= hi:
                    segs.append((F(0), F(1)))
                continue
            t0, t1 = (lo - va)/(vb - va), (hi - va)/(vb - va)
            lo2, hi2 = min(t0, t1), max(t0, t1)
            lo2, hi2 = max(lo2, F(0)), min(hi2, F(1))
            if lo2 <= hi2:
                segs.append((lo2, hi2))
        segs.sort()
        reach = F(0)
        ok = True
        for lo2, hi2 in segs:
            if lo2 > reach:
                ok = False
                break
            reach = max(reach, hi2)
        if not ok or reach < 1:
            return True
    return False

def config_fails(lh_plus):
    if edges_fail(lh_plus):
        return True
    for sigma in ((0,0,0),(0,0,1),(0,1,0),(0,1,1),
                  (1,0,0),(1,0,1),(1,1,0),(1,1,1)):
        if cell_positive_area(lh_plus, sigma):
            return True
    return False

# ---------------------------------------------------------------- B&B
def run(max_seconds=360, max_boxes=2_000_000, checkpoint=None, split_mode='widest'):
    # box = tuple of 6 (lo,hi): order (l1,h1,l2,h2,l3,h3)
    root = (tuple((F(0), F(1)) for _ in range(6)), 0)
    stack = [root]
    t0 = time.time()
    stats = dict(P1=0, P2=0, P3=0, P4=0, split=0, processed=0)
    frontier = []
    while stack:
        stats['processed'] += 1
        if stats['processed'] % 20000 == 0:
            el = time.time() - t0
            print(f"  ... {stats['processed']} boxes, stack {len(stack)}, "
                  f"{el:.0f}s, prunes {stats['P1']}/{stats['P2']}/{stats['P3']}",
                  flush=True)
        if time.time() - t0 > max_seconds or stats['processed'] > max_boxes:
            frontier = stack
            break
        box, depth = stack.pop()
        # P1: min Sigma r over box > 1 ?
        smin = sum(max(F(0), box[2*i+1][0] - box[2*i][1]) for i in range(3))
        if smin > 1:
            stats['P1'] += 1
            continue
        # P2: some plank forced extreme
        if any(box[2*i+1][0] - box[2*i][1] >= BAL for i in range(3)):
            stats['P2'] += 1
            continue
        # P4: some plank empty for EVERY config in the box -> any covering in
        # the box is by <= 2 planks in 2 non-parallel directions -> Thm 3.1
        # (Gardner) gives Sigma r >= 1 there, with the equality cases being
        # 2-plank tight coverings (handled analytically in the note).
        lh_plus = []
        empty = False
        for i in range(3):
            lo, hi = box[2*i][0], box[2*i+1][1]
            if lo > hi:
                empty = True
            lh_plus.append((lo, hi) if lo <= hi else None)
        if empty:
            stats['P4'] += 1
            continue
        # P3: enlarged config fails
        if config_fails(lh_plus):
            stats['P3'] += 1
            continue
        # split widest coordinate
        widths = [box[k][1] - box[k][0] for k in range(6)]
        if split_mode == 'roundrobin' and widths[depth % 6] > 0:
            k = depth % 6
        else:
            k = max(range(6), key=lambda j: widths[j])
        if widths[k] == 0:
            # zero-width box that survives all prunes: report loudly
            print("  !! zero-width surviving box:", box, flush=True)
            frontier = stack + [box]
            break
        mid = box[k][0] + SPLIT_FRAC*(box[k][1] - box[k][0])
        b1 = list(box); b1[k] = (box[k][0], mid)
        b2 = list(box); b2[k] = (mid, box[k][1])
        stack.append((tuple(b1), depth + 1)); stack.append((tuple(b2), depth + 1))
        stats['split'] += 1
    el = time.time() - t0
    print(f"w0 = {W0}, balanced threshold r_i <= {BAL}")
    print(f"processed {stats['processed']} boxes in {el:.0f}s; "
          f"prunes P1={stats['P1']} P2={stats['P2']} P3={stats['P3']} P4={stats['P4']}, "
          f"splits={stats['split']}")
    if not frontier and not stack:
        print("QUEUE EMPTY: no balanced covering with Sigma r <= 1 exists.")
        print("=> combined with the R13 extreme-regime theorem:")
        print("   C_3(sandwich) = 1, attained only trivially.  THEOREM")
        print("   (computer-assisted, exact rational arithmetic).")
        return True
    print(f"BUDGET HIT: {len(frontier)} boxes remain (resumable).")
    if checkpoint:
        with open(checkpoint, 'w') as f:
            for b, _ in frontier:
                f.write(repr([(str(x[0]), str(x[1])) for x in b]) + "\n")
        print(f"frontier saved to {checkpoint}")
    # diagnostic: where does it zoom?
    if frontier:
        b = frontier[-1][0]
        print("sample surviving box:",
              [(float(x[0]), float(x[1])) for x in b])
    return False


if __name__ == '__main__':
    run()
