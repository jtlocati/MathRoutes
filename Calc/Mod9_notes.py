import math


TWOPI = 2 * math.pi

def gcd(a, b):
    a = abs(int(a))
    b = abs(int(b))
    while b != 0:
        a, b = b, a % b
    return a

def safe_eval(s):
    s = s.strip().lower()
    allowed = {
        "sqrt": math.sqrt,
        "pi": math.pi
    }
    return eval(s, {"__builtins__": None}, allowed)

def wrap_0_2pi(x):
    x = x % TWOPI
    if abs(x - TWOPI) < 1e-10:
        x = 0.0
    return x

def unique_angles(angles):
    cleaned = []
    for t in angles:
        t = wrap_0_2pi(t)
        if not cleaned or all(abs(t - u) > 1e-7 for u in cleaned):
            cleaned.append(t)
    cleaned.sort()
    return cleaned

def pi_fraction(theta, denom=12):
    """
    Convert theta (radians) to a simplified fraction of π
    using the given denominator resolution (default 12).
    Covers standard UC angles: pi/6, pi/4, pi/3, pi/2, etc.
    """
    frac = (wrap_0_2pi(theta)) / math.pi  # in [0, 2)
    num = int(round(frac * denom))
    den = denom

    g = gcd(num, den)
    num //= g
    den //= g

    if num == 0:
        return "0"
    if den == 1:
        if num == 1:
            return "pi"
        return str(num) + "pi"
    if num == 1:
        return "pi/" + str(den)
    return str(num) + "pi/" + str(den)




quit = False
while quit == False:
    print("1)Ellipse\n2.)Hyperbola\n3.)Equastion of asymtopes\n4.)Parabola\n5.)Identification\n6.)Rotating")

    selection = int(input(">Select: "))


    if selection == 1:
        print("Equastion:Horazontal/Vertical:\n[(x-h)^2/a^2]+[(y-k)^2/b^2]\n[(x-h)^2/b^2]+[(y-k)^2/a^2]")
        input("")
        print("Center: (h,k)\n Foci: C^(2)=a^(2)-b^(2)")
        input("A>B")
    
    elif selection == 2:
        print("Equastion:Horazontal/Vertical:\n[(x-h)^2/a^2]-[(y-k)^2/b^2]\n[(y-k)^2/a^2]-[(x-h)^2/b^2]")
        input("")
        print("Vertex: a\nCo-vertex: b\ncenter: (h,k)\nFoci: C^(2)=a^(2)+b^(2)")
        input("")

    elif selection == 3:
        print("y=mx+b")

    elif selection == 4:
        print("Equastion:Horazontal/Vertical:\n[(x-h)^2=4p(y-k)]\np>0:up, p<0down\nfoci: (h,k+p)\nDiretrix: y=k-p")
        input("")
        print("[(y-k)^2=4p(x-h)]\nFoci: (h+p, k)\n Direcrix: x=h-p\np>0 RIGHT, p<0 LEFT")

    elif selection == 5:
        print("Ax^2+Cy^2+Dx+Ey+F=0")
        print("Circle: A = C")
        print("Ellipse:AC>0, A ≠ C")
        print("Parabola: AC=0")
        print("Hyperbola: AC<0")
        input("")
        print("Ax^2+Bxy+Cy^2+Dx+Ey+F=0")
        print("P=V^(2)-4AC")
        print("P=0: Porabola\nP<0:Ellipse\nP>0:Hyperbola")
        input("")

    elif selection ==6:
        print("Solve for Theta:\nTan(2_theta)=B/(A-C)")
        input("")
        print("input theta into\nX=x cos(the)-y sin(the)\nY=x sin(the)-y cos(the)")
        input("")
        # EXACT_TRIG_VALUES — TI-84 Python safe

    # Exact-value lookup table
    # Format: angle : (sin, cos, tan)
    EXACT = {
        0:   ("0", "1", "0"),
        30:  ("1/2", "sqrt(3)/2", "sqrt(3)/3"),
        45:  ("sqrt(2)/2", "sqrt(2)/2", "1"),
        60:  ("sqrt(3)/2", "1/2", "sqrt(3)"),
        90:  ("1", "0", "undefined"),

        120: ("sqrt(3)/2", "-1/2", "-sqrt(3)"),
        135: ("sqrt(2)/2", "-sqrt(2)/2", "-1"),
        150: ("1/2", "-sqrt(3)/2", "-sqrt(3)/3"),
        180: ("0", "-1", "0"),

        210: ("-1/2", "-sqrt(3)/2", "sqrt(3)/3"),
        225: ("-sqrt(2)/2", "-sqrt(2)/2", "1"),
        240: ("-sqrt(3)/2", "-1/2", "sqrt(3)"),
        270: ("-1", "0", "undefined"),

        300: ("-sqrt(3)/2", "1/2", "-sqrt(3)"),
        315: ("-sqrt(2)/2", "sqrt(2)/2", "-1"),
        330: ("-1/2", "sqrt(3)/2", "-sqrt(3)/3"),
        360: ("0", "1", "0")
    }

    def parse_input(s):
        s = s.strip().lower().replace(" ", "")
        if "(" not in s or ")" not in s:
            return None

        fn = s.split("(")[0]
        if fn not in ("sin", "cos", "tan"):
            return None

        inside = s[s.find("(")+1:s.rfind(")")]
        try:
            angle = int(inside)
        except:
            return None

        angle %= 360
        return fn, angle

    # ----------------------------
    # Main loop
    # ----------------------------

    print("\n=== EXACT TRIG VALUES ===")
    s = input("Input (e.g. cos(30)) or QUIT: ").strip()
    if s.upper() == "QUIT":
        break

    parsed = parse_input(s)
    if parsed is None:
        print("Bad input. Use sin(30), cos(45), tan(60), etc.")
        continue

    fn, angle = parsed

    if angle not in EXACT:
        print("No exact value for this angle.")
        continue

    sin_v, cos_v, tan_v = EXACT[angle]

    if fn == "sin":
        print(sin_v)
    elif fn == "cos":
        print(cos_v)
    else:
        print(tan_v)

    input("Enter to continue")
    print("plug back into main function")
else:
    print("incorrect selection")

