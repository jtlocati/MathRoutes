import re
from fractions import Fraction

# ---------- exact value formatting ----------
def frac_str(fr: Fraction) -> str:
    fr = Fraction(fr)
    if fr.denominator == 1:
        return str(fr.numerator)
    return f"{fr.numerator}/{fr.denominator}"

def pi_frac_str(fr: Fraction) -> str:
    """Format Fraction * pi as 'pi/#', '3pi/4', '0', etc."""
    fr = Fraction(fr)
    if fr == 0:
        return "0"
    sign = "-" if fr < 0 else ""
    fr = abs(fr)
    n, d = fr.numerator, fr.denominator
    if d == 1:
        if n == 1:
            return f"{sign}pi"
        return f"{sign}{n}pi"
    else:
        if n == 1:
            return f"{sign}pi/{d}"
        return f"{sign}{n}pi/{d}"

def simplify_radical(num, den=1):
    """Return a string for values like 1/2, sqrt(2)/2, sqrt(3), sqrt(3)/3, etc."""
    num = Fraction(num)
    den = Fraction(den)
    val = num / den
    # Should only be used for rational outputs (no radical). Keep anyway.
    return frac_str(val)

def mult_sign(sign, s):
    if s == "0":
        return "0"
    if sign == 1:
        return s
    # sign = -1
    if s.startswith("-"):
        return s[1:]
    return "-" + s

# ---------- unit circle base values ----------
# Reference-angle exact values for sin/cos at:
# 0, 30, 45, 60, 90 degrees
# store as strings for exact output
SIN_REF = {
    0:  "0",
    30: "1/2",
    45: "sqrt(2)/2",
    60: "sqrt(3)/2",
    90: "1",
}
COS_REF = {
    0:  "1",
    30: "sqrt(3)/2",
    45: "sqrt(2)/2",
    60: "1/2",
    90: "0",
}

# ---------- parsing angles ----------
def normalize_angle_pi(fr: Fraction) -> Fraction:
    """Normalize a pi-multiple Fraction to [0, 2). i.e., fr*pi in [0,2pi)."""
    fr = Fraction(fr)
    two = Fraction(2, 1)
    fr = fr % two
    return fr

def parse_pi_multiple(s: str) -> Fraction:
    """
    Parse strings like:
      pi/6, 3pi/4, -5pi/6, 7*pi/12, -pi, 2pi
    Returns Fraction of pi, i.e. angle = (Fraction)*pi
    """
    s = s.strip().lower().replace(" ", "")
    s = s.replace("π", "pi")
    s = s.replace("*", "")

    if "pi" not in s:
        raise ValueError("Radians input must contain pi (like pi/6 or 3pi/4).")

    # Match forms: [sign][num]pi[/den]
    m = re.fullmatch(r"([+\-]?)(\d*)pi(?:/(\d+))?", s)
    if not m:
        raise ValueError("Could not parse pi fraction. Use forms like pi/6, 3pi/4, -pi, 2pi.")

    sign = -1 if m.group(1) == "-" else 1
    num_str = m.group(2)
    den_str = m.group(3)

    num = int(num_str) if num_str not in ("", None) else 1
    den = int(den_str) if den_str not in ("", None) else 1

    return Fraction(sign * num, den)

def parse_degrees(s: str) -> int:
    """Parse degrees like '210', '210°', '210deg'."""
    s = s.strip().lower().replace(" ", "")
    s = s.replace("°", "")
    s = s.replace("deg", "")
    if not re.fullmatch(r"[+\-]?\d+", s):
        raise ValueError("Degrees must be an integer like 210 or 210°.")
    return int(s)

def deg_to_pi_fraction(deg: int) -> Fraction:
    """deg * pi/180"""
    return Fraction(deg, 180)

def is_supported_pi_fraction(fr: Fraction) -> bool:
    """
    We support standard unit-circle angles:
    multiples of pi/12 (15° increments).
    That means fr should have denominator dividing 12 after reduction.
    """
    fr = Fraction(fr)
    # denominator divides 12 iff 12*fr is integer
    return (fr * 12).denominator == 1

