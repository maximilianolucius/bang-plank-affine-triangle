#!/usr/bin/env python3
"""
M1' numerical validation (pure Python, no deps).

Checks, for the SHIFTED symmetric system of the working notes:
  Psi_m(x) = 1/2 |x|^2 - sum_j p_j log|<v_j,x> - m_j|
  grad = x - sum_j p_j v_j / (<v_j,x> - m_j) = 0
  system in y=<v_j,x>:  h_j(y) = (y_j - m_j)(A y)_j - p_j = 0,  A = G^{-1}, G Gram.

Claims tested:
  (C2) exactly 2^n real critical points (one per sign chamber), all distinct/simple
  (C4) det J_h = (prod_j (y_j - m_j)) * det(A + diag(p_j/(y_j-m_j)^2))
  (eq3) |u|^2 = 1 + sum_j p_j m_j/(y_j - m_j)   (broken homogeneity sanity check)
Run with several random instances and several n.
"""
import math, random

# ---------- tiny linear algebra (pure python) ----------
def matvec(M, v): return [sum(M[i][k]*v[k] for k in range(len(v))) for i in range(len(M))]
def matmul(A,B):
    n,m,p=len(A),len(B),len(B[0])
    return [[sum(A[i][k]*B[k][j] for k in range(m)) for j in range(p)] for i in range(n)]
def transpose(M): return [[M[j][i] for j in range(len(M))] for i in range(len(M[0]))]
def ident(n): return [[1.0 if i==j else 0.0 for j in range(n)] for i in range(n)]

def lu_solve(Ain, bin_):
    """Solve A x = b by Gaussian elimination with partial pivoting. Returns x."""
    n=len(Ain); A=[row[:] for row in Ain]; b=bin_[:]
    for col in range(n):
        piv=max(range(col,n), key=lambda r: abs(A[r][col]))
        if abs(A[piv][col])<1e-14: raise ValueError("singular")
        A[col],A[piv]=A[piv],A[col]; b[col],b[piv]=b[piv],b[col]
        for r in range(col+1,n):
            f=A[r][col]/A[col][col]
            for c in range(col,n): A[r][c]-=f*A[col][c]
            b[r]-=f*b[col]
    x=[0.0]*n
    for i in range(n-1,-1,-1):
        x[i]=(b[i]-sum(A[i][c]*x[c] for c in range(i+1,n)))/A[i][i]
    return x

def inverse(A):
    n=len(A); cols=[]
    for j in range(n):
        e=[1.0 if i==j else 0.0 for i in range(n)]
        cols.append(lu_solve(A,e))
    # cols[j] is j-th column of inverse
    return [[cols[j][i] for j in range(n)] for i in range(n)]

def det(Ain):
    n=len(Ain); A=[row[:] for row in Ain]; d=1.0
    for col in range(n):
        piv=max(range(col,n), key=lambda r: abs(A[r][col]))
        if abs(A[piv][col])<1e-15: return 0.0
        if piv!=col: A[col],A[piv]=A[piv],A[col]; d=-d
        d*=A[col][col]
        for r in range(col+1,n):
            f=A[r][col]/A[col][col]
            for c in range(col,n): A[r][c]-=f*A[col][c]
    return d

