import numpy as np
# Equilateral triangle vertices
V=np.array([[0,0],[1,0],[0.5,np.sqrt(3)/2]])
def support_width(u):  # width = max<x,u>-min<x,u> over vertices
    p=V@u; return p.max()-p.min()
def longest_chord(u):
    # longest segment inside triangle parallel to u. For a convex polygon,
    # longest chord parallel to u = max over sweeping lines of intersection length.
    # sample offsets along normal n of u; chord length at offset = extent along u of the slice.
    un=u/np.linalg.norm(u); n=np.array([-un[1],un[0]])
    offs=(V@n)
    best=0.0
    for t in np.linspace(offs.min()+1e-9,offs.max()-1e-9,20001):
        # intersect line {x: <x,n>=t} with triangle edges, collect <x,un>
        pts=[]
        for a in range(3):
            b=(a+1)%3
            A,B=V[a],V[b]
            da=A@n - t; db=B@n - t
            if da==0: pts.append(A@un)
            if db==0: pts.append(B@un)
            if da*db<0:
                s=da/(da-db); P=A+s*(B-A); pts.append(P@un)
        if len(pts)>=2:
            best=max(best,max(pts)-min(pts))
    return best
print("dir  tau   w      ell    rho=ell/w   ell<=w?")
for th in np.linspace(0.01,np.pi-0.01,9):
    u=np.array([np.cos(th),np.sin(th)])
    w=support_width(u); l=longest_chord(u)
    print(f"{th:4.2f}      {w:.4f} {l:.4f}  {l/w:.4f}     {l<=w+1e-6}")
print("min rho over scan ~", min(longest_chord(np.array([np.cos(th),np.sin(th)]))/support_width(np.array([np.cos(th),np.sin(th)])) for th in np.linspace(0.001,np.pi,400)))
print("4*sqrt3-6 =", 4*np.sqrt(3)-6)
# Lemma 2.3 tightness on a segment C=[0,ell] (1-D): (C-u)cap(C+u) has length ell-a for shift a/2 each side
ell=1.0
for a in [0.2,0.5,0.8]:
    # C=[0,ell]; C-u=[-a/2,ell-a/2]? u has 'norm a/2' along the line; shift by u => interval shifts by a/2
    lo=max(0+a/2, 0-a/2); hi=min(ell+a/2, ell-a/2)  # (C-u)&(C+u) = [a/2, ell-a/2]
    length=hi-lo
    print(f"a={a}: (C-u)cap(C+u) length={length:.3f}, ell-a={ell-a:.3f}, ratio={(length)/ell:.3f}=(ell-a)/ell={((ell-a)/ell):.3f}")