def pi_fraction_to_degrees(fr: Fraction) -> int:
    """Convert (fr*pi) to degrees exactly if possible."""
    # degrees = fr*180
    deg = fr * 180
    if deg.denominator != 1:
        raise ValueError("Angle is not an exact integer degree.")
    return deg.numerator

# ---------- trig exact evaluation on unit circle ----------
def ref_angle_deg_and_signs(deg: int):
    """
    Given an angle in degrees normalized to [0,360),
    return reference angle (0..90) and signs for sin/cos.
    """
    deg = deg % 360

    # Quadrantal and axis cases
    if deg in (0, 90, 180, 270):
        ref = {0:0, 90:90, 180:0, 270:90}[deg]
        # signs are handled naturally by quadrant rules below, but fine as is
    # Determine quadrant
    if 0 <= deg <= 90:
        ref = deg
        sin_sign, cos_sign = 1, 1
    elif 90 < deg < 180:
        ref = 180 - deg
        sin_sign, cos_sign = 1, -1
    elif 180 <= deg <= 270:
        ref = deg - 180
        sin_sign, cos_sign = -1, -1
    else:  # 270 < deg < 360
        ref = 360 - deg
        sin_sign, cos_sign = -1, 1

    return ref, sin_sign, cos_sign

def exact_sin_cos_from_deg(deg: int):
    deg = deg % 360
    ref, sgn_sin, sgn_cos = ref_angle_deg_and_signs(deg)

    if ref not in SIN_REF or ref not in COS_REF:
        raise ValueError("Unsupported angle. Use standard unit-circle angles (multiples of 15°).")

    sinv = mult_sign(sgn_sin, SIN_REF[ref])
    cosv = mult_sign(sgn_cos, COS_REF[ref])
    return sinv, cosv

def reciprocal(val: str) -> str:
    """Return exact reciprocal as a simplified string for our known set."""
    if val == "0":
        return "undefined"
    if val == "1":
        return "1"
    if val == "-1":
        return "-1"
    if val == "1/2":
        return "2"
    if val == "-1/2":
        return "-2"
    if val == "sqrt(2)/2":
        return "sqrt(2)"
    if val == "-sqrt(2)/2":
        return "-sqrt(2)"
    if val == "sqrt(3)/2":
        return "2sqrt(3)/3"   # rationalized
    if val == "-sqrt(3)/2":
        return "-2sqrt(3)/3"
    if val == "sqrt(3)":
        return "sqrt(3)/3"
    if val == "-sqrt(3)":
        return "-sqrt(3)/3"
    if val == "sqrt(3)/3":
        return "sqrt(3)"
    if val == "-sqrt(3)/3":
        return "-sqrt(3)"
    # fallback (rare)
    return f"1/({val})"

def divide(a: str, b: str) -> str:
    """Return exact a/b for our known set (tan = sin/cos, cot = cos/sin)."""
    if b == "0":
        return "undefined"
    if a == "0":
        return "0"

    # handle sign
    sign = 1
    if a.startswith("-"):
        sign *= -1
        a = a[1:]
    if b.startswith("-"):
        sign *= -1
        b = b[1:]

    # Known exact pairs for unit circle
    # tan reference values: 0, 1, -1, sqrt(3), sqrt(3)/3 etc.
    key = (a, b)

    tan_map = {
        ("1/2", "sqrt(3)/2"): "sqrt(3)/3",
        ("sqrt(3)/2", "1/2"): "sqrt(3)",
        ("sqrt(2)/2", "sqrt(2)/2"): "1",
        ("1", "0"): "undefined",
        ("0", "1"): "0",
        ("0", "sqrt(3)/2"): "0",
        ("0", "sqrt(2)/2"): "0",
        ("0", "1/2"): "0",
        ("1/2", "1"): "1/2",
        ("sqrt(2)/2", "1"): "sqrt(2)/2",
        ("sqrt(3)/2", "1"): "sqrt(3)/2",
        ("1", "1/2"): "2",
        ("1", "sqrt(2)/2"): "sqrt(2)",
        ("1", "sqrt(3)/2"): "2sqrt(3)/3",
        ("1/2", "0"): "undefined",
        ("sqrt(2)/2", "0"): "undefined",
        ("sqrt(3)/2", "0"): "undefined",
        ("1", "1"): "1",
    }

    # Try tan_map
    if key in tan_map:
        out = tan_map[key]
    else:
        # If not in map, try using reciprocal rules for simple patterns
        # Example: tan = sin/cos; if both are known strings but not mapped, punt
        out = f"({a})/({b})"

    out = mult_sign(sign, out)
    return out

