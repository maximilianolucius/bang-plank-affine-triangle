import math, random

def dot(u, v): return sum(a*b for a,b in zip(u,v))
def norm(u): return math.sqrt(dot(u,u))
def normalize(u):
    n = norm(u)
    return [x/n for x in u]
def sub(u, v): return [a-b for a,b in zip(u,v)]
def add(u, v): return [a+b for a,b in zip(u,v)]
def mul(s, u): return [s*x for x in u]

V = [[0.0, 0.0], [1.0, 0.0], [0.5, math.sqrt(3)/2]]
def projs(u): return [dot(v, u) for v in V]
def triangle_width(u):
    p = projs(u)
    return max(p) - min(p)

def run_flow_experiment():
    grid = []
    for i in range(20):
        a = i / 19.0
        for j in range(20 - i):
            b = j / 19.0
            c = 1.0 - a - b
            grid.append([a*V[0][0] + b*V[1][0] + c*V[2][0], a*V[0][1] + b*V[1][1] + c*V[2][1]])
            
    N = [
        normalize([0, -1]),
        normalize([math.sqrt(3)/2, 0.5]),
        normalize([-math.sqrt(3)/2, 0.5])
    ]
    
    random.seed(42)
    successes = 0
    failures = 0
    
    for _ in range(100):
        angles = [random.uniform(0, math.pi) for _ in range(4)]
        U = [[math.cos(a), math.sin(a)] for a in angles]
        
        assignments = [random.randint(0, 3) for _ in range(len(grid))]
        
        def compute_widths(U_dirs):
            w = 0
            for i in range(4):
                pts = [grid[k] for k, a in enumerate(assignments) if a == i]
                if pts:
                    p = [dot(pt, U_dirs[i]) for pt in pts]
                    w += (max(p) - min(p)) / triangle_width(U_dirs[i])
            return w
            
        orig_rw = compute_widths(U)
        
        U_new = []
        for i in range(4):
            # find closest facet normal
            best_n = N[0]
            max_dot = -1
            for n in N:
                d = dot(n, U[i])
                if abs(d) > max_dot:
                    max_dot = abs(d)
                    best_n = n if d > 0 else mul(-1, n)
            
            u_next = add(U[i], mul(0.1, sub(best_n, U[i])))
            U_new.append(normalize(u_next))
            
        new_rw = compute_widths(U_new)
        
        if new_rw <= orig_rw + 1e-9:
            successes += 1
        else:
            failures += 1
            
    print(f"Flow step results: {successes} decreased/maintained, {failures} increased.")

if __name__ == '__main__':
    run_flow_experiment()
