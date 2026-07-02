r"""
P-A step 1: ell(u) = longest chord of K parallel to u; verify ell/w formula for the
equilateral triangle, numerically (all directions) and symbolically (one sector).
"""
import numpy as np
import sympy as sp

A = np.array([0.0, 0.0]); B = np.array([1.0, 0.0]); C = np.array([0.5, np.sqrt(3)/2])
V = [A, B, C]


def formula(tau):
    return 2*(tau**2 - tau + 1)/(2 - tau) if tau <= 0.5 else 2*(tau**2 - tau + 1)/(1 + tau)


def ell_w_tau(theta):
    u = np.array([np.cos(theta), np.sin(theta)])
    wp = np.array([-np.sin(theta), np.cos(theta)])
    phi = [u @ v for v in V]
    w = max(phi) - min(phi)
    sp_ = sorted(phi); tau = (sp_[1]-sp_[0])/(sp_[2]-sp_[0])
    sperp = [wp @ v for v in V]
    mid = int(np.argsort(sperp)[1])
    others = [i for i in range(3) if i != mid]
    Vm, Pa, Pb = V[mid], V[others[0]], V[others[1]]
    M = np.array([[u[0], -(Pb-Pa)[0]], [u[1], -(Pb-Pa)[1]]])
    t, s = np.linalg.solve(M, Pa - Vm)
    return abs(t), w, abs(t)/w, tau


def numeric_check(n=3600):
    maxerr = 0
    for k in range(1, n):
        th = k*np.pi/(n/2)
        try:
            _, _, ratio, tau = ell_w_tau(th)
        except np.linalg.LinAlgError:
            continue
        maxerr = max(maxerr, abs(ratio - formula(tau)))
    mn = min(ell_w_tau(th)[2] for th in np.linspace(0.001, np.pi, 100000))
    return maxerr, mn


def symbolic_check():
    th = sp.symbols('theta', positive=True)
    s3 = sp.sqrt(3); cos, sin = sp.cos(th), sp.sin(th)
    w = sp.Rational(1, 2)*cos + s3/2*sin
    tau = cos/w
    ell = (s3/2)/sin
    ratio = ell/w
    diff = sp.simplify(ratio - 2*(tau**2 - tau + 1)/(2 - tau))
    return diff


if __name__ == "__main__":
    err, mn = numeric_check()
    print(f"[numeric] max|ell/w - formula| = {err:.2e}  min ell/w = {mn:.6f}  "
          f"(4*sqrt3-6 = {4*np.sqrt(3)-6:.6f})")
    d = symbolic_check()
    print(f"[symbolic] ell/w - formula(tau) simplifies to: {d}  -> identity holds: {d == 0}")
