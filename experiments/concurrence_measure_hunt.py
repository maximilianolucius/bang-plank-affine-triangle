# R4-4: hunt for an EXPLICIT witness measure for a GENERIC concurrent triple.
# Concurrent-at-centroid <=> vertex-value rows sum to 3/2. Test candidate measures:
# whether pushforward of each u_i is uniform on [0,1].
import numpy as np
# generic concurrent triple (rows sum 3/2), NOT the median pattern:
V=np.array([[0.0,0.5,1.0],[0.5,1.0,0.0],[1.0,0.0,0.5]])  # rowsums 1.5
assert np.allclose(V.sum(1),1.5)
# triangle vertices A,B,C in R^2 (use standard); barycentric x=(x1,x2,x3)
def bary(y,z): return np.array([1-y-z, y, z])
def uvals(y,z): return V@bary(y,z)  # (u1,u2,u3)
rng=np.random.default_rng(0)
def marg_dev(sampler, nsamp=300000, bins=20):
    U=[]
    for _ in range(nsamp):
        y,z=sampler(); U.append(uvals(y,z))
    U=np.array(U); dev=0
    for i in range(3):
        h,_=np.histogram(U[:,i],bins=bins,range=(0,1),density=True); dev=max(dev,abs(h-1).max())
    return dev
def s_perim():
    e=rng.integers(3); t=rng.random()
    if e==0: return (t,0.0)          # AB
    if e==1: return (1-t,t)          # BC
    return (0.0,t)                   # CA
def s_cevian_centroid():  # segments from centroid to the 3 vertices
    g=np.array([1/3,1/3]); e=rng.integers(3); t=rng.random()
    verts=[np.array([0,0]),np.array([1,0]),np.array([0,1])]
    p=g+t*(verts[e]-g); return (p[0],p[1])
def s_levelhalf():  # union of the 3 chords {u_i=1/2} (full chords in triangle)
    # sample point on line u_i=1/2 within triangle: parametrize, reject outside
    i=rng.integers(3)
    for _ in range(50):
        y,z=rng.random(),rng.random()
        if y+z<=1:
            # project onto u_i=1/2? just accept points near; instead sample the chord directly:
            pass
    # fallback: sample interior, keep those with u_i≈1/2 (thin) -- skip, use area
    y,z=rng.random(),rng.random()
    while y+z>1: y,z=rng.random(),rng.random()
    return (y,z)
def s_area():
    y,z=rng.random(),rng.random()
    while y+z>1: y,z=rng.random(),rng.random()
    return (y,z)
for name,s in [("perimeter",s_perim),("cevians-from-centroid",s_cevian_centroid),("area",s_area)]:
    print(f"{name}: max|marginal-1| = {marg_dev(s):.3f}")

print("\n=== TRULY generic concurrent triple (rowsum 3/2, NOT perms of {0,1/2,1}) ===")
Vg=np.array([[0.2,0.5,0.8],[0.9,0.0,0.6],[0.4,1.0,0.1]])
print("rowsums:",Vg.sum(1))  # should be 1.5
def uvals_g(y,z): return Vg@bary(y,z)
def marg_dev_g(sampler,nsamp=300000,bins=20):
    U=np.array([uvals_g(*sampler()) for _ in range(nsamp)]); dev=0
    for i in range(3):
        h,_=np.histogram(U[:,i],bins=bins,range=(U[:,i].min(),U[:,i].max()),density=True); dev=max(dev,abs(h-1).max())
    return dev
for name,s in [("perimeter",s_perim),("area",s_area),("cevians",s_cevian_centroid)]:
    print(f"generic {name}: max|marginal-1| = {marg_dev_g(s):.3f}")
# also: does each u_i even range over [0,1]? (need min=0,max=1 for uniform on [0,1])
for i in range(3): print(f"u{i} vertex-values {Vg[i]}, min={Vg[i].min()}, max={Vg[i].max()}")
