r"""
P3: GENERAL Bang(3) model (no common active edge). 3 planks with ARBITRARY normalized
directions u1,u2,u3 on Delta (vertex values (vA,vB,vC), min 0 max 1).

Key reduction (uses validated clipping engine exp_w2_delta.span_free):
    min Sum r over coverings (fixed directions)
       = min over (l1,r1,l2,r2) of [ r1 + r2 + span_{u3}(Delta \ (P1 U P2)) ],
since for fixed P1,P2 the minimal width r3 covering the residual free set equals the
u3-span of that free set. min Sum r is symmetric in the 3 planks, so fixing u3 as the
"target" is WLOG.

Direction = (imin,imax,tau): v[imin]=0, v[imax]=1, third vertex = tau in [0,1].
FACET direction <=> two vertex values equal <=> tau in {0,1}. Generic <=> tau in (0,1).

DICHOTOMY HYPOTHESIS (to test): a direction-triple is EXTREMAL (min Sum r = 1) IFF at
least one of u1,u2,u3 is facet-parallel.  Measure whether this generalizes from the
common-edge subcase (notes/32) or is a common-edge artifact.
"""
import sys
from itertools import product
from multiprocessing import Pool
from fractions import Fraction as Q
from exp_w2_delta import span_free


def gen_dir(imin, imax, tau):
    v = [None, None, None]
    third = ({0, 1, 2} - {imin, imax}).pop()
    v[imin] = 0.0; v[imax] = 1.0; v[third] = float(tau)
    return tuple(v)


def is_facet(u, tol=1e-9):
    return (abs(u[0] - u[1]) < tol) or (abs(u[1] - u[2]) < tol) or (abs(u[0] - u[2]) < tol)


def min_sigma_r(u1, u2, u3, N, refine=2):
    """Grid + local refine over (l1,r1,l2,r2). Returns (minSumr, cfg)."""
    def scan(lo, hi, nn):
        step = [(hi[k] - lo[k]) / nn for k in range(4)]
        best = (1e9, None)
        # r1,r2 grid; l1,l2 grid
        for i in range(nn + 1):
            r1 = lo[1] + i * step[1]
            if r1 < 0 or r1 > 1:
                continue
            for j in range(nn + 1):
                r2 = lo[3] + j * step[3]
                if r2 < 0 or r1 + r2 > 1 + 1e-12:
                    continue
                for a in range(nn + 1):
                    l1 = lo[0] + a * step[0]
                    for b in range(nn + 1):
                        l2 = lo[2] + b * step[2]
                        res = span_free(u1, u2, u3, l1, r1, l2, r2, exact=False)
                        if res is None:
                            continue
                        val = r1 + r2 + res["span"]
                        if val < best[0]:
                            best = (val, (l1, r1, l2, r2))
        return best
    lo = [0.0, 0.0, 0.0, 0.0]; hi = [1.0, 1.0, 1.0, 1.0]
    best = scan(lo, hi, N)
    for _ in range(refine):
        if best[1] is None:
            break
        c = best[1]
        w = [0.5 * (hi[k] - lo[k]) / N * 2 for k in range(4)]  # half window
        lo = [max(0.0, c[k] - w[k]) for k in range(4)]
        hi = [min(1.0, c[k] + w[k]) for k in range(4)]
        b2 = scan(lo, hi, N)
        if b2[0] < best[0]:
            best = b2
    return best


def job(args):
    u1, u2, u3, N = args
    val, cfg = min_sigma_r(u1, u2, u3, N)
    nf = sum(is_facet(u) for u in (u1, u2, u3))
    return (val, nf, u1, u2, u3, cfg)


def main():
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 16
    # sanity: all-facet Hunter triple -> min Sum r should be 1.0
    uA = gen_dir(0, 1, 0.0)  # vC? value (0,1,0)=x_B
    print("sanity all-facet (x_B,x_A,x_C):",
          min_sigma_r((0, 1, 0), (1, 0, 0), (0, 0, 1), N)[0], "(expect ~1)")

    # build a sample of direction triples grouped by facet-count
    taus_gen = [0.2, 0.35, 0.5, 0.65, 0.8]
    roles = [(0, 1), (1, 0), (0, 2), (2, 0), (1, 2), (2, 1)]
    import random
    random.seed(7)
    def rand_dir(facet):
        im, ix = random.choice(roles)
        tau = random.choice([0.0, 1.0]) if facet else random.choice(taus_gen)
        return gen_dir(im, ix, tau)
    jobs = []
    # 0-facet (all generic), 1-facet, 2-facet, 3-facet triples
    per = 200
    for nf_target in (0, 1, 2, 3):
        for _ in range(per):
            facets = [True] * nf_target + [False] * (3 - nf_target)
            random.shuffle(facets)
            us = [rand_dir(f) for f in facets]
            # skip degenerate (two identical directions)
            jobs.append((us[0], us[1], us[2], N))
    with Pool() as pool:
        out = pool.map(job, jobs)

    from collections import defaultdict
    buck = defaultdict(list)
    belowone = 0
    for val, nf, u1, u2, u3, cfg in out:
        buck[nf].append(val)
        if val < 1 - 1e-6:
            belowone += 1
            print(f"  !!! Sum r < 1 found: {val:.5f}  nf={nf} u=({u1},{u2},{u3}) cfg={cfg}")
    print(f"\nBang(3) general: min Sum r by #facet-directions (grid N={N}, refine):")
    print(f"  (min Sum r is an UPPER bound on the true min; ~1 => TIGHT/extremal)")
    for nf in (0, 1, 2, 3):
        vs = sorted(buck[nf])
        if not vs:
            continue
        import statistics
        tight = sum(1 for v in vs if v < 1.002)
        print(f"  #facets={nf}: n={len(vs)}  min={vs[0]:.4f}  median={statistics.median(vs):.4f}  "
              f"max={vs[-1]:.4f}  tight(<1.002)={tight}/{len(vs)} ({tight/len(vs):.0%})")
    print(f"  Sum r < 1 events (Bang(3) violations / bugs): {belowone}")


if __name__ == "__main__":
    main()
