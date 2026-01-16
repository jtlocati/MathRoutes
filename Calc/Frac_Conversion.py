# TRIG_FROM_FRACTION (TI-84 Plus CE Python)
# Input like:  sin(4/5)   and quadrant like: Q2
# Then choose which trig value(s) to display in exact fraction form.

import math

# ----------------------------
# Helpers
# ----------------------------
def gcd(a, b):
    a = abs(int(a)); b = abs(int(b))
    while b:
        a, b = b, a % b
    return a

def reduce_frac(n, d):
    if d == 0:
        return (n, d)
    g = gcd(n, d)
    n //= g
    d //= g
    if d < 0:
        n = -n
        d = -d
    return (n, d)

def is_square(n):
    if n < 0: return False
    r = int(math.isqrt(n))
    return r*r == n

def fmt_ratio(num_kind, num_val, den, sign):
    # num_kind: "int" or "sqrt"
    # sign: +1 or -1 applied to overall value
    if den == 0:
        return "undefined"
    if sign < 0:
        sign_str = "-"
    else:
        sign_str = ""

    if num_kind == "int":
        n = int(num_val)
        d = int(den)
        # reduce
        n, d = reduce_frac(n, d)
        # apply sign to numerator
        n = n if sign > 0 else -n
        # format
        if d == 1:
            return str(n)
        return str(n) + "/" + str(d)

    # sqrt form
    d = int(den)
    # keep sign outside (don’t try to simplify radicals)
    if d == 1:
        return sign_str + "sqrt(" + str(int(num_val)) + ")"
    return sign_str + "sqrt(" + str(int(num_val)) + ")/" + str(d)

def quad_signs(q):
    # returns sign for (sin, cos, tan)
    q = q.upper().strip()
    if q == "Q1": return (+1, +1, +1)
    if q == "Q2": return (+1, -1, -1)
    if q == "Q3": return (-1, -1, +1)
    if q == "Q4": return (-1, +1, -1)
    return None

def parse_input(s):
    s = s.strip().lower().replace(" ", "")
    # expects something like sin(4/5)
    if "(" not in s or ")" not in s:
        return None
    fn = s.split("(")[0]
    inside = s[s.find("(")+1 : s.rfind(")")]
    if "/" not in inside:
        return None
    a_str, b_str = inside.split("/", 1)
    try:
        a = int(a_str)
        b = int(b_str)
    except:
        return None
    if b == 0:
        return None
    a, b = reduce_frac(a, b)
    # use magnitudes for triangle; signs come from quadrant
    return (fn, abs(a), abs(b))

# ----------------------------
# Build triangle from given trig
# ----------------------------
def build_triangle(fn, a, b):
    # returns magnitudes (opp, adj, hyp) where opp>=0, adj>=0, hyp>=0
    # and maybe adj/hyp/etc can be sqrt(...) if not perfect square.
    # We'll store sides as (kind, val) where kind in {"int","sqrt"} and val>=0
    if fn == "sin":
        opp = ("int", a)
        hyp = ("int", b)
        rad = b*b - a*a
        if rad < 0: return None
        if is_square(rad):
            adj = ("int", int(math.isqrt(rad)))
        else:
            adj = ("sqrt", rad)
        return (opp, adj, hyp)

    if fn == "cos":
        adj = ("int", a)
        hyp = ("int", b)
        rad = b*b - a*a
        if rad < 0: return None
        if is_square(rad):
            opp = ("int", int(math.isqrt(rad)))
        else:
            opp = ("sqrt", rad)
        return (opp, adj, hyp)

    if fn == "tan":
        opp = ("int", a)
        adj = ("int", b)
        rad = a*a + b*b
        if is_square(rad):
            hyp = ("int", int(math.isqrt(rad)))
        else:
            hyp = ("sqrt", rad)
        return (opp, adj, hyp)

    if fn == "csc":
        # csc = hyp/opp = a/b  => hyp=a, opp=b
        hyp = ("int", a)
        opp = ("int", b)
        rad = a*a - b*b
        if rad < 0: return None
        if is_square(rad):
            adj = ("int", int(math.isqrt(rad)))
        else:
            adj = ("sqrt", rad)
        return (opp, adj, hyp)

    if fn == "sec":
        # sec = hyp/adj = a/b => hyp=a, adj=b
        hyp = ("int", a)
        adj = ("int", b)
        rad = a*a - b*b
        if rad < 0: return None
        if is_square(rad):
            opp = ("int", int(math.isqrt(rad)))
        else:
            opp = ("sqrt", rad)
        return (opp, adj, hyp)

    if fn == "cot":
        # cot = adj/opp = a/b => adj=a, opp=b
        adj = ("int", a)
        opp = ("int", b)
        rad = a*a + b*b
        if is_square(rad):
            hyp = ("int", int(math.isqrt(rad)))
        else:
            hyp = ("sqrt", rad)
        return (opp, adj, hyp)

    return None

