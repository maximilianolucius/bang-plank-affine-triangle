r"""
P3 (corrected): does a NON-DEGENERATE tight tiling (Sum r = 1, all planks essential)
exist for generic 3-direction triples? The degenerate single-full-plank covering
(r3=1, r1=r2=0) trivially gives Sum r=1 for ANY directions, so we EXCLUDE it by
requiring r_i in [eps, 1-eps] for all three planks.

min Sum r subject to r1,r2 in [eps,1-eps] and r3 = span_{u3}(free12) in [eps,1-eps].
If ~1  -> non-degenerate tight tiling exists (these directions tile).
If robustly >1 -> generic directions need Sum r>1 for an essential covering.
"""
import sys
from multiprocessing import Pool
from exp_w2_delta import span_free


def gen_dir(imin, imax, tau):
    v = [None, None, None]
    third = ({0, 1, 2} - {imin, imax}).pop()
    v[imin] = 0.0; v[imax] = 1.0; v[third] = float(tau)
    return tuple(v)


def is_facet(u, tol=1e-9):
    return (abs(u[0]-u[1]) < tol) or (abs(u[1]-u[2]) < tol) or (abs(u[0]-u[2]) < tol)


def min_tiling(u1, u2, u3, N, eps):
    best = (1e9, None)
    for i in range(N + 1):
        r1 = i / N
        if r1 < eps or r1 > 1 - eps:
            continue
        for j in range(N + 1):
            r2 = j / N
            if r2 < eps or r2 > 1 - eps or r1 + r2 > 1 - eps + 1e-12:
                continue
            for a in range(N + 1):
                l1 = a / N
                if l1 + r1 > 1 + 1e-9:
                    continue
                for b in range(N + 1):
                    l2 = b / N
                    if l2 + r2 > 1 + 1e-9:
                        continue
                    res = span_free(u1, u2, u3, l1, r1, l2, r2, exact=False)
                    if res is None:
                        continue
                    r3 = res["span"]
                    if r3 < eps or r3 > 1 - eps:
                        continue
                    val = r1 + r2 + r3
                    if val < best[0]:
                        best = (val, (l1, r1, l2, r2, r3))
    return best


def job(args):
    u1, u2, u3, N, eps = args
    val, cfg = min_tiling(u1, u2, u3, N, eps)
    nf = sum(is_facet(u) for u in (u1, u2, u3))
    return (val, nf, u1, u2, u3, cfg)


def main():
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 18
    eps = float(sys.argv[2]) if len(sys.argv) > 2 else 0.12
    # sanity: Hunter all-facet tiling t=1/3 each -> min ~1
    print("sanity all-facet:", min_tiling((0, 1, 0), (1, 0, 0), (0, 0, 1), N, eps)[0], "(expect ~1)")

    import random
    random.seed(11)
    roles = [(0, 1), (1, 0), (0, 2), (2, 0), (1, 2), (2, 1)]
    taus = [0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8]

    def rdir(facet):
        im, ix = random.choice(roles)
        t = random.choice([0.0, 1.0]) if facet else random.choice(taus)
        return gen_dir(im, ix, t)

    jobs = []
    per = 150
    for nf in (0, 1, 2, 3):
        cnt = 0
        tries = 0
        while cnt < per and tries < per * 20:
            tries += 1
            facets = [True]*nf + [False]*(3-nf); random.shuffle(facets)
            us = [rdir(f) for f in facets]
            # avoid two identical directions
            if len({us[0], us[1], us[2]}) < 3:
                continue
            if sum(is_facet(u) for u in us) != nf:
                continue
            jobs.append((us[0], us[1], us[2], N, eps)); cnt += 1
    with Pool() as pool:
        out = pool.map(job, jobs)

    from collections import defaultdict
    import statistics
    buck = defaultdict(list)
    feasible = defaultdict(int)
    below = 0
    examples_gen_tight = []
    for val, nf, u1, u2, u3, cfg in out:
        if cfg is None:
            continue  # no essential covering with Sum r small enough found in grid
        buck[nf].append(val)
        if val < 1 - 1e-6:
            below += 1
            print(f"  !!! essential Sum r<1: {val:.5f} nf={nf} u=({u1},{u2},{u3}) cfg={cfg}")
        if nf == 0 and val < 1.01:
            examples_gen_tight.append((val, u1, u2, u3, cfg))
    print(f"\nNON-DEGENERATE tight tiling, min Sum r by #facets (N={N}, eps={eps}):")
    for nf in (0, 1, 2, 3):
        vs = sorted(buck[nf])
        if not vs:
            print(f"  #facets={nf}: NO essential covering found in grid"); continue
        tight = sum(1 for v in vs if v < 1.01)
        print(f"  #facets={nf}: n={len(vs)} min={vs[0]:.4f} median={statistics.median(vs):.4f} "
              f"max={vs[-1]:.4f}  tight(<1.01)={tight}/{len(vs)} ({tight/len(vs):.0%})")
    print(f"  essential Sum r<1 events: {below}")
    print(f"\n  generic (0-facet) tight examples (val,u1,u2,u3,cfg):")
    for e in examples_gen_tight[:5]:
        print("   ", round(e[0], 4), e[1], e[2], e[3], tuple(round(x, 3) for x in e[4]))


if __name__ == "__main__":
    main()
