#!/usr/bin/env python3
"""
Explore Hunter (1993) edge parameters and whether m=4 admits a closed identity.

NOT a proof — algebraic/numerical exploration only.
"""
from __future__ import annotations

import itertools
from dataclasses import dataclass

import numpy as np
from scipy.optimize import linprog, minimize


# ---------------------------------------------------------------------------
# Equilateral triangle model (Hunter Fig. 2 style)
# Vertices at unit circle angles 90°, 210°, 330°; side length 1 after affine map.
# ---------------------------------------------------------------------------
SQ3 = np.sqrt(3)


def equilateral_vertices() -> np.ndarray:
    """3 vertices in R^2, side length 1."""
    return np.array(
        [
            [0.0, 0.0],
            [1.0, 0.0],
            [0.5, SQ3 / 2],
        ]
    )


def triangle_width(V: np.ndarray, u: np.ndarray) -> float:
    p = V @ u
    return float(p.max() - p.min())


@dataclass
class Plank:
    u: np.ndarray  # unit normal
    center: float  # ⟨u, x⟩ at center
    rw: float

    @property
    def width(self) -> float:
        return self.rw  # relative to equilateral unit-side triangle in Hunter setup


def plank_covers(V: np.ndarray, p: Plank, x: np.ndarray) -> bool:
    val = float(p.u @ x)
    w = p.rw * triangle_width(V, p.u)
    return abs(val - p.center) <= w / 2 + 1e-12


def covers_triangle(V: np.ndarray, planks: list[Plank], grid_n: int = 80) -> bool:
    xs = np.linspace(0, 1, grid_n)
    ys = np.linspace(0, 1, grid_n)
    for x in xs:
        for y in ys:
            pt = np.array([x, y, 0.0])  # wrong — use barycentric on 2D triangle
    # barycentric grid on V
    for a in np.linspace(0, 1, grid_n):
        for b in np.linspace(0, 1 - a, max(2, int(grid_n * (1 - a)))):
            x = (1 - a - b) * V[0] + a * V[1] + b * V[2]
            if not any(plank_covers(V, p, x) for p in planks):
                return False
    return True


def random_planks(m: int, sum_rw: float, rng: np.random.Generator) -> list[Plank]:
    V = equilateral_vertices()
    angles = rng.uniform(0, 2 * np.pi, m)
    U = np.stack([np.cos(angles), np.sin(angles)], axis=1)
    fracs = rng.dirichlet(np.ones(m)) * sum_rw
    planks = []
    for i in range(m):
        u = U[i]
        w_T = triangle_width(V, u)
        rw = fracs[i]
        w = rw * w_T
        projs = V @ u
        lo, hi = projs.min(), projs.max()
        c = rng.uniform(lo + w / 2, hi - w / 2)
        planks.append(Plank(u=u, center=c, rw=rw))
    return planks


# ---------------------------------------------------------------------------
# Cubical / vector model on standard 2-simplex
# ---------------------------------------------------------------------------
def random_cubical_config(
    m: int, sum_rw: float, rng: np.random.Generator
) -> tuple[np.ndarray, list[tuple[float, float]]]:
    """
    Build U (m x 3) with each row min=0 max=1 on vertices e1,e2,e3,
    and intervals I_a of total length sum_rw.
    """
    U = np.zeros((m, 3))
    for a in range(m):
        perm = rng.permutation(3)
        U[a, perm[0]] = 0.0
        U[a, perm[2]] = 1.0
        U[a, perm[1]] = rng.uniform(0, 1)
    lengths = rng.dirichlet(np.ones(m)) * sum_rw
    intervals = []
    for a in range(m):
        L = lengths[a]
        lo = rng.uniform(0, 1 - L)
        intervals.append((lo, lo + L))
    return U, intervals


def eval_f(U: np.ndarray, x: np.ndarray) -> np.ndarray:
    return U @ x


def vector_covers(U: np.ndarray, intervals: list[tuple[float, float]], grid_n: int = 60) -> bool:
    for x1 in np.linspace(0, 1, grid_n):
        for x2 in np.linspace(0, 1 - x1, max(2, int(grid_n * (1 - x1)))):
            x3 = 1 - x1 - x2
            x = np.array([x1, x2, x3])
            f = eval_f(U, x)
            if all(not (lo <= fa <= hi) for fa, (lo, hi) in zip(f, intervals)):
                return False
    return True


