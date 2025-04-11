import math
import random
import time

def main():
    # Separator for visual clarity
    seperator = "................................"

    # User authentication variables
    Users = ["Jet", "izzy", "wyatt"]
    PassKey = [4922, 123456, 909772]
    IsUser = False
    AttLef = 0
    ContGate = 0
    TotWongTac = 0

    # User Login
    while not IsUser:
        try:
            print("Please enter Passkey:")
            Password = int(input("> "))
        except ValueError:
            print("Invalid input. Enter a number.")
            continue
        
        for i in range(len(Users)):
            DictatorPASS = PassKey[i]
            if DictatorPASS == Password:
                print("______")
                print("USER => " + Users[i])
                print("Hello " + Users[i] + "! Welcome to NERVcalc")
                IsUser = True
                break
        
        ContGate += 1
        if not IsUser and ContGate >= len(Users):
            AttLef += 1
            print("______")
            print("Incorrect password:\nAttempts left " + str(max(0, 3 - AttLef)))
            print("______")
            ContGate = 0

        if AttLef >= 3:
            TotWongTac += 1
            wait_time = AttLef * 5 * TotWongTac
            print("______")
            print("Password limit reached:\nMust wait " + str(wait_time) + " seconds")
            print("______")
            time.sleep(wait_time)
            AttLef = 0

    # Menu Loop
    ContFunc = True
    while ContFunc and IsUser:
        print("______")
        print("ALG TEST 1")
        print("(1) 3x+5, if x ≤ -2 | -2x-7, if x > -2")
        print("(2) x-1, if x ≤ -2 | 2x-1, if -2 < x ≤ 4 | -3x+8, if x > 4")
        print("(6) Force Flood")
        print("(7) Force Quit")
        print("(8) See more options")

        try:
            chooser = int(input("> "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        # Secondary menu
        Chooser2 = 0
        if chooser == 8:
            print(seperator)
            print("(3) Piecewise graph")
            print("(4) Use f/g(x) to solve")
            print("(5) Use f/g/h to solve")
            print("(9) Inverse: f(x) = -2x - 5")
            print("(10) Inverse: f(x) = x/3 + 10")
            print("(11) Inverse?: f(x) = 1/x - 2 | g(x) = 1/x + 2")
            print("(12) BONUS")
            print("(6) Force Flood")
            print("(7) Force Quit")

            try:
                Chooser2 = int(input("> "))
            except ValueError:
                continue

        if chooser == 7 or Chooser2 == 7:
            print("QUITTING....")
            time.sleep(0.2)
            for _ in range(30):
                print(" ")
            print("____________________")
            IsUser = False
            ContFunc = False

        elif chooser == 1 or Chooser2 == 1:
            print("~ For x ≤ -2 use 3x+5")
            print("~ At x = -2, f(-2) = -6 + 5 = -1")
            print("~ Graph (-2,-1) closed ->")
            print("(1) Next:")
            try:
                LocalChooser = int(input())
            except ValueError:
                continue
            if LocalChooser == 1:
                for _ in range(9):
                    print(" ")
                print("For x > -2 use -2x-7")
                print("f(x) = 4 - 7 = -3")
                print("Graph: -3 open ->")
            input()

        elif chooser == 2 or Chooser2 == 2:
            print(seperator)
            print("7 > 4 → f(x) = -3x + 8")
            print("f(7) = -3(7) + 8 = -21 + 8 = -13")
            print("Final: -13")
            input()

        elif chooser == 3 or Chooser2 == 3:
            print(seperator)
            print("2, x ≤ 4")
            print("x - 2, 4 < x < 1")
            print("4x - 6, x ≥ 1")
            input()

        elif chooser == 4 or Chooser2 == 4:
            print(seperator)
            print("______")
            print("Solve for: g(f(-3))")
            print("f(-3) = 2(-3) + 1 = -6 + 1 = -5")
            print("Solve for: g(-5)")
            print("g(-5) = 2(-5) - 6 = -10 - 6 = -16")
            print("Final: -16")
            input()

        elif chooser == 5 or Chooser2 == 5:
            print(seperator)
            print("Finding: g(f(x))")
            print("g(f(x)) = g(9-x) = (9-x)^2 + (9-x)")
            print("= 81 - 18x + x^2 + 9 - x")
            print("x^2 - 19x + 90")
            print("Final: x^2 - 19x + 90")
            input()

        elif chooser == 10 or Chooser2 == 10:
            print(seperator)
            print("x = y / 3")
            print("3 * x - 10 = y / 3 * 3")
            print("Final: f⁻¹(x) = 3x - 10")
            input()

        elif chooser == 11 or Chooser2 == 11:
            print(seperator)
            print("g(1/x - 2) => (1/x - 2) + 2")
            print("1/(1/x) => x")
            print("Second:")
            print("f(1/x - 2) => x + 2 = x")
            input()

        elif chooser == 9 or Chooser2 == 9:
            print(seperator)
            print("y = 2x - 5")
            print("x = 2y - 5")
            print("x + 5 = 2y")
            print("Final: f⁻¹(x) = (x + 5) / 2")
            input()

        elif chooser == 12 or Chooser2 == 12:
            print(seperator)
            print("The shop charges $130 for up to 1 hour.")
            print("$70 per additional hour after the first.")
            print("Final: 130, 0 < x ≤ 1 | 130 + 70(x - 1), x > 1")
            input()

# Call main() to start the program when executed on TI-84 Plus CE
main()
