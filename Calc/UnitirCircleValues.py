import math

def main():
    print("Unit Circle Calculator")
    print("Outputs: sin, cos, tan, cot, sec, csc\n")

    angle = float(input("Enter angle: "))
    mode = input("Is this in degrees or radians? (deg/rad): ").lower()

    if mode == "deg":
        angle = math.radians(angle)

    sin_val = math.sin(angle)
    cos_val = math.cos(angle)

    # rounding to avoid floating errors
    sin_val = round(sin_val, 6)
    cos_val = round(cos_val, 6)

    print("\n--- Unit Circle Values ---")
    print("sin =", sin_val)
    print("cos =", cos_val)

    # tan
    if abs(cos_val) < 1e-9:
        print("tan = undefined")
        print("sec = undefined")
    else:
        tan_val = round(sin_val / cos_val, 6)
        sec_val = round(1 / cos_val, 6)
        print("tan =", tan_val)
        print("sec =", sec_val)

    # cot
    if abs(sin_val) < 1e-9:
        print("cot = undefined")
        print("csc = undefined")
    else:
        cot_val = round(cos_val / sin_val, 6)
        csc_val = round(1 / sin_val, 6)
        print("cot =", cot_val)
        print("csc =", csc_val)


main()
