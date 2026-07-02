r"""
General span engine on the triangle Delta = {(y,z): y>=0, z>=0, y+z<=1}.
Vertices A=(0,0), B=(1,0), C=(0,1).

Affine forms given by vertex values (vA,vB,vC):  v(y,z) = vA + (vB-vA) y + (vC-vA) z.
Normalized iff min(vertex vals)=0, max=1.

Planks P_i = {g_i in [l_i,h_i]}.  target f.
Free = Delta cap {g1<=l1 or g1>=h1} cap {g2<=l2 or g2>=h2}.
span_f(Free) = max_Free f - min_Free f  (extrema at arrangement vertices).

Float version for search; exact (fractions) version for certification.
Common-edge z=0: g1=(0,1,a1).  SAME: g2=(0,1,a2).  OPP: g2=(1,0,a2).
"""
from fractions import Fraction as Q

# ---------- geometry helpers (generic over number type) ----------

def form_coeffs(vA, vB, vC):
    # v(y,z) = c0 + cy*y + cz*z
    return vA, (vB - vA), (vC - vA)  # (c0, cy, cz)


def evalform(coeffs, p):
    c0, cy, cz = coeffs
    return c0 + cy * p[0] + cz * p[1]


def clip_halfplane(poly, a, b, c, keep_le, zero):
    """Clip convex polygon (list of (x,y)) by {a*x+b*y <= c} (keep_le) or {>= c}.
    Returns new vertex list (possibly empty)."""
    if not poly:
        return poly
    out = []
    n = len(poly)
    def side(p):
        v = a * p[0] + b * p[1] - c
        return v if keep_le else -v   # keep where side <= 0
    for i in range(n):
        cur = poly[i]; nxt = poly[(i + 1) % n]
        sc = side(cur); sn = side(nxt)
        cur_in = sc <= zero
        nxt_in = sn <= zero
        if cur_in:
            out.append(cur)
        if cur_in != nxt_in:
            # intersection point
            t = sc / (sc - sn)
            ix = cur[0] + t * (nxt[0] - cur[0])
            iy = cur[1] + t * (nxt[1] - cur[1])
            out.append((ix, iy))
    return out


def poly_area2(poly):
    """Twice the signed area."""
    s = 0
    n = len(poly)
    for i in range(n):
        x1, y1 = poly[i]; x2, y2 = poly[(i + 1) % n]
        s += x1 * y2 - x2 * y1
    return s


def span_free(g1v, g2v, fv, l1, r1, l2, r2, exact=True):
    if exact:
        zero = Q(0)
        l1, r1, l2, r2 = Q(l1), Q(r1), Q(l2), Q(r2)
        g1v = tuple(Q(x) for x in g1v); g2v = tuple(Q(x) for x in g2v); fv = tuple(Q(x) for x in fv)
        delta = [(Q(0), Q(0)), (Q(1), Q(0)), (Q(0), Q(1))]
    else:
        zero = 0.0
        l1, r1, l2, r2 = float(l1), float(r1), float(l2), float(r2)
        g1v = tuple(float(x) for x in g1v); g2v = tuple(float(x) for x in g2v); fv = tuple(float(x) for x in fv)
        delta = [(0.0, 0.0), (1.0, 0.0), (0.0, 1.0)]
    h1, h2 = l1 + r1, l2 + r2
    g1 = form_coeffs(*g1v); g2 = form_coeffs(*g2v); f = form_coeffs(*fv)
    a1c, b1c = g1[1], g1[2]   # g1 = c0 + a1c*y + b1c*z
    a2c, b2c = g2[1], g2[2]

    # halfplane options per strip (complement of CLOSED plank):
    # strip1 present (r1>0): {g1<=l1} or {g1>=h1}; absent (r1==0): whole Delta
    def options(cc, lo, hi, a, b, present):
        c0 = cc[0]
        if not present:
            return [None]
        return [("le", a, b, lo - c0), ("ge", a, b, hi - c0)]  # g<=lo  ;  g>=hi
    opt1 = options(g1, l1, h1, a1c, b1c, r1 > 0)
    opt2 = options(g2, l2, h2, a2c, b2c, r2 > 0)

    fmin = fmax = None
    for o1 in opt1:
        for o2 in opt2:
            poly = list(delta)
            for o in (o1, o2):
                if o is None:
                    continue
                kind, a, b, c = o
                poly = clip_halfplane(poly, a, b, c, kind == "le", zero)
                if not poly:
                    break
            if not poly:
                continue
            if poly_area2(poly) == 0:   # degenerate cell -> not part of open free set
                continue
            for p in poly:
                val = evalform(f, p)
                if fmin is None or val < fmin[0]:
                    fmin = (val, p)
                if fmax is None or val > fmax[0]:
                    fmax = (val, p)
    if fmin is None:
        return None
    span = fmax[0] - fmin[0]
    return {"fmin": fmin[0], "fmax": fmax[0], "span": span, "R": r1 + r2,
            "gap": span - (1 - (r1 + r2)), "argmin": fmin[1], "argmax": fmax[1]}


LINENAME = {0: "y=0", 1: "z=0", 2: "y+z=1", 3: "g1=l1", 4: "g1=h1", 5: "g2=l2", 6: "g2=h2"}


if __name__ == "__main__":
    # sanity 0: no planks -> span 1
    r = span_free((0, 1, Q(1, 3)), (0, 1, Q(3, 4)), (0, Q(2, 5), 1), 0, 0, 0, 0)
    print("no planks: span", r["span"], "(expect 1)")
    # sanity 1: Hunter tight config: g1=x_B=(0,1,0), g2=x_A=(1,0,0), f=x_C=(0,0,1),
    #           I_i=[0,t_i] -> span should equal 1-R exactly.
    for (t1, t2) in [(Q(1, 3), Q(1, 3)), (Q(1, 4), Q(1, 2)), (Q(2, 5), Q(1, 5))]:
        r = span_free((0, 1, 0), (1, 0, 0), (0, 0, 1), 0, t1, 0, t2)
        print(f"Hunter tight t=({t1},{t2}) R={t1+t2}: span={r['span']} 1-R={1-t1-t2} "
              f"gap={r['gap']}  (expect gap 0)")
    # SAME sample
    r = span_free((0, 1, Q(1, 3)), (0, 1, Q(3, 4)), (0, Q(2, 5), 1),
                  Q(1, 5), Q(1, 10), Q(2, 5), Q(1, 10))
    print("SAME sample: span", r["span"], "gap", r["gap"])
