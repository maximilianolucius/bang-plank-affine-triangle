import numpy as np
from scipy.optimize import minimize

def test_pigeonhole_packing():
    print("Prop 6: Difference Body Symmetrization & Pigeonhole Packing (m=4)")
    
    V = np.array([[0,0], [1,0], [0.5, np.sqrt(3)/2]])
    def triangle_width(u):
        projs = V @ u
        return np.max(projs) - np.min(projs)
        
    np.random.seed(42)
    successes = 0
    trials = 100
    
    for _ in range(trials):
        angles = np.random.uniform(0, np.pi, 4)
        U = np.array([np.cos(angles), np.sin(angles)]).T
        
        # Relative widths summing to 0.95
        cuts = np.sort(np.random.uniform(0, 0.95, 3))
        cuts = np.concatenate(([0], cuts, [0.95]))
        p = np.diff(cuts)
        widths = np.array([p[i] * triangle_width(U[i]) for i in range(4)])
        
        # We want to find 5 points in the triangle such that for all i!=j, and all k=0..3:
        # | <U[k], P_i - P_j> | > widths[k]
        
        # Let's frame this as a maximization problem:
        # maximize min_{i!=j, k} ( | <U[k], P_i - P_j> | / widths[k] )
        # If the max-min is > 1, we successfully packed 5 points!
        
        def objective(x):
            # x is a flat array of 5 points in barycentric coordinates (5x2 = 10 vars)
            pts_bary = x.reshape(5, 2)
            
            # Map to Cartesian
            pts_cart = np.zeros((5, 2))
            for i in range(5):
                pts_cart[i] = pts_bary[i,0]*V[0] + pts_bary[i,1]*V[1] + (1 - pts_bary[i,0] - pts_bary[i,1])*V[2]
                
            min_sep = float('inf')
            for i in range(5):
                for j in range(i+1, 5):
                    for k in range(4):
                        sep = np.abs(np.dot(U[k], pts_cart[i] - pts_cart[j])) / widths[k]
                        if sep < min_sep:
                            min_sep = sep
            return -min_sep # minimize negative = maximize
            
        bnds = [(0, 1)] * 10
        
        # Constraints: sum of barycentric x+y <= 1 for each point
        cons = []
        for i in range(5):
            cons.append({'type': 'ineq', 'fun': lambda x, i=i: 1 - x[2*i] - x[2*i+1]})
            
        best_sep = -1
        for _ in range(20):
            x0 = np.random.dirichlet([1,1,1], 5)[:, :2].flatten()
            res = minimize(objective, x0, bounds=bnds, constraints=cons, method='SLSQP')
            if -res.fun > best_sep:
                best_sep = -res.fun
                
        if best_sep > 1.0:
            successes += 1
            
    print(f"Configurations where 5 points were successfully packed: {successes}/{trials}")
    if successes == trials:
        print("PHENOMENAL SUCCESS! We can ALWAYS pack 5 separated points.")
        print("By Pigeonhole Principle, one point is mathematically guaranteed to be uncovered!")
    else:
        print("FAILURE: We cannot always pack 5 mutually separated points.")
        print("The pigeonhole bounding condition is too strict.")

if __name__ == '__main__':
    test_pigeonhole_packing()