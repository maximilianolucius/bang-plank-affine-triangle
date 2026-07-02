# R5-3 step 2: can a perimeter measure with VARIABLE edge densities rho1(AB),rho2(BC),rho3(CA)
# give uniform marginals for the non-median concurrent triple tau=(5/9,4/5,1/6)?
# Functional system (derived; u1=(t1,0,1), u2=(0,1,t2), u3=(1,t3,0), edges AB,BC,CA param t in[0,1]):
#  u1: s in[0,t1]:  rho2(s) + rho1(1-s/t1)/t1            = 1
#      s in[t1,1]:  rho2(s) + rho3((1-s)/(1-t1))/(1-t1)  = 1
#  u2: s in[0,t2]:  rho1(s) + rho3(1-s/t2)/t2            = 1
#      s in[t2,1]:  rho1(s) + rho2((1-s)/(1-t2))/(1-t2)  = 1
#  u3: s in[0,t3]:  rho3(s) + rho2(1-s/t3)/t3            = 1
#      s in[t3,1]:  rho3(s) + rho1((1-s)/(1-t3))/(1-t3)  = 1
# Discretize rho_e as piecewise-linear on M+1 grid values; collocate at fine points; solve LSQ.
import numpy as np
t1,t2,t3 = 5/9, 4/5, 1/6
M=400           # grid intervals per edge
NC=2000         # collocation points per equation family
grid=np.linspace(0,1,M+1)
def interp_row(x):  # row vector: linear interpolation weights of rho(x) on grid
    w=np.zeros(M+1)
    if x<=0: w[0]=1; return w
    if x>=1: w[M]=1; return w
    k=int(x*M); f=x*M-k
    w[k]=1-f; w[min(k+1,M)]=f
    return w
rows=[];rhs=[]
Z=np.zeros(M+1)
def eq(c1,x1,c2,x2):  # c1*rho_{e1}(x1) + c2*rho_{e2}(x2) = 1 ; e indices 0,1,2 = AB,BC,CA
    r=np.zeros(3*(M+1))
    e1,xx1=x1; e2,xx2=x2
    r[e1*(M+1):(e1+1)*(M+1)]+=c1*interp_row(xx1)
    r[e2*(M+1):(e2+1)*(M+1)]+=c2*interp_row(xx2)
    rows.append(r); rhs.append(1.0)
for s in np.linspace(1e-6,1-1e-6,NC):
    # u1
    if s<t1: eq(1.0,(1,s), 1/t1,(0,1-s/t1))
    else:    eq(1.0,(1,s), 1/(1-t1),(2,(1-s)/(1-t1)))
    # u2
    if s<t2: eq(1.0,(0,s), 1/t2,(2,1-s/t2))
    else:    eq(1.0,(0,s), 1/(1-t2),(1,(1-s)/(1-t2)))
    # u3
    if s<t3: eq(1.0,(2,s), 1/t3,(1,1-s/t3))
    else:    eq(1.0,(2,s), 1/(1-t3),(0,(1-s)/(1-t3)))
A=np.array(rows); b=np.array(rhs)
sol,res,rk,sv=np.linalg.lstsq(A,b,rcond=None)
resid=np.abs(A@sol-b).max()
r1,r2,r3=sol[:M+1],sol[M+1:2*(M+1)],sol[2*(M+1):]
print(f"max residual = {resid:.2e}   min densities: rho1={r1.min():.4f} rho2={r2.min():.4f} rho3={r3.min():.4f}")
print(f"masses: M1={np.trapezoid(r1,grid):.4f} M2={np.trapezoid(r2,grid):.4f} M3={np.trapezoid(r3,grid):.4f} sum={np.trapezoid(r1,grid)+np.trapezoid(r2,grid)+np.trapezoid(r3,grid):.4f}")
neg=min(r1.min(),r2.min(),r3.min())
print("VERDICT: system solvable with NONNEGATIVE densities?" , (resid<1e-6) and (neg>-1e-6))
# where negative?
for name,r in [("rho1(AB)",r1),("rho2(BC)",r2),("rho3(CA)",r3)]:
    idx=np.where(r<-1e-3)[0]
    if len(idx): print(f"  {name}<0 on s in [{grid[idx[0]]:.3f},{grid[idx[-1]]:.3f}], min={r.min():.4f}")
