#!/usr/bin/env python3
"""3 facets + 1 tilted (f4 = t*x2 + x3): min-sum search with multi-grid verification."""
from __future__ import annotations

import argparse
import sys

import numpy as np
from scipy.optimize import differential_evolution, minimize


def covers(t: float, iv: list[tuple[float, float]], n: int) -> bool:
    u = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1], [0, t, 1]], float)
    for x1 in np.linspace(0, 1, n):
        for x2 in np.linspace(0, 1 - x1, max(2, int(n * (1 - x1)))):
            x = np.array([x1, x2, 1 - x1 - x2])
            f = u @ x
            if all(not (lo <= fa <= hi) for fa, (lo, hi) in zip(f, iv)):
                return False
    return True


def verify_multigrid(t: float, iv: list[tuple[float, float]], grids: list[int]) -> tuple[bool, int]:
    """Return (all_grids_cover, first_failing_n)."""
    for n in grids:
        if not covers(t, iv, n):
            return False, n
    return True, grids[-1]


def uncovered_count(t: float, iv: list[tuple[float, float]], n: int) -> int:
    u = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1], [0, t, 1]], float)
    c = 0
    for x1 in np.linspace(0, 1, n):
        for x2 in np.linspace(0, 1 - x1, max(2, int(n * (1 - x1)))):
            x = np.array([x1, x2, 1 - x1 - x2])
            f = u @ x
            if all(not (lo <= fa <= hi) for fa, (lo, hi) in zip(f, iv)):
                c += 1
    return c


def pack_iv(x: np.ndarray) -> list[tuple[float, float]]:
    a1, a2, a3, c, r1, r2, r3, r4 = x
    return [
        (a1, a1 + r1),
        (a2, a2 + r2),
        (a3, a3 + r3),
        (c, c + r4),
    ]


def _feasible_seed() -> np.ndarray:
    """Known-feasible start: facets [0,0.35]^3 + centered tilted band."""
    return np.array([0.0, 0.0, 0.0, 0.4, 0.35, 0.35, 0.35, 0.35])


def min_sum_search(
    t: float,
    cover_n: int = 80,
    seeds: int = 12,
    maxiter: int = 300,
) -> dict:
    def obj(x: np.ndarray) -> float:
        a1, a2, a3, c, r1, r2, r3, r4 = x
        if any(a + r > 1 + 1e-9 for a, r in [(a1, r1), (a2, r2), (a3, r3)]):
            return 10.0
        if c + r4 > 1 + 1e-9:
            return 10.0
        iv = pack_iv(x)
        if covers(t, iv, cover_n):
            return r1 + r2 + r3 + r4
        return 10.0

    bounds = [(0, 0.95)] * 4 + [(0.01, 0.98)] * 4
    best_x = None
    best = 10.0
    seed0 = _feasible_seed()
    for s in range(seeds):
        res = differential_evolution(
            obj,
            bounds,
            maxiter=maxiter,
            seed=s,
            polish=True,
            tol=0.005,
            x0=seed0 if s == 0 else None,
        )
        if res.fun < best:
            best = res.fun
            best_x = res.x

    if best_x is None or best >= 9.5:
        return {"ok": False, "min_sum": None}

    iv = pack_iv(best_x)
    ok, fail_n = verify_multigrid(t, iv, [cover_n, cover_n + 40, cover_n + 80])
    return {
        "ok": ok,
        "min_sum": float(best),
        "params": best_x,
        "iv": iv,
        "cover_n_opt": cover_n,
        "fail_n": fail_n,
        "uncovered_at_fail": uncovered_count(t, iv, fail_n) if not ok else 0,
    }


def edge_coverage_analysis(t: float, iv: list[tuple[float, float]], n: int = 500) -> dict:
    """Per-edge: min r2+r3+r4 needed to cover edge (facet1=0 on edge x1=0)."""
    (a1, b1), (a2, b2), (a3, b3), (c, d) = iv
    r2, r3, r4 = b2 - a2, b3 - a3, d - c
    s = np.linspace(0, 1, n)
    # edge x1=0: (0,s,1-s)
    g2, g3 = s, 1 - s
    g4 = 1 + (t - 1) * s
    cov = (a2 <= g2) & (g2 <= b2) | (a3 <= g3) & (g3 <= b3) | (c <= g4) & (g4 <= d)
    return {
        "edge_e2e3_frac_covered": float(cov.mean()),
        "edge_e2e3_uncovered": int((~cov).sum()),
        "r234": r2 + r3 + r4,
    }


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--t", type=float, nargs="+", default=[0.25, 0.5, 0.75])
    p.add_argument("--cover-n", type=int, default=80)
    p.add_argument("--seeds", type=int, default=12)
    args = p.parse_args()

    print("3 facets + 1 tilted: min Σrw with multi-grid verification")
    print(f"  optimization cover check: n={args.cover_n}")
    print(f"  verification grids: [{args.cover_n}, {args.cover_n + 40}, {args.cover_n + 80}]")
    print()

    any_fail = False
    for t in args.t:
        r = min_sum_search(t, cover_n=args.cover_n, seeds=args.seeds)
        if r["min_sum"] is None:
            any_fail = True
            print(f"t={t}: no feasible covering found (optimizer)")
        elif not r["ok"]:
            any_fail = True
            print(f"t={t}: OPTIMIZER sum={r['min_sum']:.6f}  FAILS grid n={r['fail_n']} "
                  f"({r['uncovered_at_fail']} uncovered)")
        else:
            ed = edge_coverage_analysis(t, r["iv"])
            print(
                f"t={t}: min Σrw={r['min_sum']:.6f}  verified to n={args.cover_n + 80}  "
                f"edge e2-e3 cover={ed['edge_e2e3_frac_covered']:.4f}"
            )
            print(f"       intervals: r=({r['params'][4]:.4f},{r['params'][5]:.4f},"
                  f"{r['params'][6]:.4f},{r['params'][7]:.4f})  "
                  f"a=({r['params'][0]:.3f},{r['params'][1]:.3f},{r['params'][2]:.3f})  "
                  f"c={r['params'][3]:.3f}")

    return 1 if any_fail else 0


if __name__ == "__main__":
    sys.exit(main())
