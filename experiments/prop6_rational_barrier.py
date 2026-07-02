import numpy as np
from scipy.optimize import minimize

def test_rational_barrier():
    print("Prop 6: The Rational Barrier Bound (m=4)")
    
    V = np.array([[0,0], [1,0], [0.5, np.sqrt(3)/2]])
    def triangle_width(u):
        projs = V @ u
        return np.max(projs) - np.min(projs)
        
    np.random.seed(42)
    successes = 0
    trials = 500
    
    for _ in range(trials):
        angles = np.random.uniform(0, np.pi, 4)
        U = np.array([np.cos(angles), np.sin(angles)]).T
        
        # Relative widths summing to 0.95
        cuts = np.sort(np.random.uniform(0, 0.95, 3))
        cuts = np.concatenate(([0], cuts, [0.95]))
        p = np.diff(cuts)
        
        centers = []
        for i in range(4):
            w = triangle_width(U[i]) * p[i]
            min_p = np.min(V@U[i])
            max_p = np.max(V@U[i])
            c = np.random.uniform(min_p + w/2, max_p - w/2)
            centers.append(c)
            
        def barrier(x_bary):
            x_cart = x_bary[0]*V[0] + x_bary[1]*V[1] + (1 - x_bary[0] - x_bary[1])*V[2]
            
            val = 0
            for i in range(4):
                dist_sq = (np.dot(U[i], x_cart) - centers[i])**2
                w_half_sq = ((triangle_width(U[i]) * p[i]) / 2.0)**2
                val += w_half_sq / max(dist_sq, 1e-12)
            return val
            
        bnds = ((0, 1), (0, 1))
        cons = ({'type': 'ineq', 'fun': lambda x: 1 - x[0] - x[1]})
        
        min_val = float('inf')
        for _ in range(10):
            x0 = np.random.dirichlet([1,1,1])[:2]
            res = minimize(barrier, x0, bounds=bnds, constraints=cons)
            if res.fun < min_val:
                min_val = res.fun
                
        # If the sum of (w_half / dist)^2 is < 1, then ALL terms must be < 1.
        # This implies dist > w_half for ALL i.
        # Thus the point escapes ALL planks!
        if min_val < 1.0:
            successes += 1
            
    print(f"Configurations where Barrier Minimum < 1.0 (Point Escapes): {successes}/{trials}")
    if successes == trials:
        print("SUCCESS! The Rational Barrier provides a strict analytic bound.")
    else:
        print("FAILURE: The Rational Barrier minimum can exceed 1.0 even when sum(rw) < 1.")

if __name__ == '__main__':
    test_rational_barrier()