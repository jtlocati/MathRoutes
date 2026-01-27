import re, math
from fractions import Fraction

PI = math.pi

# ---------- formatting: express values as pi/# when possible ----------
def as_pi_frac(x, max_den=48, tol=1e-9):
    """
    Return a string like 'pi/4', '-3pi/2', '0', or a decimal if not close to a pi-rational.
    """
    if abs(x) < tol:
        return "0"
    r = x / PI
    frac = Fraction(r).limit_denominator(max_den)
    approx = float(frac) * PI
    if abs(approx - x) < 1e-6:  # closeness threshold for "pi rational"
        n, d = frac.numerator, frac.denominator
        sign = "-" if n < 0 else ""
        n = abs(n)
        if d == 1:
            if n == 1:
                return f"{sign}pi"
            return f"{sign}{n}pi"
        else:
            if n == 1:
                return f"{sign}pi/{d}"
            return f"{sign}{n}pi/{d}"
    # fallback
    return str(round(x, 6))

def as_num_or_pi(x):
    # use pi-form if it fits, otherwise decimal
    return as_pi_frac(x)

# ---------- safe numeric parsing (supports pi/π) ----------
def safe_num(expr: str) -> float:
    expr = expr.strip().replace("π", "pi")
    allowed = {"pi": PI}
    if not re.fullmatch(r"[0-9\.\+\-\*\/\(\)\sppi]*", expr):
        raise ValueError(f"Bad numeric expression: {expr}")
    return float(eval(expr, {"__builtins__": {}}, allowed))

def normalize(s: str) -> str:
    return s.lower().replace(" ", "").replace("π", "pi")

# ---------- parse equation: y = a trig(inside) + c ----------
def extract_outer(eq: str):
    s = normalize(eq)
    s = s.replace("y=", "").replace("f(x)=", "")
    m = re.search(r"(sin|cos|tan)\(", s)
    if not m:
        raise ValueError("Could not find sin( ), cos( ), or tan( ).")

    trig = m.group(1)
    a_part = s[:m.start()]

    if a_part in ("", "+"):
        a = 1.0
    elif a_part == "-":
        a = -1.0
    else:
        a = safe_num(a_part)

    # match parentheses content
    i = m.end()
    depth = 1
    j = i
    while j < len(s) and depth > 0:
        if s[j] == "(":
            depth += 1
        elif s[j] == ")":
            depth -= 1
        j += 1
    if depth != 0:
        raise ValueError("Unmatched parentheses.")

    inside = s[i:j-1]
    rest = s[j:]
    c = 0.0 if rest == "" else safe_num(rest)
    return trig, a, inside, c

def parse_k_and_b(inside: str):
    """
    Infer k and b so inside is k(x - b).
    Supports common forms:
      1) k(x - b) or k*(x - b)
      2) (x - b)/d   (=> k = 1/d)
      3) kx + m      (=> b = -m/k)
      4) x/d + m     (=> k = 1/d, b = -m/k)
    """
    inside = inside.replace(" ", "")

    # k(x±B)
    m = re.fullmatch(r"(.+?)\*?\((x[+\-].+)\)", inside)
    if m:
        k = safe_num(m.group(1))
        par = m.group(2)
        if par.startswith("x-"):
            b = safe_num(par[2:])
        elif par.startswith("x+"):
            b = -safe_num(par[2:])
        else:
            raise ValueError("Bad (x±...) structure.")
        return k, b

    # (x±B)/d
    m = re.fullmatch(r"\((x[+\-].+)\)\/(.+)", inside)
    if m:
        par = m.group(1)
        d = safe_num(m.group(2))
        k = 1.0 / d
        if par.startswith("x-"):
            b = safe_num(par[2:])
        elif par.startswith("x+"):
            b = -safe_num(par[2:])
        else:
            raise ValueError("Bad (x±...) in (..)/d.")
        return k, b

    # x/d ± ...
    m = re.fullmatch(r"([+\-]?)(x)\/(.+?)([+\-].+)?", inside)
    if m:
        sign = -1.0 if m.group(1) == "-" else 1.0
        d = safe_num(m.group(3))
        k = sign * (1.0 / d)
        m_const = 0.0 if not m.group(4) else safe_num(m.group(4))
        b = -m_const / k
        return k, b

    # kx ± ...
    m = re.fullmatch(r"([+\-]?(?:\d+(?:\.\d+)?(?:\/\d+(?:\.\d+)?)?)?)x([+\-].+)?", inside)
    if m:
        kp = m.group(1)
        if kp in ("", "+"):
            k = 1.0
        elif kp == "-":
            k = -1.0
        else:
            k = safe_num(kp)
        m_const = 0.0 if not m.group(2) else safe_num(m.group(2))
        b = -m_const / k
        return k, b

    raise ValueError(f"Couldn't parse inside: {inside}")

