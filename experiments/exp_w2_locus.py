r"""
EXP-A/B: map the tight LOCUS. For each (orient,a1,a2,s) compute the minimal gap over
placements (R>0). Tight directions (min gap ~ 0) are the extremal locus; elsewhere
there is strictly positive slack. Float search, parallel.
"""
import sys
from multiprocessing import Pool
from exp_w2_delta import span_free


def dir_min_gap(args):
    orient, a1, a2, s, N = args
    g1v = (0.0, 1.0, a1)
    g2v = (0.0, 1.0, a2) if orient == "SAME" else (1.0, 0.0, a2)
    fv = (0.0, s, 1.0)
    step = 1.0 / N
    best = 1e9
    for ir1 in range(0, N):
        r1 = ir1 * step
        for ir2 in range(0, N):
            r2 = ir2 * step
            R = r1 + r2
            if R >= 1 - 1e-12 or ir1 + ir2 < 2:
                continue
            for il1 in range(0, N - ir1 + 1):
                l1 = il1 * step
                for il2 in range(0, N - ir2 + 1):
                    l2 = il2 * step
                    res = span_free(g1v, g2v, fv, l1, r1, l2, r2, exact=False)
                    if res is None:
                        return (orient, a1, a2, s, -9.0)  # free empty
                    if res["gap"] < best:
                        best = res["gap"]
    return (orient, a1, a2, s, best)


def main():
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 22
    M = int(sys.argv[2]) if len(sys.argv) > 2 else 8
    avs = [k / M for k in range(0, M + 1)]
    svs = [k / M for k in range(0, M + 1)]
    for orient in ("SAME", "OPP"):
        jobs = [(orient, a1, a2, s, N) for a1 in avs for a2 in avs for s in svs if abs(a1 - a2) > 1e-9]
        with Pool() as pool:
            out = pool.map(dir_min_gap, jobs)
        tights = [o for o in out if o[4] < 1e-4]
        print(f"\n===== {orient}: {len(tights)}/{len(out)} directions are TIGHT (min gap<1e-4) =====")
        # characterize tight locus by s and by a-values
        s_tight = sorted(set(round(o[3], 3) for o in tights))
        print("  s-values that appear in tight locus:", s_tight)
        # for each s, which a-pairs are tight
        for s in svs:
            at = [(round(o[1], 3), round(o[2], 3)) for o in tights if abs(o[3] - s) < 1e-9]
            if at:
                print(f"   s={s:.3f}: tight (a1,a2) pairs: {sorted(at)[:12]}{' ...' if len(at)>12 else ''} (n={len(at)})")
        # min gap over ALL directions (should be ~0)
        gmin = min(o[4] for o in out)
        print(f"  overall min gap = {gmin:+.6f}")


if __name__ == "__main__":
    main()
