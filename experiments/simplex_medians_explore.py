# R3-2 exploration: does the median theorem extend to the regular d-simplex?
# Triangle medians (cyclic): m_i(e_i)=1/2, m_i(e_{i+1})=0, m_i(e_{i-1})=1.
# Generalize: m_i(e_i)=1/2, m_i(e_{i+1})=0, m_i(e_{i-1})=1, m_i(e_j)=1/2 else. Row sum=(d+1)/2.
# Test: measure mu on 1-skeleton (edges), is pushforward of each m_i uniform on [0,1]?
import numpy as np, itertools
def median_matrix(d):
    n=d+1
    V=np.full((n,n),0.5)
    for i in range(n):
        V[i,i]=0.5
        V[i,(i+1)%n]=0.0
        V[i,(i-1)%n]=1.0
    return V  # row i = vertex-values of m_i ; m_i(x)=sum_j V[i,j] x_j
def check(d, measure='edges', nsamp=400000, bins=20):
    n=d+1; V=median_matrix(d)
    # sample points on chosen skeleton, barycentric
    pts=[]
    rng=np.random.default_rng(0)
    if measure=='edges':
        edges=list(itertools.combinations(range(n),2))
        for _ in range(nsamp):
            a,b=edges[rng.integers(len(edges))]
            t=rng.random(); x=np.zeros(n); x[a]=1-t; x[b]=t; pts.append(x)
    elif measure=='facets':  # uniform on (d-1)-facets: drop one coord =0, uniform on sub-simplex
        for _ in range(nsamp):
            drop=rng.integers(n); x=rng.random(n); x[drop]=0; x/=x.sum(); pts.append(x)
    pts=np.array(pts)
    M=pts@V.T  # each column = m_i values
    ok=True; devs=[]
    for i in range(n):
        hist,_=np.histogram(M[:,i],bins=bins,range=(0,1),density=True)
        dev=np.abs(hist-1).max(); devs.append(dev)
        if dev>0.15: ok=False
    return max(devs), ok
for d in [2,3,4]:
    for meas in ['edges','facets']:
        dev,ok=check(d,meas)
        print(f"d={d} simplex, measure={meas}: max|marginal-1|={dev:.3f} uniform~{ok}")