# ---------- compute graph parameters + key points ----------
def params(trig, a, k, b, c):
    amp = abs(a) if trig in ("sin", "cos") else abs(a)  # "vertical stretch" for tan too
    period = (2*PI)/abs(k) if trig in ("sin", "cos") else PI/abs(k)
    phase_shift = b  # because inside is k(x - b)
    v_shift = c
    return amp, period, phase_shift, v_shift

def sin_key_points(a, k, b, c):
    T = (2*PI)/abs(k)
    xs = [b + 0*T/4, b + 1*T/4, b + 2*T/4, b + 3*T/4, b + 4*T/4]
    base = [0, 1, 0, -1, 0]
    labels = ["intercept", "max", "intercept", "min", "intercept"]
    pts = [(labels[i], xs[i], a*base[i] + c) for i in range(5)]
    return T, pts

def cos_key_points(a, k, b, c):
    T = (2*PI)/abs(k)
    xs = [b + 0*T/4, b + 1*T/4, b + 2*T/4, b + 3*T/4, b + 4*T/4]
    base = [1, 0, -1, 0, 1]
    labels = ["max", "intercept", "min", "intercept", "max"]
    pts = [(labels[i], xs[i], a*base[i] + c) for i in range(5)]
    return T, pts

def tan_key_points(a, k, b, c):
    T = PI/abs(k)
    left_asym = b - T/2
    right_asym = b + T/2
    xL = b - T/4
    xR = b + T/4
    pts = [
        ("quarter (tan=-1)", xL, a*(-1) + c),
        ("center (intercept)", b, c),
        ("quarter (tan=+1)", xR, a*(1) + c),
    ]
    return T, pts, (left_asym, right_asym)

# ---------- main ----------
def main():
    print("Enter an equation (use pi or π), like:")
    print("  y = 2sin(2x - pi) + 1")
    print("  y = -cos(x/3 + pi/6) - 2")
    print("  y = 3tan(2(x - pi/4)) + 1\n")

    eq = input("Equation: ").strip()

    trig, a, inside, c = extract_outer(eq)
    k, b = parse_k_and_b(inside)
    amp, per, ph, vs = params(trig, a, k, b, c)

    print("\n--- PARAMETERS (from your equation) ---")
    print(f"function: {trig}")
    print(f"vertical stretch (|a|): {amp}")
    print(f"k: {k}")
    print(f"phase shift (b): {as_pi_frac(ph)}")
    print(f"vertical shift (c): {vs}")
    print(f"period: {as_pi_frac(per)}")
    input("Enter to continue")

    print("\n--- KEY PLOTTING POINTS (one fundamental period) ---")
    if trig == "sin":
        T, pts = sin_key_points(a, k, b, c)
        print(f"fundamental x-interval: [{as_pi_frac(b)}, {as_pi_frac(b+T)}]")
        for name, x, y in pts:
            print(f"{name:10s}: ( {as_pi_frac(x)} , {y} )")
            input("Enter to continue")

    elif trig == "cos":
        T, pts = cos_key_points(a, k, b, c)
        print(f"fundamental x-interval: [{as_pi_frac(b)}, {as_pi_frac(b+T)}]")
        for name, x, y in pts:
            print(f"{name:10s}: ( {as_pi_frac(x)} , {y} )")
            input("Enter to continue")

    else:  # tan
        T, pts, (L, R) = tan_key_points(a, k, b, c)
        print(f"period: {as_pi_frac(T)}")
        print(f"vertical asymptotes: x = {as_pi_frac(L)} and x = {as_pi_frac(R)}")
        print(f"fundamental x-interval: ({as_pi_frac(L)}, {as_pi_frac(R)})")
        for name, x, y in pts:
            print(f"{name:18s}: ( {as_pi_frac(x)} , {y} )")
            input("Enter to continue")

if __name__ == "__main__":
    main()
