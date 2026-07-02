import sympy as sp

def run_homogenized_algebra():
    print("Prop 1 (Advanced): Homogenized Algebraic System in R^3")
    
    x1, x2, x3 = sp.symbols('x1 x2 x3', real=True)
    
    # Let's model the 3 facets of the simplex as 3 linear forms
    L1 = x1
    L2 = x2
    L3 = x3
    
    # We add 1 plank as a linear form (since any affine form L(x)-m on the simplex x1+x2+x3=1 
    # can be rewritten as L(x) - m(x1+x2+x3), which is purely linear).
    # Let's use 3 planks.
    u1, u2, u3 = sp.symbols('u1 u2 u3', real=True)
    v1, v2, v3 = sp.symbols('v1 v2 v3', real=True)
    w1, w2, w3 = sp.symbols('w1 w2 w3', real=True)
    
    L4 = u1*x1 + u2*x2 + u3*x3
    L5 = v1*x1 + v2*x2 + v3*x3
    L6 = w1*x1 + w2*x2 + w3*x3
    
    # The potential is Phi = -sum q_j log(L_j)
    # We want to minimize Phi subject to x1+x2+x3=1.
    # The Lagrangian gradient gives: dPhi/dx_k = lambda
    
    q1, q2, q3, q4, q5, q6 = sp.symbols('q1 q2 q3 q4 q5 q6', real=True)
    
    grad_1 = -q1/L1 - q4*u1/L4 - q5*v1/L5 - q6*w1/L6
    grad_2 = -q2/L2 - q4*u2/L4 - q5*v2/L5 - q6*w2/L6
    grad_3 = -q3/L3 - q4*u3/L4 - q5*v3/L5 - q6*w3/L6
    
    # Multiply by L1*L2*L3*L4*L5*L6 to clear denominators
    Q = L1 * L2 * L3 * L4 * L5 * L6
    
    # By Euler's theorem on homogeneous functions, x1*grad_1 + x2*grad_2 + x3*grad_3 = -sum(q_j)
    # Since grad_k = lambda at the critical point, lambda * (x1+x2+x3) = -sum(q_j).
    # Since x1+x2+x3 = 1, lambda = -sum(q_j).
    lam = -(q1+q2+q3+q4+q5+q6)
    
    H1 = sp.cancel(Q * (grad_1 - lam))
    H2 = sp.cancel(Q * (grad_2 - lam))
    H3 = sp.cancel(Q * (grad_3 - lam))
    
    # We actually only need 2 independent equations since x1+x2+x3=1.
    # Let's substitute x3 = 1 - x1 - x2 into H1 and H2
    H1_sub = H1.subs(x3, 1 - x1 - x2)
    H2_sub = H2.subs(x3, 1 - x1 - x2)
    
    H1_num = sp.fraction(H1_sub)[0]
    H2_num = sp.fraction(H2_sub)[0]
    
    print("\nDegrees of the homogenized polynomials after substituting x3 = 1 - x1 - x2:")
    print(f"deg(H1) in (x1,x2): {sp.degree(sp.expand(H1_num), x1)} (x1), {sp.degree(sp.expand(H1_num), x2)} (x2)")
    
    # Let's check if the corners are still roots.
    # Corner 1: x1=1, x2=0 (which implies x3=0)
    H1_corner = H1_num.subs({x1: 1, x2: 0})
    print(f"\nValue of H1 at corner (1,0,0):")
    print(sp.simplify(H1_corner))
    
    print("\nResult: By homogenizing the planks into pure linear forms in R^3, the system is EXACTLY")
    print("the centered Martinez-Ortega-Moreno system (but with 6 forms in 3 dimensions instead of n in n).")
    print("We can apply the classical Euler-Jacobi theorem directly to this homogenized system if it forms a complete intersection.")

if __name__ == '__main__':
    run_homogenized_algebra()