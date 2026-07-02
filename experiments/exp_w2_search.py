r"""
EXP-A/B (corrected engine): map the extremal (tight) set of common-edge W_2.
Float bulk search (parallel) + exact certification of the minimizer.

g1=(0,1,a1).  SAME: g2=(0,1,a2).  OPP: g2=(1,0,a2).  target f=(0,s,1).
Reports per (orient): global min gap (and whether <0 -> counterexample!), the
minimizer cfg + witness points (argmin/argmax), fraction tight, fraction inf>0.
"""
import sys
from collections import Counter
from multiprocessing import Pool
from fractions import Fraction as Q
from exp_w2_delta import span_free


def classify_pt(p, tol=1e-6):
    y, z = p
    names = {(0, 0): "A=(0,0)", (1, 0): "B=(1,0)", (0, 1): "C=(0,1)"}
    for (vy, vz), nm in names.items():
        if abs(y - vy) < tol and abs(z - vz) < tol:
            return nm
    on = []
    if abs(y) < tol: on.append("y=0")
    if abs(z) < tol: on.append("z=0")
    if abs(y + z - 1) < tol: on.append("y+z=1")
    return ("edge:" + "&".join(on)) if on else f"int({y:.3f},{z:.3f})"


def search_dir(args):
    orient, a1, a2, s, N = args
    g1v = (0.0, 1.0, a1)
    g2v = (0.0, 1.0, a2) if orient == "SAME" else (1.0, 0.0, a2)
    fv = (0.0, s, 1.0)
    step = 1.0 / N
    best = (1e9, None, None)
    n_tight = 0; n_pos_inf = 0; n_tot = 0
    for ir1 in range(0, N):
        r1 = ir1 * step
        for ir2 in range(0, N):
            r2 = ir2 * step
            R = r1 + r2
            if R >= 1.0 - 1e-12:
                continue
            for il1 in range(0, N - ir1 + 1):
                l1 = il1 * step
                for il2 in range(0, N - ir2 + 1):
                    l2 = il2 * step
                    res = span_free(g1v, g2v, fv, l1, r1, l2, r2, exact=False)
                    if res is None:
                        return ("FREE_EMPTY", orient, (a1, a2, s), (l1, r1, l2, r2))
                    n_tot += 1
                    gap = res["gap"]
                    if R >= 1.5 * step and gap < best[0]:
                        best = (gap, (l1, r1, l2, r2), (res["argmin"], res["argmax"]))
                    if gap < 1e-9 and R >= 1.5 * step:
                        n_tight += 1
                    if res["fmin"] > 1e-9:
                        n_pos_inf += 1
    return (orient, (a1, a2, s), best, n_tight, n_pos_inf, n_tot)


def main():
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 28
    avs = [k / 8 for k in range(0, 9)]
    svs = [k / 8 for k in range(0, 8)]  # include s=0
    for orient in ("SAME", "OPP"):
        jobs = [(orient, a1, a2, s, N) for a1 in avs for a2 in avs for s in svs]
        with Pool() as pool:
            out = pool.map(search_dir, jobs)
        empties = [o for o in out if o[0] == "FREE_EMPTY"]
        good = [o for o in out if o[0] != "FREE_EMPTY"]
        good.sort(key=lambda o: o[2][0])
        gmin = good[0][2][0]
        tot_tight = sum(o[3] for o in good)
        tot_posinf = sum(o[4] for o in good)
        tot = sum(o[5] for o in good)
        print(f"\n===== {orient} N={N} jobs={len(jobs)} FREE_EMPTY={len(empties)} =====")
        if empties:
            print("  !!! FREE_EMPTY (Bang(3) violation candidate):", empties[:3])
        print(f"  global min gap (R>0) = {gmin:+.6f}  (negative => W_2 counterexample)")
        print(f"  tight configs (gap<1e-9,R>0): {tot_tight}/{tot} = {tot_tight/tot:.3%}")
        print(f"  inf_F f>0 configs: {tot_posinf}/{tot} = {tot_posinf/tot:.3%}")
        print("  examples of tightest dirs (min gap, witnesses):")
        for o in good[:8]:
            _, (a1, a2, s), best, *_ = o
            gap, cfg, wit = best
            if wit is None:
                continue
            print(f"    (a1,a2,s)=({a1:.3f},{a2:.3f},{s:.3f}) gap={gap:+.6f} "
                  f"cfg(l1,r1,l2,r2)={tuple(round(x,3) for x in cfg)} "
                  f"min@{classify_pt(wit[0])} max@{classify_pt(wit[1])}")


if __name__ == "__main__":
    main()
