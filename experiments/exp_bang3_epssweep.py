from exp_bang3_edges import gen_dir, min_tiling
from multiprocessing import Pool
import random
random.seed(5)
roles=[(0,1),(1,0),(0,2),(2,0),(1,2),(2,1)]
taus=[0.15,0.25,0.35,0.45,0.55,0.65,0.75,0.85]
def rdir():
    im,ix=random.choice(roles); return gen_dir(im,ix,random.choice(taus))

# build 5 three-distinct-edge triples + 1 common-edge contrast
triples=[]
tries=0
while len(triples)<5 and tries<5000:
    tries+=1
    d1,d2,d3=rdir(),rdir(),rdir()
    if len({d1[1],d2[1],d3[1]})!=3: continue
    if len({d1[0],d2[0],d3[0]})<3: continue
    triples.append(("3edge",d1[0],d2[0],d3[0]))
triples.append(("1edge",(0.0,1.0,0.3),(0.0,1.0,0.6),(1.0,0.0,0.5)))

jobs=[]
for tag,u1,u2,u3 in triples:
    for eps in (0.20,0.12,0.06,0.03):
        jobs.append((tag,u1,u2,u3,eps))
def work(j):
    tag,u1,u2,u3,eps=j
    v,cfg=min_tiling(u1,u2,u3,24,eps)
    return (tag,(u1,u2,u3),eps,v,cfg)
with Pool() as p:
    res=p.map(work,jobs)
from collections import defaultdict
byt=defaultdict(dict)
order=[]
for tag,us,eps,v,cfg in res:
    if us not in order: order.append(us)
    byt[us][eps]=(v,cfg)
for us in order:
    tag=[t for t,a,b,c in [(r[0],*r[1:2]) for r in []]] 
    d=byt[us]
    s=" ".join(f"eps={e}:{d[e][0]:.4f}" for e in (0.20,0.12,0.06,0.03))
    print(f"{us}\n   {s}")
    # show cfg at eps=0.06 to see if degenerate-ish
    v,cfg=d[0.06]
    print(f"   @eps.06 cfg(l1,r1,l2,r2,r3)={tuple(round(x,3) for x in cfg) if cfg else None}")
