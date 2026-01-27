import math

TWOPI = 2 * math.pi

# ---------------------------
# Safe eval: supports sqrt(x), pi, fractions, + - * / ( )
# Example inputs:
#   sin(1/2)
#   cos(sqrt(3)/2)
#   tan(-1)
#   cos(-2/5)
# ---------------------------

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

def r4(x):
    return round(x, 4)

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

def unique_angles(angles):
    cleaned = []
    for t in angles:
        t = wrap_0_2pi(t)
        if not cleaned or all(abs(t - u) > 1e-7 for u in cleaned):
            cleaned.append(t)
    cleaned.sort()
    return cleaned

def quadrant(theta):
    t = wrap_0_2pi(theta)
    if abs(t - 0) < 1e-10 or abs(t - math.pi/2) < 1e-10 or abs(t - math.pi) < 1e-10 or abs(t - 3*math.pi/2) < 1e-10:
        return "Axis"
    if 0 < t < math.pi/2:
        return "QI"
    if math.pi/2 < t < math.pi:
        return "QII"
    if math.pi < t < 3*math.pi/2:
        return "QIII"
    return "QIV"

# ---------------------------
# Option 1: π-form from sin(v), cos(v), tan(v)
# Input means: sin(theta) = v
# Examples:
#   sin(1/2)
#   cos(sqrt(3)/2)
# ---------------------------
def option_pi_form():
    while True:
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

# ---------------------------
# Option 2: Decimal solving on [0, 2π)
# You enter:
#   sin
#   .8246
# or:
#   cos
#   -2/5
# or:
#   sin
#   sqrt(3)/2
# ---------------------------
def option_decimal_solving():
    while True:
        print("\nTrig Eq Solver on [0, 2π)")
        f = input("Function? (sin/cos/tan): ").strip().lower()

        try:
            a = safe_eval(input("Value a (ex: .8246, -2/5, sqrt(3)/2): ").strip())
        except:
            print("Couldn't read the value. Use numbers, /, pi, and sqrt(x).")
            continue

        sol = []

        if f == "sin":
            if a < -1 or a > 1:
                print("No real solution (|a| must be <= 1).")
            else:
                t = math.asin(a)
                sol = [wrap_0_2pi(t), wrap_0_2pi(math.pi - t)]

        elif f == "cos":
            if a < -1 or a > 1:
                print("No real solution (|a| must be <= 1).")
            else:
                t = math.acos(a)
                sol = [wrap_0_2pi(t), wrap_0_2pi(TWOPI - t)]

        elif f == "tan":
            t = math.atan(a)
            sol = [wrap_0_2pi(t), wrap_0_2pi(t + math.pi)]

        else:
            print("Invalid function.")
            sol = []

        if sol:
            cleaned = unique_angles(sol)

            print("\nSolutions (radians, 4 decimals):")
            for x in cleaned:
                print(r4(x))

            print("\nGeneral solution:")
            if f in ["sin", "cos"]:
                print("x = listed angles + 2πk")
            else:
                print("x = first angle + πk (or listed angles + 2πk)")

        again = input("Continue? (y/n): ").strip().lower()
        if again != "y":
            break


def option_identities():
    print("\nPythagorean Trig Identities:")
    print("sin^2(θ) + cos^2(θ) = 1")
    print("1 + tan^2(θ) = sec^2(θ)")
    print("1 + cot^2(θ) = csc^2(θ)")
    input("\nPress ENTER to return to menu.")

# ---------------------------
# Main menu
# ---------------------------
def main():
    while True:
        print("\n1.) pi form\n2.) decimal solving\n3.) UC picture\n4.) equastions info\n5.) exit")
        try:
            select = int(input("Choose an option: ").strip())
        except:
            print("Enter 1, 2, 3, or 4.")
            continue

        if select == 1:
            option_pi_form()
        elif select == 2:
            option_decimal_solving()
        elif select == 4:
            option_identities()
        elif select == 5:
            break
        else:
            print("Enter 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()
