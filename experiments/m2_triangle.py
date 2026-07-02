#!/usr/bin/env python3
"""
M2 triangle testbed (pure Python). d=2 simplex (triangle).
Barrier potential  Phi(x) = -sum_k c_k log(b_k - <a_k,x>) - sum_i alpha_i log|<u_i,x>-m_i|
on each chamber (cell of the n plank-lines inside the triangle).

Checks:
 - existence of a critical point (analytic center) per non-empty chamber
 - those points are INSIDE the triangle and AVOID all planks (by construction)
 - count of critical points vs number of chambers
 - reality (critical points are real by construction; we confirm the cleared system has
   the same number of real solutions = no spurious complex/infinity, a P2/P1 signal)
 - width w_K(u_i) and the relative-width sum, to relate to non-covering
"""
import math, random
def solve2(A,b):  # 2x2 solve
    det=A[0][0]*A[1][1]-A[0][1]*A[1][0]
    return [(b[0]*A[1][1]-b[1]*A[0][1])/det, (A[0][0]*b[1]-A[1][0]*b[0])/det]

def triangle(equilateral=True):
    if equilateral:
        V=[(0.0,0.0),(1.0,0.0),(0.5,math.sqrt(3)/2)]
    else:
        V=[(0.0,0.0),(1.3,0.1),(0.4,1.1)]
    # facets: for each edge (Vi,Vj), outward normal a, offset b=<a,Vi>, third vertex inside
    fac=[]
    for (i,j,l) in [(0,1,2),(1,2,0),(2,0,1)]:
        e=(V[j][0]-V[i][0], V[j][1]-V[i][1])
        a=(e[1],-e[0])  # normal
        b=a[0]*V[i][0]+a[1]*V[i][1]
        if a[0]*V[l][0]+a[1]*V[l][1] > b:  # make outward (third vertex strictly inside: <b)
            a=(-a[0],-a[1]); b=-b
        nrm=math.hypot(*a); a=(a[0]/nrm,a[1]/nrm); b=b/nrm
        fac.append((a,b))
    return V,fac

def wK(V,u):  # width of triangle in direction u
    vals=[u[0]*p[0]+u[1]*p[1] for p in V]
    return max(vals)-min(vals)

def run(V,fac,planks,c=1.0,alpha=1.0):
    # planks: list of (u (unit), m, w)
    nP=len(planks)
    def facval(k,x): return fac[k][1]-(fac[k][0][0]*x[0]+fac[k][0][1]*x[1])  # b-<a,x> >0 inside
    def Lval(i,x): return (planks[i][0][0]*x[0]+planks[i][0][1]*x[1])-planks[i][1]  # <u,x>-m
    def phi(x):
        val=0.0
        for k in range(3):
            f=facval(k,x)
            if f<=0: return float('inf')
            val-=c*math.log(f)
        for i in range(nP):
            L=Lval(i,x)
            if L==0: return float('inf')
            val-=alpha*math.log(abs(L))
        return val
    def grad(x):
        g=[0.0,0.0]
        for k in range(3):
            f=facval(k,x)
            for d in range(2): g[d]+=c*fac[k][0][d]/f   # d/dx[-c log(b-<a,x>)] = c a/(b-<a,x>)
        for i in range(nP):
            L=Lval(i,x)
            for d in range(2): g[d]-=alpha*planks[i][0][d]/L
        return g
    def hess(x):
        H=[[0.0,0.0],[0.0,0.0]]
        for k in range(3):
            f=facval(k,x); cc=c/(f*f)
            for a in range(2):
                for b in range(2): H[a][b]+=cc*fac[k][0][a]*fac[k][0][b]
        for i in range(nP):
            L=Lval(i,x); cc=alpha/(L*L)
            for a in range(2):
                for b in range(2): H[a][b]+=cc*planks[i][0][a]*planks[i][0][b]
        return H
    def newton(x0):
        x=list(x0)
        sgnL=[1 if Lval(i,x0)>0 else -1 for i in range(nP)]
        for _ in range(300):
            g=grad(x)
            if max(abs(v) for v in g)<1e-12: break
            st=solve2(hess(x),g)
            f0=phi(x); t=1.0
            ok=False
            for _ in range(80):
                xn=[x[d]-t*st[d] for d in range(2)]
                inside = all(facval(k,xn)>0 for k in range(3)) and all(Lval(i,xn)*sgnL[i]>0 for i in range(nP))
                if inside and phi(xn)<f0: ok=True; break
                t*=0.5
            if not ok: break
            x=xn
        return x
    # enumerate chambers by sampling many interior points; find critical pt in each visited chamber
    found={}
    R=random.Random(7)
    # barycentric sampling inside triangle
    for _ in range(4000):
        r1,r2=R.random(),R.random()
        if r1+r2>1: r1,r2=1-r1,1-r2
        x=[V[0][0]+r1*(V[1][0]-V[0][0])+r2*(V[2][0]-V[0][0]),
           V[0][1]+r1*(V[1][1]-V[0][1])+r2*(V[2][1]-V[0][1])]
        if any(Lval(i,x)==0 for i in range(nP)): continue
        key=tuple(1 if Lval(i,x)>0 else -1 for i in range(nP))
        if key in found: continue
        sol=newton(x)
        if max(abs(v) for v in grad(sol))<1e-8:
            found[key]=sol
    return found

if __name__=="__main__":
    V,fac=triangle(equilateral=True)
    print("Equilateral triangle, widths in axis dirs:", round(wK(V,(1,0)),3), round(wK(V,(0,1)),3))
    # 3 planks parallel to the 3 sides (normals = facet normals), centered, sub-covering
    for scenario,wfrac in [("sub-cover (sum rw<1)",0.28),("near-tight",0.34)]:
        planks=[]
        srw=0.0
        for k in range(3):
            u=fac[k][0]
            wid=wK(V,u)
            # center the plank at the middle of the triangle's extent in dir u
            vals=[u[0]*p[0]+u[1]*p[1] for p in V]
            m=(max(vals)+min(vals))/2
            w=wfrac*wid
            planks.append((u,m,w)); srw+=w/wid
        found=run(V,fac,planks)
        # check avoidance: does any critical point avoid ALL planks (|<u,x>-m|>=w)?
        avoid=[]
        for key,x in found.items():
            ok=all(abs((planks[i][0][0]*x[0]+planks[i][0][1]*x[1])-planks[i][1])>=planks[i][2]-1e-9 for i in range(len(planks)))
            if ok: avoid.append(x)
        print(f"\n[{scenario}] sum rel-width={srw:.3f}  #chambers-with-critpt={len(found)}  #critpts-avoiding-all-planks={len(avoid)}")
        if avoid:
            x=avoid[0]
            print(f"   example uncovered point x={[round(v,3) for v in x]}, inside={all(fac[k][1]-(fac[k][0][0]*x[0]+fac[k][0][1]*x[1])>0 for k in range(3))}")
