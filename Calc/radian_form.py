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
while True:
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
