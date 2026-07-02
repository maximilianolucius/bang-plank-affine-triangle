# R5-3 THEOREM CHECK: weighted-perimeter measure for the CYCLIC concurrent family.
# Directions u1=(t1,0,1), u2=(0,1,t2), u3=(1,t3,0) concurrent at interior p:
#   t1=(1/2-pC)/pA, t2=(1/2-pB)/pC, t3=(1/2-pA)/pB.
# Claim: measure = uniform on each edge with masses  w_AB=1-2pC, w_BC=1-2pA, w_CA=1-2pB
# has uniform marginal under each u_i. Symbolic + Monte Carlo verification.
import sympy as sp
pA,pB,pC=sp.symbols('pA pB pC',positive=True)
pC_expr=1-pA-pB
t1=(sp.Rational(1,2)-pC_expr)/pA
t2=(sp.Rational(1,2)-pB)/pC_expr
t3=(sp.Rational(1,2)-pA)/pB
m1=1-2*pC_expr; m2=1-2*pA; m3=1-2*pB   # masses on AB, BC, CA
eqs={
 "u1 low ":m2+m1/t1, "u1 high":m2+m3/(1-t1),
 "u2 low ":m1+m3/t2, "u2 high":m1+m2/(1-t2),
 "u3 low ":m3+m2/t3, "u3 high":m3+m1/(1-t3),
}
print("SYMBOLIC (should all be 1):")
for k,v in eqs.items(): print(f"  {k}: {sp.simplify(v)}")

# Monte Carlo sanity for 3 random p in the open medial triangle (max p_j<1/2)
import numpy as np
rng=np.random.default_rng(7)
def mc(p,n=400000,bins=25):
    pa,pb,pc=p
    T1=(0.5-pc)/pa; T2=(0.5-pb)/pc; T3=(0.5-pa)/pb
    V=np.array([[T1,0,1],[0,1,T2],[1,T3,0]])
    w=[1-2*pc,1-2*pa,1-2*pb]; W=sum(w)
    # sample edges AB,BC,CA with probs w/W ; vertices A=(1,0,0) etc. barycentric
    E=[((1,0,0),(0,1,0)),((0,1,0),(0,0,1)),((0,0,1),(1,0,0))]
    U=[]
    for _ in range(n):
        e=rng.choice(3,p=np.array(w)/W); t=rng.random()
        x=np.array(E[e][0])*(1-t)+np.array(E[e][1])*t
        U.append(V@x)
    U=np.array(U); dev=0
    for i in range(3):
        h,_=np.histogram(U[:,i],bins=bins,range=(0,1),density=True); dev=max(dev,abs(h-1).max())
    return dev,(T1,T2,T3)
print("\nMONTE CARLO (max|marginal-1|, should be ~0.02 noise):")
for p in [(9/20,3/10,1/4),(0.35,0.42,0.23),(0.48,0.28,0.24)]:
    dev,T=mc(p); print(f"  p={p}: dev={dev:.3f}  tau={tuple(round(t,3) for t in T)}")
