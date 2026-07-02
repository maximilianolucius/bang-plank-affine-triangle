from fractions import Fraction as F
def mvals(y,z):
    return (F(1,2)-y/2+z/2, y+z/2, 1-y/2-z)
def covers(I, N):
    for i in range(0,N+1):
        for j in range(0,N-i+1):
            y=F(i,N); z=F(j,N); m=mvals(y,z)
            if not any(I[k][0]<=m[k]<=I[k][1] for k in range(3)):
                return False
    return True
def search(D, Ncover):
    vals=[F(a,D) for a in range(0,D+1)]
    triples=[(l,h) for l in vals for h in vals if h>l]
    sols=[]; seen=set()
    for t1 in triples:
        for t2 in triples:
            r12=(t1[1]-t1[0])+(t2[1]-t2[0])
            if r12>=1: continue
            r3=1-r12
            for t3 in triples:
                if (t3[1]-t3[0])!=r3: continue
                I=(t1,t2,t3)
                if I in seen: continue
                seen.add(I)
                if covers(I,Ncover): sols.append(I)
    return sols
tc=((F(1,3),F(2,3)),)*3
print("third-central covers (N=24)?", covers(tc,24))
for name,(y,z) in [("A",(F(0),F(0))),("B",(F(1),F(0))),("C",(F(0),F(1)))]:
    print(name, mvals(y,z))
for D in [6,9,12]:
    s=search(D, Ncover=4*D)
    print(f"D={D}: {len(s)} tilings Sum r=1;", s[:8])
