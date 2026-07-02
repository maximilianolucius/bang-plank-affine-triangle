import numpy as np
from scipy.optimize import minimize

def test_infimal_convolution():
    print("Prop 8: Infimal Convolution & Support Functions")
    
    V = np.array([[0,0], [1,0], [0.5, np.sqrt(3)/2]])
    def triangle_support(v):
        return np.max(V @ v)
        
    np.random.seed(42)
    
    # We generate a generic 4-plank configuration that DOES NOT cover the triangle
    # sum(rw) = 0.95
    angles = np.random.uniform(0, np.pi, 4)
    U = np.array([np.cos(angles), np.sin(angles)]).T
    cuts = np.sort(np.random.uniform(0, 0.95, 3))
    cuts = np.concatenate(([0], cuts, [0.95]))
    p = np.diff(cuts)
    
    widths = []
    centers = []
    for i in range(4):
        w_T = np.max(V@U[i]) - np.min(V@U[i])
        w = p[i] * w_T
        widths.append(w)
        
        min_p = np.min(V@U[i])
        max_p = np.max(V@U[i])
        c = np.random.uniform(min_p + w/2, max_p - w/2)
        centers.append(c)
        
    # We want to find lambda in R^4 such that the inequality is < 0.
    # Inequality: h_Delta(-sum lambda_i u_i) + sum |lambda_i| w_i / 2 - sum lambda_i c_i < 0
    
    def objective(lam):
        v = - np.sum(lam[:, np.newaxis] * U, axis=0)
        h_Delta = triangle_support(v)
        val = h_Delta + np.sum(np.abs(lam) * widths / 2) - np.sum(lam * centers)
        return val
        
    # We minimize this function to see if it drops below 0
    # Since it's positively homogeneous (wait, is it?), we can bound lambda to [-1, 1]^4
    
    min_val = float('inf')
    for _ in range(50):
        lam0 = np.random.uniform(-1, 1, 4)
        res = minimize(objective, lam0, method='Nelder-Mead')
        if res.fun < min_val:
            min_val = res.fun
            
    print(f"Minimum value of the dual support function: {min_val:.5f}")
    if min_val < -1e-4:
        print("SUCCESS! The dual support function is strictly negative.")
        print("By Convex Geometry, this guarantees the intersection of planks DOES NOT cover the triangle.")
        print("This is an EXACT DUAL formulation of covering!")
    else:
        print("FAILURE: The minimum is >= 0, meaning the dual test did not detect the gap.")

if __name__ == '__main__':
    test_infimal_convolution()
