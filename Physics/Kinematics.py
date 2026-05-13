import math

def get_value(name):
    raw = input(f"Enter {name} (or type 'x' if unknown): ").strip().lower()
    if raw == "x":
        return None
    return float(raw)

def solve_kinematics(s, vi, vf, a, t):
    # 1) vf = vi + a*t
    if vf is None and vi is not None and a is not None and t is not None:
        return ("Final velocity", vi + a * t)

    if vi is None and vf is not None and a is not None and t is not None:
        return ("Initial velocity", vf - a * t)

    if a is None and vf is not None and vi is not None and t is not None and t != 0:
        return ("Acceleration", (vf - vi) / t)

    if t is None and vf is not None and vi is not None and a is not None and a != 0:
        return ("Time", (vf - vi) / a)

    # 2) s = vi*t + 1/2*a*t^2
    if s is None and vi is not None and a is not None and t is not None:
        return ("Displacement", vi * t + 0.5 * a * t**2)

    if vi is None and s is not None and a is not None and t is not None and t != 0:
        return ("Initial velocity", (s - 0.5 * a * t**2) / t)

    if a is None and s is not None and vi is not None and t is not None and t != 0:
        return ("Acceleration", 2 * (s - vi * t) / (t**2))

    # 3) s = vf*t - 1/2*a*t^2
    if vf is None and s is not None and a is not None and t is not None and t != 0:
        return ("Final velocity", (s + 0.5 * a * t**2) / t)

    # 4) vf^2 = vi^2 + 2*a*s
    if vf is None and vi is not None and a is not None and s is not None:
        value = vi**2 + 2 * a * s
        if value < 0:
            return ("Error", "No real solution for final velocity.")
        return ("Final velocity", math.sqrt(value))

    if vi is None and vf is not None and a is not None and s is not None:
        value = vf**2 - 2 * a * s
        if value < 0:
            return ("Error", "No real solution for initial velocity.")
        return ("Initial velocity", math.sqrt(value))

    if a is None and vf is not None and vi is not None and s is not None and s != 0:
        return ("Acceleration", (vf**2 - vi**2) / (2 * s))

    if s is None and vf is not None and vi is not None and a is not None and a != 0:
        return ("Displacement", (vf**2 - vi**2) / (2 * a))

    # 5) s = ((vi + vf) / 2) * t
    if s is None and vi is not None and vf is not None and t is not None:
        return ("Displacement", ((vi + vf) / 2) * t)

    if t is None and s is not None and vi is not None and vf is not None and (vi + vf) != 0:
        return ("Time", (2 * s) / (vi + vf))

    return ("Error", "Not enough valid information to solve exactly one variable.")

def main():
    print("Kinematics Solver")
    print("Use 'x' for the unknown value.")
    print("Variables:")
    print("s  = displacement (m)")
    print("vi = initial velocity (m/s)")
    print("vf = final velocity (m/s)")
    print("a  = acceleration (m/s^2)")
    print("t  = time (s)")
    print()

    s = get_value("displacement s")
    vi = get_value("initial velocity vi")
    vf = get_value("final velocity vf")
    a = get_value("acceleration a")
    t = get_value("time t")

    unknowns = [s, vi, vf, a, t].count(None)
    if unknowns != 1:
        print("\nError: Enter exactly one unknown.")
        return

    name, result = solve_kinematics(s, vi, vf, a, t)

    print()
    if name == "Error":
        print(result)
    else:
        print(f"{name} = {result}")

if __name__ == "__main__":
    main()