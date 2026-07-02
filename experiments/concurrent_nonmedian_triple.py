# R5-3 step 1: exact concurrent non-median triple + verification.
# Cyclic pattern: u1=(t1,0,1), u2=(0,1,t2), u3=(1,t3,0) (vertex values at A,B,C).
# Concurrency at p: u_i(p)=1/2.
from fractions import Fraction as F
pA,pB,pC = F(9,20), F(3,10), F(1,4)
assert pA+pB+pC==1
t1=(F(1,2)-pC)/pA; t2=(F(1,2)-pB)/pC; t3=(F(1,2)-pA)/pB
print("tau =",t1,t2,t3, " all in (0,1)?", all(0<t<1 for t in (t1,t2,t3)), " any =1/2?", any(t==F(1,2) for t in (t1,t2,t3)))
V=[[t1,F(0),F(1)],[F(0),F(1),t2],[F(1),t3,F(0)]]
# check u_i(p)=1/2
p=[pA,pB,pC]
for i in range(3):
    val=sum(V[i][j]*p[j] for j in range(3)); assert val==F(1,2), (i,val)
# cond = 1^T V^{-1} 1 via solving V x = 1 exactly (Gaussian elim over Q)
import copy
def solveQ(A,b):
    A=[row[:] for row in A]; b=b[:]; n=len(b)
    for c in range(n):
        piv=next(r for r in range(c,n) if A[r][c]!=0)
        A[c],A[piv]=A[piv],A[c]; b[c],b[piv]=b[piv],b[c]
        inv=F(1,1)/A[c][c]
        A[c]=[x*inv for x in A[c]]; b[c]*=inv
        for r in range(n):
            if r!=c and A[r][c]!=0:
                f=A[r][c]; A[r]=[A[r][k]-f*A[c][k] for k in range(3)]; b[r]-=f*b[c]
    return b
x=solveQ(V,[F(1),F(1),F(1)])
print("V^{-1}1 =",x," 1^T V^{-1} 1 =",sum(x)," (=2?)", sum(x)==2, " V^{-1}1>=0?", all(v>=0 for v in x))
