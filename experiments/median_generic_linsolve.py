from fractions import Fraction as F
# Solve by substitution the 6 eqs; verify unique solution.
# l1=1-2l3, l3=1-2l2, l2=1-2l1  => l1=1-2(1-2(1-2l1))
l1=F(1,3)
assert l1==1-2*(1-2*(1-2*l1)), "l chain"
l2=1-2*l1; l3=1-2*l2
h1=F(2,3)
assert h1==2-2*(2-2*(2-2*h1)), "h chain"
h2=2-2*h1; h3=2-2*h2
print("l1,l2,l3 =",l1,l2,l3)
print("h1,h2,h3 =",h1,h2,h3)
# check the two remaining eqs (5),(6) generic
assert h3==2-2*h1 and l3==1-2*l2
# also verify these are the third-central and r_i=1/3
print("r_i =",[h1-l1,h2-l2,h3-l3], " sum=",(h1-l1)+(h2-l2)+(h3-l3))
print("UNIQUE generic solution = third-central [1/3,2/3]^3:", (l1,h1)==(F(1,3),F(2,3)))
