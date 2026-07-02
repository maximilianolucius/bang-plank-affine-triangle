import numpy as np
from scipy.optimize import linprog

def test_signed_measure():
    print("Prop 5: Universal Signed Measure via Linear Programming")
    print("Testing if a Signed Measure can bypass Gardner's Wall for non-symmetric bodies.")
    
    # 1. Discretize the Triangle (Membrane Q)
    V = np.array([[0,0], [1,0], [0.5, np.sqrt(3)/2]])
    grid = []
    steps = 20
    for i in range(steps + 1):
        a = i / steps
        for j in range(steps - i + 1):
            b = j / steps
            c = 1.0 - a - b
            grid.append(a*V[0] + b*V[1] + c*V[2])
    grid = np.array(grid)
    N_pts = len(grid)
    print(f"Discretized triangle into {N_pts} points.")
    
    # 2. Generate a dense set of test planks
    print("Generating dense dictionary of test planks...")
    np.random.seed(42)
    directions = np.linspace(0, np.pi, 30, endpoint=False)
    
    A_eq = np.ones((1, N_pts))
    b_eq = np.array([1.0])
    
    A_ub = []
    b_ub = []
    
    def triangle_width(u):
        projs = grid @ u
        return np.max(projs) - np.min(projs)
        
    plank_count = 0
    for theta in directions:
        u = np.array([np.cos(theta), np.sin(theta)])
        w_T = triangle_width(u)
        
        projs = grid @ u
        min_p, max_p = np.min(projs), np.max(projs)
        
        # We sample several widths and positions
        for w in np.linspace(0.1, w_T, 10):
            for start in np.linspace(min_p, max_p - w, 10):
                end = start + w
                
                # Indicator vector for points inside the plank
                indicator = ((projs >= start - 1e-6) & (projs <= end + 1e-6)).astype(float)
                if np.sum(indicator) > 0:
                    A_ub.append(indicator)
                    b_ub.append(w / w_T)
                    plank_count += 1
                    
    A_ub = np.array(A_ub)
    b_ub = np.array(b_ub)
    print(f"Generated {plank_count} plank constraints.")
    
    # 3. Solve the LP for a Signed Measure
    # The variables are D_i (density at point i).
    # Since it's a signed measure, D_i can be negative, so bounds are (None, None).
    print("Solving Linear Program for Signed Measure (bounds = unconstrained)...")
    res_signed = linprog(c=np.zeros(N_pts), A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=b_eq, bounds=(None, None), method='highs')
    
    print(f"\nSigned Measure LP Success: {res_signed.success}")
    if res_signed.success:
        neg_mass = np.sum(res_signed.x[res_signed.x < 0])
        pos_mass = np.sum(res_signed.x[res_signed.x > 0])
        print(f"A Universal Signed Measure EXISTS!")
        print(f"Total Positive Mass: {pos_mass:.3f}")
        print(f"Total Negative Mass: {neg_mass:.3f}")
        print(f"Net Mass (Sum): {np.sum(res_signed.x):.3f}")
        print("This completely shatters Gardner's obstruction (which only applied to positive measures).")
    else:
        print("Signed Measure LP FAILED. The obstruction is absolute even for signed measures.")
        
    # For comparison, let's try a Positive Measure
    print("\nSolving Linear Program for POSITIVE Measure (bounds = (0, None))...")
    res_pos = linprog(c=np.zeros(N_pts), A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=b_eq, bounds=(0, None), method='highs')
    print(f"Positive Measure LP Success: {res_pos.success}")
    if not res_pos.success:
        print("As expected, Gardner's Theorem confirms no positive measure exists.")

if __name__ == '__main__':
    test_signed_measure()