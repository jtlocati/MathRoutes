import math
#balls
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

# TI-84 Python does NOT support math.isqrt(), so we use sqrt-based integer check
def is_square(n):
    if n < 0:
        return False
    r = int(math.sqrt(n))
    return r * r == n

def fmt_ratio(num_kind, num_val, den, sign):
    if den == 0:
        return "undefined"

    if num_kind == "int":
        n = int(num_val)
        d = int(den)

        n, d = reduce_frac(n, d)
        n = n if sign > 0 else -n

        if d == 1:
            return str(n)
        return str(n) + "/" + str(d)

    # sqrt form
    d = int(den)
    sign_str = "-" if sign < 0 else ""
    if d == 1:
        return sign_str + "sqrt(" + str(int(num_val)) + ")"
    return sign_str + "sqrt(" + str(int(num_val)) + ")/" + str(d)

def quad_signs(q):
    q = q.upper().strip()
    if q == "Q1": return (+1, +1, +1)  # sin, cos, tan
    if q == "Q2": return (+1, -1, -1)
    if q == "Q3": return (-1, -1, +1)
    if q == "Q4": return (-1, +1, -1)
    return None

def parse_input(s):
    s = s.strip().lower().replace(" ", "")
    if "(" not in s or ")" not in s:
        return None

    fn = s.split("(")[0]
    if fn not in ("sin", "cos", "tan"):
        return None

    inside = s[s.find("(") + 1 : s.rfind(")")]
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
    return (fn, abs(a), abs(b))

def build_triangle(fn, a, b):
    # returns magnitudes (opp, adj, hyp) as (kind, val)
    if fn == "sin":
        opp = ("int", a)
        hyp = ("int", b)
        rad = b*b - a*a
        if rad < 0:
            return None
        if is_square(rad):
            adj = ("int", int(math.sqrt(rad)))
        else:
            adj = ("sqrt", rad)
        return (opp, adj, hyp)

    if fn == "cos":
        adj = ("int", a)
        hyp = ("int", b)
        rad = b*b - a*a
        if rad < 0:
            return None
        if is_square(rad):
            opp = ("int", int(math.sqrt(rad)))
        else:
            opp = ("sqrt", rad)
        return (opp, adj, hyp)

    if fn == "tan":
        opp = ("int", a)
        adj = ("int", b)
        rad = a*a + b*b
        if is_square(rad):
            hyp = ("int", int(math.sqrt(rad)))
        else:
            hyp = ("sqrt", rad)
        return (opp, adj, hyp)

    return None

def trig_values(opp, adj, hyp, q):
    ss, cs, ts = quad_signs(q)

    ok, ov = opp
    ak, av = adj
    hk, hv = hyp

    # sin = opp/hyp
    sin_s = fmt_ratio(ok, ov, hv if hk == "int" else 1, ss) if hk == "int" else (
        ("-" if ss < 0 else "") + str(ov) + "/sqrt(" + str(hv) + ")"
    )

    # cos = adj/hyp
    cos_s = fmt_ratio(ak, av, hv if hk == "int" else 1, cs) if hk == "int" else (
        ("-" if cs < 0 else "") + str(av) + "/sqrt(" + str(hv) + ")"
    )

    # tan = opp/adj
    if ak == "int":
        tan_s = fmt_ratio(ok, ov, av, ts)
    else:
        tan_s = ("-" if ts < 0 else "") + str(ov) + "/sqrt(" + str(av) + ")"

    return {"sin": sin_s, "cos": cos_s, "tan": tan_s}

# ----------------------------
# Main loop
# ----------------------------
while True:
    print("\n=== TRIG FROM FRACTION (sin/cos/tan only) ===")
    s = input("Input (e.g. sin(4/5)) or QUIT: ").strip()
    if s.upper() == "QUIT":
        break

    parsed = parse_input(s)
    if parsed is None:
        print("Bad input. Use sin(4/5), cos(3/5), or tan(4/3).")
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

    input("Enter to continue")
