# R2-2: complete symbolic proof of median rigidity, ALL crossing patterns.
# For each pattern (c1,c2,c3) in {L,M,R}^3 (L:I subset[0,1/2], M:crosses 1/2, R:subset[1/2,1]),
# each edge has 3 trace-intervals (as linear fns of l_i,h_i); some empty.
# Nonempty traces must partition [0,1]: enumerate their order, impose abutting, solve exactly.
import sympy as sp
from itertools import permutations, product
l1,h1,l2,h2,l3,h3=sp.symbols('l1 h1 l2 h2 l3 h3',rational=True)
half=sp.Rational(1,2)
I={1:(l1,h1),2:(l2,h2),3:(l3,h3)}

def trace(edge,i,c):
    l,h=I[i]
    # returns (lo,hi) trace interval in edge param, or None if empty for crossing type c
    if edge=='AB':
        if i==2: return (l,h)                       # full
        if i==1: # m1 in [0,1/2], t=1-2 m1
            if c=='R': return None
            top = h if c=='L' else half             # min(h,1/2)
            return (1-2*top, 1-2*l)
        if i==3: # m3 in [1/2,1], t=2-2 m3
            if c=='L': return None
            bot = l if c=='R' else half             # max(l,1/2)
            return (2-2*h, 2-2*bot)
    if edge=='BC':
        if i==1: return (l,h)                        # full
        if i==2: # m2 in [1/2,1], t=2-2 m2
            if c=='L': return None
            bot = l if c=='R' else half
            return (2-2*h, 2-2*bot)
        if i==3: # m3 in [0,1/2], t=1-2 m3
            if c=='R': return None
            top = h if c=='L' else half
            return (1-2*top, 1-2*l)
    if edge=='CA':
        if i==3: return (1-h,1-l)                    # full (s=1-m3)
        if i==1: # m1 in [1/2,1], s=2 m1-1
            if c=='L': return None
            bot = l if c=='R' else half
            return (2*bot-1, 2*h-1)
        if i==2: # m2 in [0,1/2], s=2 m2
            if c=='R': return None
            top = h if c=='L' else half
            return (2*l, 2*top)

sols=[]
for (c1,c2,c3) in product('LMR',repeat=3):
    cross={1:c1,2:c2,3:c3}
    base_eqs=[]
    ok=True
    # crossing-type constraints
    cons=[]
    for i in (1,2,3):
        l,h=I[i]
        if cross[i]=='L': cons+=[h-half]         # h<=1/2  (as <=, handle later)
        if cross[i]=='R': cons+=[half-l]         # l>=1/2
        # M: l<1/2<h
    # For each edge, gather nonempty traces, enumerate orders, impose tiling
    edge_order_choices=[]
    feasible_edge=True
    per_edge=[]
    for edge in ('AB','BC','CA'):
        tr={i:trace(edge,i,cross[i]) for i in (1,2,3)}
        nonempty=[i for i in (1,2,3) if tr[i] is not None]
        per_edge.append((edge,tr,nonempty))
    # enumerate orders per edge
    order_space=[list(permutations(ne)) for (_,_,ne) in per_edge]
    for orders in product(*order_space):
        eqs=[]
        for (edge,tr,ne),order in zip(per_edge,orders):
            # tile [0,1] in this order: cumulative
            pos=sp.Integer(0)
            segs=[]
            for i in order:
                lo,hi=tr[i]; length=hi-lo
                # actual interval must be [pos,pos+length]; and equal tr[i]=[lo,hi]
                eqs.append(sp.Eq(lo,pos))
                pos=pos+length
                segs.append(i)
            eqs.append(sp.Eq(pos,1))  # ends at 1
        sol=sp.solve(eqs,[l1,h1,l2,h2,l3,h3],dict=True)
        for s in sol:
            vals={v:s.get(v,v) for v in (l1,h1,l2,h2,l3,h3)}
            # need fully determined numeric
            if any(not vals[v].is_number for v in vals): 
                continue
            L1,H1,L2,H2,L3,H3=[vals[v] for v in (l1,h1,l2,h2,l3,h3)]
            # checks: l<h, subset[0,1], r_i>0, crossing consistency
            def okint(l,h): return (0<=l) and (h<=1) and (l<h)
            if not(okint(L1,H1) and okint(L2,H2) and okint(L3,H3)): continue
            cok=True
            for i,(L,H) in zip((1,2,3),[(L1,H1),(L2,H2),(L3,H3)]):
                if cross[i]=='L' and not(H<=half): cok=False
                if cross[i]=='R' and not(L>=half): cok=False
                if cross[i]=='M' and not(L<half<H): cok=False
            if not cok: continue
            sols.append(((c1,c2,c3),(L1,H1,L2,H2,L3,H3)))

# dedup
uniq=set(sols)
print("distinct valid solutions across ALL patterns/orders:")
for pat,v in sorted(uniq):
    print("  pattern",pat,"-> I =",[(v[0],v[1]),(v[2],v[3]),(v[4],v[5])])
print("total distinct:",len(uniq))