def min_cover_sum_ilp(
    U: np.ndarray, rng: np.random.Generator, n_intervals_per_coord: int = 12
) -> tuple[float, list[tuple[float, float]], bool]:
    """
    Exact minimum sum of interval lengths for fixed directions U via set-cover ILP
    on a discretized simplex (necessary lower bound on true minimum; exact if grid fine).

    Variables: choose intervals on [0,1] discretized; minimize sum lengths s.t. all grid pts covered.
    Simplified: for each direction a, interval is [t_a, t_a + r_a]; discretize t_a on grid.
    """
    m = U.shape[0]
    grid_pts = []
    g = 25
    for x1 in np.linspace(0, 1, g):
        for x2 in np.linspace(0, 1 - x1, max(1, int(g * (1 - x1)))):
            grid_pts.append(np.array([x1, x2, 1 - x1 - x2]))
    grid_pts = np.array(grid_pts)
    F = grid_pts @ U.T  # (N, m)

    # For each plank a, candidate intervals: start positions on grid
    candidates = []
    for a in range(m):
        vals = F[:, a]
        vmin, vmax = vals.min(), vals.max()
        step = (vmax - vmin) / n_intervals_per_coord
        for k in range(n_intervals_per_coord):
            lo = vmin + k * step
            for L in np.linspace(0.05, 1.0, 20):
                hi = lo + L
                covered = (vals >= lo - 1e-9) & (vals <= hi + 1e-9)
                if covered.any():
                    candidates.append((a, lo, hi, L, covered))

    # Set cover: pick one candidate per... actually each candidate is (plank, interval)
    # Standard set cover: universe = grid points, sets = candidates
    # We can pick MULTIPLE candidates for same plank? No — one interval per plank.
    # Decision: choose one interval per plank a.
    best = np.inf
    best_iv = None
    best_ok = False
    # brute over interval choices (small m)
    per_plank = [[] for _ in range(m)]
    for c in candidates:
        per_plank[c[0]].append(c)

    for choice in itertools.product(*[per_plank[a] if per_plank[a] else [None] for a in range(m)]):
        if any(c is None for c in choice):
            continue
        covered = np.zeros(len(grid_pts), dtype=bool)
        total = 0.0
        ivs = []
        for c in choice:
            a, lo, hi, L, cov = c
            covered |= cov
            total += L
            ivs.append((lo, hi))
        if covered.all():
            if total < best:
                best = total
                best_iv = ivs
                best_ok = True
    return best, best_iv or [], best_ok


# ---------------------------------------------------------------------------
# 3 facets + 1 tilted — structured partial case
# ---------------------------------------------------------------------------
def facet_plus_tilted_min_sum(
    tilt_middle: float, rng: np.random.Generator, trials: int = 200
) -> dict:
    """
    U = [I_3; ũ] with ũ = (0, tilt_middle, 1) normalized pattern (0, t, 1).
  """
    results = []
    for _ in range(trials):
        t = tilt_middle
        U = np.array(
            [
                [1, 0, 0],
                [0, 1, 0],
                [0, 0, 1],
                [0, t, 1],
            ]
        )
        s, ivs, ok = min_cover_sum_ilp(U, rng, n_intervals_per_coord=8)
        results.append(s if ok else np.nan)
    arr = np.array([r for r in results if not np.isnan(r)])
    return {
        "tilt_middle": tilt_middle,
        "min_sum_mean": float(arr.mean()) if len(arr) else np.nan,
        "min_sum_min": float(arr.min()) if len(arr) else np.nan,
        "n_ok": len(arr),
    }


def hunter_T_S_identity_check(rng: np.random.Generator, n: int = 5000) -> dict:
    """
    Hunter: for 3 planks on equilateral triangle, (2-T)(2-S)=1 and R-1=(1-T)(S-1).
    Reproduce numerically from random feasible (t1,t2,t3) in (0,1) with t1+t2+t3=T<3/2.
    Uses sympy-free closed form from Hunter's cyclic formulas (approximate via search).
    """
    # We don't have closed s_i(t) here; instead sample random 3-plank configs and
    # measure R, T from edge intersections numerically.
    V = equilateral_vertices()
    edges = [(0, 1), (1, 2), (2, 0)]
    violations = 0
    checked = 0
    for _ in range(n):
        planks = random_planks(3, sum_rw=rng.uniform(0.5, 1.5), rng=rng)
        # edge segment lengths t_i: where plank lines cut edge i
        ts = []
        for (i, j) in edges:
            seg_len = 1.0  # unit side
            # approximate: fraction of edge covered by union of plank strips projected
            ts.append(rng.uniform(0, 0.5))  # placeholder — full geometry omitted
        T = sum(ts)
        R = sum(p.rw for p in planks)
        if R < 1 - 1e-6 and covers_triangle(V, planks, grid_n=30):
            violations += 1
        checked += 1
    return {"violations_R_lt_1_but_covers": violations, "checked": checked}


def main():
    rng = np.random.default_rng(0)
    print("=== Cubical ILP min sum (m=4 random directions) ===")
    for _ in range(5):
        U, _ = random_cubical_config(4, sum_rw=0.95, rng=rng)
        s, ivs, ok = min_cover_sum_ilp(U, rng)
        print(f"  sum_rw target 0.95 -> min covering sum ≈ {s:.4f} (ok={ok})")

    print("\n=== 3 facets + 1 tilted (0,t,1) — ILP min sum (coarse) ===")
    for t in [0.2, 0.5, 0.8]:
        d = facet_plus_tilted_min_sum(t, rng)
        print(f"  t={t}: min_sum_min={d['min_sum_min']:.4f} over {d['n_ok']} trials")

    print("\n=== Random m=4, sum=0.95, vector covers? ===")
    fails = 0
    for _ in range(100):
        U, ivs = random_cubical_config(4, 0.95, rng)
        if vector_covers(U, ivs, grid_n=40):
            fails += 1
    print(f"  grid covers with sum=0.95: {fails}/100 (expect 0 if conjecture true)")

    print("\nDone (exploration only, not proof).")


if __name__ == "__main__":
    main()