# ---------- problem setup ----------
def run_instance(n, seed):
    rng=random.Random(seed)
    # random unit vectors v_j in R^n (basis, generic)
    V=[]  # V[j] = v_j
    for j in range(n):
        w=[rng.gauss(0,1) for _ in range(n)]
        nrm=math.sqrt(sum(c*c for c in w)); V.append([c/nrm for c in w])
    Vt=transpose(V)            # columns are v_j ; Vt[i][j] = (v_j)_i
    G=[[sum(V[i][k]*V[j][k] for k in range(n)) for j in range(n)] for i in range(n)]  # Gram
    A=inverse(G)
    m=[rng.uniform(-0.8,0.8) for _ in range(n)]
    raw=[rng.uniform(0.2,1.0) for _ in range(n)]; s=sum(raw); p=[r/s for r in raw]  # sum p=1

    def yvec(x): return [sum(V[j][k]*x[k] for k in range(n)) for j in range(n)]  # y_j=<v_j,x>
    def psi(x):
        y=yvec(x); val=0.5*sum(c*c for c in x)
        for j in range(n):
            d=y[j]-m[j]
            if d==0.0: return float('inf')
            val-=p[j]*math.log(abs(d))
        return val
    def grad(x):
        y=yvec(x); g=x[:]
        for j in range(n):
            d=y[j]-m[j];
            for k in range(n): g[k]-=p[j]*V[j][k]/d
        return g
    def hess(x):
        y=yvec(x); H=ident(n)
        for j in range(n):
            d=y[j]-m[j]; c=p[j]/(d*d)
            for a in range(n):
                for b in range(n): H[a][b]+=c*V[j][a]*V[j][b]
        return H
    def newton(x0):
        # damped Newton with Armijo backtracking on the (convex) value psi.
        x=x0[:]; sgn=[1 if (yvec(x0)[j]-m[j])>0 else -1 for j in range(n)]
        for _ in range(300):
            g=grad(x); H=hess(x)
            if max(abs(c) for c in g)<1e-13: break
            try: step=lu_solve(H,g)
            except ValueError: return None
            f0=psi(x); slope=sum(g[k]*step[k] for k in range(n))  # d/dt psi(x - t step) at 0 = -slope
            t=1.0; xn=x
            for _ in range(80):
                xn=[x[k]-t*step[k] for k in range(n)]
                yn=yvec(xn)
                inside=all((yn[j]-m[j])*sgn[j]>0 for j in range(n))  # stay in chamber
                if inside and psi(xn)<=f0-1e-4*t*slope: break
                t*=0.5
            else:
                break  # line search failed; stop
            x=xn
        return x

    # one (robust) start per sign chamber; retry failed chambers with several offsets
    rng2=random.Random(seed*7919+1)
    found={}  # sign-pattern tuple -> solution
    scales=(0.5,1.0,2.0,0.25,4.0,8.0,0.1,16.0)
    for mask in range(2**n):
        eps=tuple(1 if (mask>>j)&1 else -1 for j in range(n))
        if eps in found: continue
        tries=0
        while eps not in found and tries<40:
            scale=scales[tries%len(scales)]
            offs=[eps[j]*scale*(0.5+1.5*rng2.random()) for j in range(n)]
            x0=lu_solve(V,[m[j]+offs[j] for j in range(n)])
            sol=newton(x0); tries+=1
            if sol is not None and max(abs(c) for c in grad(sol))<1e-7:
                y=yvec(sol); sp=tuple(1 if (y[j]-m[j])>0 else -1 for j in range(n))
                found[sp]=sol
    uniq=list(found.values())

    # verify h(y)=0, det J_h identity, eq(3)
    max_h=0.0; max_jac_err=0.0; max_eq3=0.0
    for x in uniq:
        y=yvec(x); Ay=matvec(A,y)
        h=[(y[j]-m[j])*Ay[j]-p[j] for j in range(n)]; max_h=max(max_h,max(abs(c) for c in h))
        # J_h = diag(Ay) + diag(y-m) A
        Jh=[[ (Ay[i] if i==j else 0.0) + (y[i]-m[i])*A[i][j] for j in range(n)] for i in range(n)]
        lhs=det(Jh)
        Pm=1.0
        for j in range(n): Pm*=(y[j]-m[j])
        M2=[[A[i][j] + (p[i]/((y[i]-m[i])**2) if i==j else 0.0) for j in range(n)] for i in range(n)]
        rhs=Pm*det(M2)
        max_jac_err=max(max_jac_err, abs(lhs-rhs)/(abs(lhs)+1e-12))
        nrm2=sum(c*c for c in x); pred=1.0+sum(p[j]*m[j]/(y[j]-m[j]) for j in range(n))
        max_eq3=max(max_eq3, abs(nrm2-pred))
    return len(uniq), 2**n, max_h, max_jac_err, max_eq3

print(f"{'n':>2} {'seed':>5} {'#crit':>6} {'2^n':>5} {'max|h|':>10} {'jac_relerr':>11} {'eq3_err':>10}")
ok=True
for n in (2,3,4,5):
    for seed in range(4):
        ncrit,expected,mh,mj,me=run_instance(n,seed)
        flag="" if (ncrit==expected and mh<1e-7 and mj<1e-7 and me<1e-7) else "  <-- FAIL"
        if flag: ok=False
        print(f"{n:>2} {seed:>5} {ncrit:>6} {expected:>5} {mh:>10.2e} {mj:>11.2e} {me:>10.2e}{flag}")
print("\nALL CHECKS PASSED" if ok else "\nSOME CHECKS FAILED")
