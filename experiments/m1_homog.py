#!/usr/bin/env python3
"""
M1' — empirical exploration of the (n+1)-homogenization route (pure Python).

Affine planks in R^n:  f_j(x) = <v_j,x> - m_j,  ||v_j||=1,  want |f_j(ubar)|>=w_j.
Homogenize to R^{N}, N=n+1, with UNIT vectors:
    W_0 = e_0                         (form L_0 = x_0)
    W_j = (-m_j, v_j)/sqrt(1+m_j^2)   (form L_j = <v_j,x> - m_j x_0, normalized)
Apply the CENTERED M-OM strong-polarization engine to W_0..W_n with weights q_a>0,
sum q_a = 1:  there is a unit U in S^{N-1} with  sum_a q_a^2/<W_a,U>^2 <= 1.
The witness is the critical point (of the convex potential on the sphere) that
realizes the bound.  De-homogenize: U=(U0, x), ubar = x/U0.

Question: with EQUAL weights q_a = 1/N = 1/(n+1), does ubar land in the unit ball,
and is min_j |f_j(ubar)| >= 1/(n+1) (Ball's corollary margin)?  Report empirically.
"""
import math, random
def lu_solve(Ain,bin_):
    n=len(Ain);A=[r[:] for r in Ain];b=bin_[:]
    for c in range(n):
        p=max(range(c,n),key=lambda r:abs(A[r][c]))
        if abs(A[p][c])<1e-15: raise ValueError("sing")
        A[c],A[p]=A[p],A[c];b[c],b[p]=b[p],b[c]
        for r in range(c+1,n):
            f=A[r][c]/A[c][c]
            for k in range(c,n):A[r][k]-=f*A[c][k]
            b[r]-=f*b[c]
    x=[0.0]*n
    for i in range(n-1,-1,-1): x[i]=(b[i]-sum(A[i][k]*x[k] for k in range(i+1,n)))/A[i][i]
    return x

def explore(n, seed):
    rng=random.Random(seed); N=n+1
    # unit v_j in R^n
    v=[]
    for j in range(n):
        w=[rng.gauss(0,1) for _ in range(n)]; nr=math.sqrt(sum(c*c for c in w)); v.append([c/nr for c in w])
    m=[rng.uniform(-0.8,0.8) for _ in range(n)]
    # unit vectors W_a in R^N (index 0..n); coordinate 0 is x_0
    W=[]
    W.append([1.0]+[0.0]*n)                       # W_0 = e_0
    for j in range(n):
        d=math.sqrt(1.0+m[j]*m[j])
        W.append([-m[j]/d]+[v[j][k]/d for k in range(n)])   # W_{j+1}
    q=[1.0/N]*N                                   # equal weights 1/(n+1)
    def inner(a,U): return sum(W[a][k]*U[k] for k in range(N))
    def grad(U):
        g=U[:]
        for a in range(N):
            d=inner(a,U)
            for k in range(N): g[k]-=q[a]*W[a][k]/d
        return g
    def hess(U):
        H=[[1.0 if i==j else 0.0 for j in range(N)] for i in range(N)]
        for a in range(N):
            d=inner(a,U); c=q[a]/(d*d)
            for i in range(N):
                for j in range(N): H[i][j]+=c*W[a][i]*W[a][j]
        return H
    def psi(U):
        val=0.5*sum(c*c for c in U)
        for a in range(N):
            d=inner(a,U)
            if d==0: return float('inf')
            val-=q[a]*math.log(abs(d))
        return val
    def newton(U0):
        U=U0[:]; sgn=[1 if inner(a,U0)>0 else -1 for a in range(N)]
        for _ in range(400):
            g=grad(U)
            if max(abs(c) for c in g)<1e-12: break
            try: step=lu_solve(hess(U),g)
            except ValueError: return None
            f0=psi(U); slope=sum(g[k]*step[k] for k in range(N)); t=1.0
            for _ in range(100):
                Un=[U[k]-t*step[k] for k in range(N)]
                if all(inner(a,Un)*sgn[a]>0 for a in range(N)) and psi(Un)<=f0-1e-4*t*slope: break
                t*=0.5
            else: break
            U=Un
        return U
    # find the witness: among critical points (one per sign chamber of <W_a,.>),
    # the one with strong-sum <= 1. Wmatrix rows are W_a (a basis of R^N).
    best=None; best_sum=None
    for mask in range(2**N):
        eps=[1 if (mask>>a)&1 else -1 for a in range(N)]
        U0=lu_solve(W,[eps[a]*1.0 for a in range(N)])   # <W_a,U0>=eps_a
        U=newton(U0)
        if U is None or max(abs(c) for c in grad(U))>1e-6: continue
        S=sum(q[a]**2/inner(a,U)**2 for a in range(N))
        if best_sum is None or S<best_sum: best_sum=S; best=U
    if best is None: return None
    U=best; U0coord=U[0]; x=U[1:]
    if abs(U0coord)<1e-12: return ("U0~0",)
    sgn=1.0 if U0coord>0 else -1.0
    ubar=[sgn*x[k]/abs(U0coord) for k in range(n)]
    normub=math.sqrt(sum(c*c for c in ubar))
    margins=[abs(sum(v[j][k]*ubar[k] for k in range(n))-m[j]) for j in range(n)]
    return dict(strong_sum=best_sum, U0=abs(U0coord), normub=normub,
                min_margin=min(margins), inv_np1=1.0/N,
                in_ball=(normub<=1.0+1e-9), margin_ok=(min(margins)>=1.0/N-1e-9))

print(f"{'n':>2} {'seed':>4} {'strongSum<=1':>12} {'|U0|':>7} {'||ubar||':>9} {'min_margin':>11} {'1/(n+1)':>8} {'inBall?':>8} {'marginOK?':>9}")
for n in (2,3,4,5):
    for seed in range(5):
        r=explore(n,seed)
        if r is None: print(f"{n:>2} {seed:>4}  (no witness)"); continue
        print(f"{n:>2} {seed:>4} {r['strong_sum']:>12.4f} {r['U0']:>7.3f} {r['normub']:>9.3f} "
              f"{r['min_margin']:>11.4f} {r['inv_np1']:>8.4f} {str(r['in_ball']):>8} {str(r['margin_ok']):>9}")
