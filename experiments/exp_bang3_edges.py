r"""
P3 (right axis): classify NON-FACET direction triples by the number of DISTINCT ACTIVE
EDGES (edge between argmin and argmax of each direction). Measure whether a NON-DEGENERATE
tight tiling (Sum r = 1, all planks essential, r_i in [eps,1-eps]) exists.

- 1 distinct active edge  = all three planks share a common active edge (the notes/32
  common-edge family).
- 3 distinct active edges = truly generic Bang(3) (no two planks share an active edge).

Question: do 3-distinct-edge triples admit tight tilings, or is Sum r robustly >1
(i.e., is there exploitable slack in the genuinely-generic Bang(3) case)?
"""
import sys
from multiprocessing import Pool
from exp_w2_delta import span_free

EDGE = {frozenset((0, 1)): "AB", frozenset((1, 2)): "BC", frozenset((0, 2)): "CA"}


def gen_dir(imin, imax, tau):
    v = [None, None, None]
    third = ({0, 1, 2} - {imin, imax}).pop()
    v[imin] = 0.0; v[imax] = 1.0; v[third] = float(tau)
    return tuple(v), frozenset((imin, imax))


def min_tiling(u1, u2, u3, N, eps):
    best = (1e9, None)
    for i in range(N + 1):
        r1 = i / N
        if not (eps <= r1 <= 1 - eps):
            continue
        for j in range(N + 1):
            r2 = j / N
            if not (eps <= r2 <= 1 - eps) or r1 + r2 > 1 - eps + 1e-12:
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
                    if not (eps <= r3 <= 1 - eps):
                        continue
                    val = r1 + r2 + r3
                    if val < best[0]:
                        best = (val, (l1, r1, l2, r2, r3))
    return best


def job(args):
    (u1, e1), (u2, e2), (u3, e3), N, eps = args
    ndist = len({e1, e2, e3})
    val, cfg = min_tiling(u1, u2, u3, N, eps)
    return (ndist, val, (u1, u2, u3), cfg)


def main():
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 20
    eps = float(sys.argv[2]) if len(sys.argv) > 2 else 0.12
    import random, statistics
    from collections import defaultdict
    random.seed(5)
    roles = [(0, 1), (1, 0), (0, 2), (2, 0), (1, 2), (2, 1)]
    taus = [0.15, 0.25, 0.35, 0.45, 0.55, 0.65, 0.75, 0.85]

    def rdir():
        im, ix = random.choice(roles)
        return gen_dir(im, ix, random.choice(taus))

    # bucket targets: want enough of each ndist in {1,2,3}
    jobs = []
    want = {1: 150, 2: 150, 3: 300}
    have = defaultdict(int)
    tries = 0
    while sum(have.values()) < sum(want.values()) and tries < 200000:
        tries += 1
        d1, d2, d3 = rdir(), rdir(), rdir()
        nd = len({d1[1], d2[1], d3[1]})
        if have[nd] >= want[nd]:
            continue
        if len({d1[0], d2[0], d3[0]}) < 3:
            continue
        jobs.append((d1, d2, d3, N, eps)); have[nd] += 1

    with Pool() as pool:
        out = pool.map(job, jobs)

    buck = defaultdict(list); below = 0; ex3 = []
    for ndist, val, us, cfg in out:
        if cfg is None:
            buck[(ndist, "noness")].append(1); continue
        buck[ndist].append(val)
        if val < 1 - 1e-6:
            below += 1
            print(f"  !!! essential Sum r<1: {val:.5f} ndist={ndist} u={us} cfg={cfg}")
        if ndist == 3 and val < 1.01:
            ex3.append((val, us, cfg))
    print(f"\nNON-DEGENERATE tight tiling vs #distinct active edges (N={N}, eps={eps}):")
    for nd in (1, 2, 3):
        vs = sorted(buck.get(nd, []))
        noness = len(buck.get((nd, "noness"), []))
        if not vs:
            print(f"  #edges={nd}: NO essential covering found (n_noness={noness})"); continue
        tight = sum(1 for v in vs if v < 1.01)
        print(f"  #edges={nd}: n={len(vs)} (+{noness} w/ no essential cover) "
              f"min={vs[0]:.4f} median={statistics.median(vs):.4f} max={vs[-1]:.4f} "
              f"tight(<1.01)={tight}/{len(vs)} ({tight/len(vs):.0%})")
    print(f"  essential Sum r<1 events: {below}")
    if ex3:
        print("  3-distinct-edge tight examples (val,u,cfg):")
        for e in ex3[:6]:
            print("    ", round(e[0], 4), e[1], tuple(round(x, 3) for x in e[2]))
    else:
        print("  NO 3-distinct-edge triple admitted a tight (<1.01) essential tiling in this sample.")


if __name__ == "__main__":
    main()
