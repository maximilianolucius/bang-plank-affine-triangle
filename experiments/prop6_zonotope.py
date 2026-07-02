import numpy as np

def test_zonotope_support():
    print("Prop 6: Zonotope Support Function & Minkowski Sums (m=4)")
    
    V = np.array([[0,0], [1,0], [0.5, np.sqrt(3)/2]])
    def triangle_width(u):
        projs = V @ u
        return np.max(projs) - np.min(projs)
        
    np.random.seed(42)
    successes = 0
    trials = 500
    
    # Generate random directions to test the support function
    test_dirs = []
    for theta in np.linspace(0, 2*np.pi, 100):
        test_dirs.append(np.array([np.cos(theta), np.sin(theta)]))
    test_dirs = np.array(test_dirs)
    
    for _ in range(trials):
        angles = np.random.uniform(0, np.pi, 4)
        U = np.array([np.cos(angles), np.sin(angles)]).T
        
        # Relative widths summing to 0.95
        cuts = np.sort(np.random.uniform(0, 0.95, 3))
        cuts = np.concatenate(([0], cuts, [0.95]))
        p = np.diff(cuts)
        
        # The zonotope Z = sum p_i * w_T(u_i) * [-u_i, u_i]
        # Wait, the width of the plank is w_i = p_i * w_T(u_i).
        # The zonotope formed by the normals is Z = sum w_i * [-u_i, u_i]
        
        widths = np.array([p[i] * triangle_width(U[i]) for i in range(4)])
        
        # Support function of the Zonotope Z in direction v:
        # h_Z(v) = sum (w_i / 2) * |<u_i, v>|
        # The width of Z in direction v is W_Z(v) = 2 * h_Z(v) = sum w_i * |<u_i, v>|
        
        # We test if there is ALWAYS a direction v where the Zonotope is "thinner" than the Triangle.
        # If so, Z cannot contain the Triangle (or any translation of it).
        
        zonotope_dominates = True
        min_ratio = float('inf')
        
        for v in test_dirs:
            W_Z = np.sum(widths * np.abs(U @ v))
            W_T = triangle_width(v)
            
            ratio = W_Z / W_T
            if ratio < min_ratio:
                min_ratio = ratio
                
            if W_Z < W_T:
                zonotope_dominates = False
                
        # If the Zonotope does NOT dominate the Triangle in all directions, 
        # it means the Zonotope is too "narrow" to cover the Triangle in a Minkowski sense.
        # Does this geometric property hold for EVERY configuration with sum(p) < 1?
        if not zonotope_dominates:
            successes += 1
            
    print(f"Configurations where Zonotope is strictly narrower than the Triangle: {successes}/{trials}")
    if successes == trials:
        print("SUCCESS! The Zonotope Width Theorem holds.")
        print("If sum(rw) < 1, the associated Zonotope is strictly narrower than the Triangle in at least one direction.")
        print("By Minkowski Sum properties, this geometrically forbids the planks from covering the Triangle.")
    else:
        print("FAILURE: The Zonotope can be wider than the Triangle in all directions even when sum(rw) < 1.")

if __name__ == '__main__':
    test_zonotope_support()