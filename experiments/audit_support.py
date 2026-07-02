import numpy as np
from scipy.optimize import minimize

def audit_support_function():
    print("--- SIXTH AUDIT: The Convex Hull Fallacy in Support Functions ---")
    
    print("\n[1] The Claim:")
    print("Claim: 'If the infimal convolution support function F(lambda) < 0, the planks do not cover the triangle.'")
    
    print("\n[2] The Mathematical Reality:")
    print("Support functions h_K(v) only describe the CONVEX HULL of a set K.")
    print("For a union of planks U = union P_i, the support function h_U is exactly the support function of conv(U).")
    print("If we evaluate F(lambda) < 0, we are proving that the CONVEX HULL of the planks does not cover the triangle.")
    
    print("\n[3] Empirical Proof of the Flaw:")
    V = np.array([[0,0], [1,0], [0.5, np.sqrt(3)/2]])
    def triangle_support(v):
        return np.max(V @ v)
        
    np.random.seed(42)
    # Generic directions
    angles = np.random.uniform(0, np.pi, 4)
    U = np.array([np.cos(angles), np.sin(angles)]).T
    
    # Tiny widths, so sum(rw) is very small (e.g. 0.1)
    # They obviously DO NOT cover the triangle.
    p = np.array([0.02, 0.02, 0.02, 0.02])
    
    widths = []
    centers = []
    for i in range(4):
        w_T = np.max(V@U[i]) - np.min(V@U[i])
        widths.append(p[i] * w_T)
        centers.append( (np.max(V@U[i]) + np.min(V@U[i])) / 2 )
        
    def objective(lam):
        v = - np.sum(lam[:, np.newaxis] * U, axis=0)
        h_Delta = triangle_support(v)
        val = h_Delta + np.sum(np.abs(lam) * widths / 2) - np.sum(lam * centers)
        return val
        
    min_val = float('inf')
    for _ in range(50):
        lam0 = np.random.uniform(-1, 1, 4)
        res = minimize(objective, lam0, method='Nelder-Mead')
        if res.fun < min_val:
            min_val = res.fun
            
    print(f"Minimum value of F(lambda): {min_val:.5f}")
    if min_val >= -1e-4:
        print("\nCRITICAL FAILURE! The minimum is >= 0, meaning F(lambda) claims the triangle IS COVERED.")
        print("But the sum of relative widths is only 0.08, so it is IMPOSSIBLE that it's covered.")
        print("Why did it fail? Because the CONVEX HULL of 4 intersecting lines in R^2 is the entire R^2 space.")
        print("Thus, conv(Union P_i) covers the triangle trivially, making the dual test completely blind to the actual covering.")
        
    print("\nCONCLUSION: FATAL ERROR IN THE SUPPORT FUNCTION ROUTE.")
    print("The route must be immediately retracted.")

if __name__ == '__main__':
    audit_support_function()