def trig_all(func: str, deg: int):
    sinv, cosv = exact_sin_cos_from_deg(deg)

    func = func.lower()
    if func == "sin":
        return sinv
    if func == "cos":
        return cosv
    if func == "tan":
        return divide(sinv, cosv)
    if func == "cot":
        return divide(cosv, sinv)
    if func == "sec":
        return reciprocal(cosv)
    if func == "csc":
        return reciprocal(sinv)
    raise ValueError("Function must be sin, cos, tan, cot, sec, or csc.")

# ---------- main program ----------
def main():
    print("Unit Circle Exact Evaluator")
    print("Enter either:")
    print("  • trig(angle)   e.g. sin(pi/6), csc(3pi/4), tan(210°), sec(30deg)")
    print("  • degrees only  e.g. 210 or 210°  (returns pi/#)")
    print("Supported angles: standard unit-circle (multiples of 15° / pi/12)\n")

    while True:
        raw = input("Input (or 'q' to quit): ").strip()
        if raw.lower() in ("q", "quit", "exit"):
            break

        try:
            s = raw.strip()

            # Case 1: degree-only input -> return radians in pi/# form
            if re.fullmatch(r"[+\-]?\d+\s*(?:°|deg)?\s*", s.lower()):
                deg = parse_degrees(s)
                pi_fr = deg_to_pi_fraction(deg)
                # normalize to [0,2) in pi multiples for nicer display
                pi_fr_norm = normalize_angle_pi(pi_fr)
                # also show full (not normalized) if you want:
                print(f"{deg}° = {pi_frac_str(pi_fr)} radians  (normalized: {pi_frac_str(pi_fr_norm)})")
                continue

            # Case 2: trig expression
            m = re.fullmatch(r"\s*(sin|cos|tan|cot|sec|csc)\s*\(\s*(.+)\s*\)\s*", s.lower())
            if not m:
                raise ValueError("Input must be like sin(pi/6) or 210°.")

            func = m.group(1)
            inside = m.group(2).strip()

            # If inside has degrees marker, parse degrees
            if "deg" in inside.lower() or "°" in inside:
                deg = parse_degrees(inside)
                pi_fr = deg_to_pi_fraction(deg)
                pi_fr_norm = normalize_angle_pi(pi_fr)
                deg_norm = deg % 360

                val = trig_all(func, deg_norm)
                print(f"{func}({deg}°) = {val}")
                print(f"Angle in radians: {pi_frac_str(pi_fr)}  (normalized: {pi_frac_str(pi_fr_norm)})")
                continue

            # Otherwise: radians in pi/# form
            pi_mult = parse_pi_multiple(inside)
            if not is_supported_pi_fraction(pi_mult):
                raise ValueError("Angle must be a multiple of pi/12 (like pi/6, 5pi/4, 7pi/12, etc).")

            pi_mult_norm = normalize_angle_pi(pi_mult)
            deg = pi_fraction_to_degrees(pi_mult_norm)  # exact integer degrees
            val = trig_all(func, deg)

            print(f"{func}({pi_frac_str(pi_mult)}) = {val}")
            print(f"Angle in degrees (normalized): {deg}°")

        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    main()