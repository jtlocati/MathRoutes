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
        print("Solve for Theta: ")
        print("\nUnit Circle (Exact π Form)")
        expr = input("Enter (ex: cos(sqrt(3)/2)): ").strip().lower()

        if len(expr) < 6 or "(" not in expr or not expr.endswith(")"):
            print("Bad format. Use like: sin(1/2) or cos(sqrt(3)/2)")
            continue

        func = expr[:3]
        inside = expr[4:-1]

        try:
            value = safe_eval(inside)
        except:
            print("Couldn't read the value. Use numbers, /, pi, and sqrt(x).")
            continue

        angles = []

        if func == "sin":
            if value < -1 or value > 1:
                print("No real solutions (|value| must be <= 1).")
                continue
            a = math.asin(value)
            angles = [a, math.pi - a]

        elif func == "cos":
            if value < -1 or value > 1:
                print("No real solutions (|value| must be <= 1).")
                continue
            a = math.acos(value)
            angles = [a, TWOPI - a]

        elif func == "tan":
            a = math.atan(value)
            angles = [a, a + math.pi]

        else:
            print("Invalid trig function. Use sin, cos, or tan.")
            continue

        cleaned = unique_angles(angles)

        print("\nResults:")
        for t in cleaned:
            x = round(math.cos(t), 3)
            y = round(math.sin(t), 3)
            print("θ =", pi_fraction(t), "Point:", (x, y))

        again = input("Continue? (y/n): ").strip().lower()
        if again != "y":
            break
    else:
        print("incorrect selection")

