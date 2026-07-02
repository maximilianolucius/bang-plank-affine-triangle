# R3-2: LP feasibility - does SOME measure on Delta^d give uniform marginals in the d+1
# cyclic medians? (like notes/37 for the triangle). Necessary cond (concurrency, sum=(d+1)/2)
# holds by construction; this tests full sufficiency.
import numpy as np, itertools
from scipy.optimize import linprog
def median_matrix(d):
    n=d+1; V=np.full((n,n),0.5)
    for i in range(n):
        V[i,(i+1)%n]=0.0; V[i,(i-1)%n]=1.0; V[i,i]=0.5
    return V
def feasible(d, G=12, K=8):
    n=d+1; V=median_matrix(d)
    # grid of barycentric points with denominator G
    pts=[np.array(c)/G for c in itertools.product(range(G+1),repeat=n) if sum(c)==G]
    pts=np.array(pts); Npt=len(pts)
    M=pts@V.T  # Npt x n median values
    # variables: mass on each grid point >=0, sum=1; each median binned into K bins must have mass 1/K
    A_eq=[]; b_eq=[]
    for i in range(n):
        b=np.clip((M[:,i]*K).astype(int),0,K-1)
        for k in range(K):
            row=(b==k).astype(float); A_eq.append(row); b_eq.append(1.0/K)
    A_eq.append(np.ones(Npt)); b_eq.append(1.0)
    res=linprog(c=np.zeros(Npt),A_eq=np.array(A_eq),b_eq=np.array(b_eq),bounds=(0,None),method='highs')
    return res.success, Npt
for d in [2,3,4]:
    for K in [6,10]:
        ok,Npt=feasible(d,G=(10 if d<=3 else 7),K=K)
        print(f"d={d} (Npts={Npt}), K={K} bins: uniform-marginal measure exists? {ok}")
