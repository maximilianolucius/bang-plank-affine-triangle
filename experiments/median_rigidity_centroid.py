from fractions import Fraction as F
def mvals(y,z): return (F(1,2)-y/2+z/2, y+z/2, 1-y/2-z)
G=mvals(F(1,3),F(1,3))
print("m(centroid) =", G)
cases=[("MMM",(F(1,3),F(2,3))),("LLL",(F(0),F(1,3))),("RRR",(F(2,3),F(1)))]
def covers(iv,N):
    for i in range(N+1):
        for j in range(N-i+1):
            m=mvals(F(i,N),F(j,N))
            if not any(iv[0]<=m[k]<=iv[1] for k in range(3)): return False
    return True
for name,iv in cases:
    cov_c = any(iv[0]<=G[k]<=iv[1] for k in range(3))
    print(f"{name}: I={iv}  centroid covered? {cov_c}   covers Delta(N=24)? {covers(iv,24)}")
