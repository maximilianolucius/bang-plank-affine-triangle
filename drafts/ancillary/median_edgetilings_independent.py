# INDEPENDENT cross-check of notes/45 Step 2: the perimeter (edge) tiling by 3 median planks
# has EXACTLY 3 solutions. Method DIFFERENT from median_rigidity_enumeration.py (sympy orders):
# here we brute-force rational endpoints and check edge-partition DIRECTLY via trace intervals.
from fractions import Fraction as F

# medians (notes/36): m1=1/2-y/2+z/2, m2=y+z/2, m3=1-y/2-z
# Edge parametrizations & per-edge trace of P_i={m_i in [l_i,h_i]} as sub-interval of [0,1]:
# AB (t=m2): P2=[l2,h2]; P1: m1=1/2-t/2 in I1 -> t in [1-2*min(h1,1/2),1-2*l1] cap[0,1]; P3: m3=1-t/2 in I3 -> t in [2-2*h3,2-2*max(l3,1/2)] cap[0,1]
# BC (t=m1): P1=[l1,h1]; P2: m2=1-t/2 -> t in[2-2*h2,2-2*max(l2,1/2)]; P3: m3=1/2-t/2 -> t in[1-2*min(h3,1/2),1-2*l3]
# CA (s):    P3=[1-h3,1-l3]; P1: s=2*m1-1 -> [2*max(l1,1/2)-1,2*h1-1]; P2: s=2*m2 -> [2*l2,2*min(h2,1/2)]
def clip(a,b):
    a=max(a,F(0)); b=min(b,F(1)); return (a,b) if b>a else None
def traces(I):
    (l1,h1),(l2,h2),(l3,h3)=I
    AB=[clip(l2,h2), clip(1-2*min(h1,F(1,2)),1-2*l1), clip(2-2*h3,2-2*max(l3,F(1,2)))]
    BC=[clip(l1,h1), clip(2-2*h2,2-2*max(l2,F(1,2))), clip(1-2*min(h3,F(1,2)),1-2*l3)]
    CA=[clip(1-h3,1-l3), clip(2*max(l1,F(1,2))-1,2*h1-1), clip(2*l2,2*min(h2,F(1,2)))]
    return [AB,BC,CA]
def partitions_unit(intervals):
    segs=sorted([s for s in intervals if s is not None])
    if not segs: return False
    if segs[0][0]!=0: return False
    cur=F(0)
    for a,b in segs:
        if a!=cur: return False   # gap or overlap
        cur=b
    return cur==1
def is_edge_tiling(I):
    return all(partitions_unit(e) for e in traces(I))

sols=set()
for D in [6,12,18]:
    found=set()
    vals=[F(a,D) for a in range(D+1)]
    trip=[(l,h) for l in vals for h in vals if h>l]
    for t1 in trip:
        for t2 in trip:
            r12=(t1[1]-t1[0])+(t2[1]-t2[0])
            if r12>=1: continue
            r3=1-r12
            for t3 in trip:
                if t3[1]-t3[0]!=r3: continue
                I=(t1,t2,t3)
                if is_edge_tiling(I): found.add(I)
    print(f"D={D}: edge-tilings found = {len(found)}: {sorted(found)}")
    sols|=found
print("UNION over grids:", sorted(sols))
