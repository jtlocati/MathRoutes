# TI-84 Plus CE Python
# Exact trig evaluator for pi-form angles

SIN_REF = {0: "0", 30: "1/2", 45: "sqrt(2)/2", 60: "sqrt(3)/2", 90: "1"}
COS_REF = {0: "1", 30: "sqrt(3)/2", 45: "sqrt(2)/2", 60: "1/2", 90: "0"}

FUNCS = ("sin", "cos", "tan", "csc", "sec", "cot")

def strip_parens(s):
    if len(s) >= 2 and s[0] == "(" and s[-1] == ")":
        return s[1:-1]
    return s

def parse_pi_angle(angle):
    angle = angle.replace("π", "pi")

    if angle == "0":
        return 0, 1   # numerator, denominator

    sign = 1
    if angle[0] == "-":
        sign = -1
        angle = angle[1:]

    if "pi" not in angle:
        raise ValueError("Angle must contain pi")

    parts = angle.split("pi")

    if parts[0] == "":
        num = 1
    else:
        num = int(parts[0])

    den = 1
    if len(parts[1]) > 0:
        if parts[1][0] != "/":
            raise ValueError("Bad angle format")
        den = int(parts[1][1:])

    return sign * num, den

def parse_expression(expr):
    s = expr.lower().strip()
    s = s.replace(" ", "").replace("*", "").replace("π", "pi")

    func = None
    for f in FUNCS:
        if s.startswith(f):
            func = f
            s = s[len(f):]
            break
    if func is None:
        raise ValueError("Must start with sin, cos, tan, csc, sec, or cot")

    s = strip_parens(s)
    num, den = parse_pi_angle(s)
    return func, num, den

def simplify_sign(val, sign):
    if val == "0":
        return "0"
    return val if sign == 1 else "-" + val

def reciprocal(val):
    sign = ""
    if val.startswith("-"):
        sign = "-"
        val = val[1:]

    if val == "0":
        return "undefined"
    if val == "1":
        return sign + "1"
    if val == "1/2":
        return sign + "2"
    if val == "sqrt(2)/2":
        return sign + "sqrt(2)"
    if val == "sqrt(3)/2":
        return sign + "2sqrt(3)/3"
    if val == "sqrt(3)":
        return sign + "sqrt(3)/3"
    if val == "sqrt(3)/3":
        return sign + "sqrt(3)"

    return sign + "1/(" + val + ")"

def divide(a, b):
    if b == "0":
        return "undefined"
    if a == "0":
        return "0"

    sign = 1
    if a.startswith("-"):
        sign *= -1
        a = a[1:]
    if b.startswith("-"):
        sign *= -1
        b = b[1:]

    table = {
        ("1/2", "sqrt(3)/2"): "sqrt(3)/3",
        ("sqrt(3)/2", "1/2"): "sqrt(3)",
        ("sqrt(2)/2", "sqrt(2)/2"): "1",
        ("1", "1/2"): "2",
        ("1", "sqrt(2)/2"): "sqrt(2)",
        ("1", "sqrt(3)/2"): "2sqrt(3)/3",
    }

    out = table.get((a, b), "(" + a + ")/(" + b + ")")
    return out if sign == 1 else "-" + out

def trig_exact(func, num, den):
    deg = (num * 180) // den
    deg = deg % 360

    if deg == 0:
        sinv, cosv = "0", "1"
    elif deg == 90:
        sinv, cosv = "1", "0"
    elif deg == 180:
        sinv, cosv = "0", "-1"
    elif deg == 270:
        sinv, cosv = "-1", "0"
    else:
        if 0 < deg < 90:
            ref, ss, cs = deg, 1, 1
        elif 90 < deg < 180:
            ref, ss, cs = 180 - deg, 1, -1
        elif 180 < deg < 270:
            ref, ss, cs = deg - 180, -1, -1
        else:
            ref, ss, cs = 360 - deg, -1, 1

        if ref not in SIN_REF:
            return "unsupported angle"

        sinv = simplify_sign(SIN_REF[ref], ss)
        cosv = simplify_sign(COS_REF[ref], cs)

    if func == "sin": return sinv
    if func == "cos": return cosv
    if func == "tan": return divide(sinv, cosv)
    if func == "cot": return divide(cosv, sinv)
    if func == "sec": return reciprocal(cosv)
    if func == "csc": return reciprocal(sinv)

    return "invalid function"

print("TI-84 Exact Trig Evaluator (pi-form only)")
print("Type q to quit\n")

while True:
    expr = input("Enter trig expression: ")
    if expr.lower() in ("q", "quit", "exit"):
        break
    try:
        func, num, den = parse_expression(expr)
        result = trig_exact(func, num, den)
        print(expr + " = " + result + "\n")
    except Exception as e:
        print("Error: " + str(e) + "\n")
