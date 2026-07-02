import sympy as sp

def audit_algebraic_infinity():
    print("--- AUDIT: Algebraic Roots at Infinity ---")
    x1, x2 = sp.symbols('x1 x2', real=True)
    
    # We use random integer coefficients to avoid accidental cancellations
    # and strictly test the generic structural degrees.
    import random
    random.seed(999)
    
    # L1, L2, L3 are the facets. L1=x1, L2=x2, L3=1-x1-x2
    L1 = x1
    L2 = x2
    L3 = 1 - x1 - x2
    
    # L4, L5, L6 are 3 homogenized planks. 
    # L(x) = u*x1 + v*x2 + w*(1-x1-x2)
    def random_L():
        return random.randint(1,10)*x1 + random.randint(1,10)*x2 + random.randint(1,10)*(1-x1-x2)
        
    L4 = random_L()
    L5 = random_L()
    L6 = random_L()
    
    Ls = [L1, L2, L3, L4, L5, L6]
    qs = [random.randint(1,5) for _ in range(6)]
    
    # grad_1 is the derivative with respect to x1.
    # Phi = -sum q_j log(L_j).
    # To be extremely precise, since x3 = 1-x1-x2, the total derivative is:
    # d/dx1 = partial/dx1 - partial/dx3
    # Wait! In the previous script `prop1_homogenized.py`, we took grad_1, grad_2, grad_3 INDEPENDENTLY
    # before substituting x3 = 1-x1-x2. But if the space is 2D, we only have 2 independent derivatives!
    print("CHECKING INDEPENDENT DERIVATIVES:")
    grad_x1 = 0
    grad_x2 = 0
    
    for q, L in zip(qs, Ls):
        # L is already in terms of x1, x2
        # derivative of log(L) wrt x1
        dL_dx1 = sp.diff(L, x1)
        dL_dx2 = sp.diff(L, x2)
        grad_x1 += -q * dL_dx1 / L
        grad_x2 += -q * dL_dx2 / L
        
    Q = sp.expand(L1 * L2 * L3 * L4 * L5 * L6)
    
    H1 = sp.cancel(Q * grad_x1)
    H2 = sp.cancel(Q * grad_x2)
    
    H1_num = sp.fraction(H1)[0]
    H2_num = sp.fraction(H2)[0]
    
    H1_poly = sp.poly(H1_num, x1, x2)
    H2_poly = sp.poly(H2_num, x1, x2)
    
    print(f"Actual Degree of H1: {H1_poly.total_degree()}")
    print(f"Actual Degree of H2: {H2_poly.total_degree()}")
    
    # The degree is 5 (since Q has degree 6, and grad has degree -1).
    # To check for roots at projective infinity, we take the homogeneous part of degree 5
    H1_top = 0
    for monom, coeff in H1_poly.terms():
        if sum(monom) == 5:
            H1_top += coeff * x1**monom[0] * x2**monom[1]
                             
    H2_top = 0
    for monom, coeff in H2_poly.terms():
        if sum(monom) == 5:
            H2_top += coeff * x1**monom[0] * x2**monom[1]
                             
    print("\nHighest degree part of H1 (degree 5):")
    print(H1_top)
    
    # If H1_top and H2_top have a common root in P^1 (i.e. x1/x2 = constant), 
    # then the system HAS ROOTS AT INFINITY.
    # We can check this by computing the resultant of H1_top and H2_top.
    print("\nComputing Resultant(H1_top, H2_top, x1)...")
    res = sp.resultant(H1_top, H2_top, x1)
    print(f"Resultant: {res}")
    
    if res == 0:
        print("CRITICAL FLAW: The resultant is 0. This means H1_top and H2_top share a common factor!")
        print("Therefore, the homogenized system HAS ROOTS AT PROJECTIVE INFINITY.")
        print("Classical Euler-Jacobi CANNOT be applied without boundary corrections.")
    else:
        print("SAFE: Resultant is non-zero. No roots at infinity.")

if __name__ == '__main__':
    audit_algebraic_infinity()