# ----------------------------
# Compute requested trig outputs
# ----------------------------
def trig_values(opp, adj, hyp, q):
    ss, cs, ts = quad_signs(q)  # signs for sin, cos, tan

    # magnitudes
    ok, ov = opp
    ak, av = adj
    hk, hv = hyp

    # For ratios, we need a single numerator kind; if numerator is sqrt, keep sqrt.
    # Denominator must be int if possible; if denom is sqrt we keep as sqrt(...) (rare here).
    # (In our construction, denom will be int except for some tan/cot involving sqrt adj/opp.)

    # sin = opp/hyp
    sin_s = fmt_ratio(ok, ov, hv if hk=="int" else 1, ss) if hk=="int" else (("-" if ss<0 else "") + str(ov) + "/sqrt(" + str(hv) + ")")

    # cos = adj/hyp
    cos_s = fmt_ratio(ak, av, hv if hk=="int" else 1, cs) if hk=="int" else (("-" if cs<0 else "") + str(av) + "/sqrt(" + str(hv) + ")")

    # tan = opp/adj
    # If adj is sqrt, show opp/sqrt(...)
    if ak == "int":
        tan_s = fmt_ratio(ok, ov, av, ts)
    else:
        tan_s = ("-" if ts<0 else "") + str(ov) + "/sqrt(" + str(av) + ")"

    # csc = hyp/opp (same sign as sin)
    if ok == "int":
        csc_s = fmt_ratio(hk, hv, ov, ss) if hk=="int" else (("-" if ss<0 else "") + "sqrt(" + str(hv) + ")/" + str(ov))
    else:
        # opp is sqrt: hyp/sqrt(...)
        csc_s = ("-" if ss<0 else "") + str(hv) + "/sqrt(" + str(ov) + ")"

    # sec = hyp/adj (same sign as cos)
    if ak == "int":
        sec_s = fmt_ratio(hk, hv, av, cs) if hk=="int" else (("-" if cs<0 else "") + "sqrt(" + str(hv) + ")/" + str(av))
    else:
        sec_s = ("-" if cs<0 else "") + str(hv) + "/sqrt(" + str(av) + ")"

    # cot = adj/opp (same sign as tan)
    if ok == "int":
        if ak == "int":
            cot_s = fmt_ratio("int", av, ov, ts)
        else:
            cot_s = ("-" if ts<0 else "") + "sqrt(" + str(av) + ")/" + str(ov)
    else:
        cot_s = ("-" if ts<0 else "") + str(av) + "/sqrt(" + str(ov) + ")"

    return {
        "sin": sin_s,
        "cos": cos_s,
        "tan": tan_s,
        "csc": csc_s,
        "sec": sec_s,
        "cot": cot_s
    }

# ----------------------------
# Main
# ----------------------------
while True:
    print("\n=== TRIG FROM FRACTION ===")
    s = input("Input (e.g. sin(4/5)) or QUIT: ").strip()
    if s.upper() == "QUIT":
        break

    parsed = parse_input(s)
    if parsed is None:
        print("Bad input format. Use like: sin(4/5)")
        continue

    fn, a, b = parsed
    q = input("Quadrant (Q1/Q2/Q3/Q4): ").strip().upper()
    if quad_signs(q) is None:
        print("Bad quadrant.")
        continue

    tri = build_triangle(fn, a, b)
    if tri is None:
        print("That fraction doesn't make a real triangle.")
        continue

    opp, adj, hyp = tri
    vals = trig_values(opp, adj, hyp, q)


    print("1.) sin(theta) =", vals["sin"])
    print("2.) cos(theta) =", vals["cos"])
    print("3.) tan(theta) =", vals["tan"])
    print("4.) cot(theta) =", vals["cot"])
    print("5.) csc(theta) =", vals["csc"])
    print("6.) sec(theta) =", vals["sec"])

