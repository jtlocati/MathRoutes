import time
import math
import random

def main():
    # In Java: Scanner sc = new Scanner(System.in);
    # In Python, we use input() so no need to create a scanner object.
    ContNotes = True
    ContFunc = True
    IsUser = False
    Users = ["Jet", "izzy", "wyatt"]
    PassKey = [4922, 123456, 9772]
    AttLef = 0
    ContGate = 0
    TotWongTac = 0
    while IsUser == False:
        print("Please enter Passkey:")
        print(">", end="")
        try:
            Password = int(input())
        except ValueError:
            Password = 0
        for i in range(len(Users)):
            DictatorPASS = PassKey[i]
            if DictatorPASS == Password:
                print("______")
                print("USER => " + Users[i])
                print("Hello " + Users[i] + " Welcome to NERVcalc")
                IsUser = True
            ContGate += 1
            if DictatorPASS != Password and ContGate >= len(Users):
                AttLef += 1
                print("______")
                print("inccorect password:")
                print("attemps left " + str(abs(AttLef-3)))
                print("______")
                ContGate = 0
            if AttLef >= 3:
                TotWongTac += 1
                print("______")
                print("Password limit reached:")
                print(" must wait " + str(AttLef * 5 * TotWongTac) + " seconds")
                print("______")
                time.sleep(AttLef * 5 * TotWongTac)
                AttLef = 0
    while ContFunc == True and IsUser == True:
        print("______")
        print("V=VOID")
        print("ALG TEST 1")
        print("(1)PecieWise")
        print("(2)V-3e^(7x+9) + 6 = -6")
        print("(3)V ln(5x - 2) - ln2 = 1")
        print("(4)V log15(4-x) = log15(-2x + 2)")
        print("(5)V log3(2) + log3(8 + x) = log3(x^(2) - 4x)")
        print("(6)Force Flood")
        print("(7)Force Quit")
        print(">", end="")        
        try:
            chooser = int(input())
        except ValueError:
            chooser = 0
        if chooser == 7:
            print("QUITTING....")
            time.sleep(0.2)
            for i in range(30):
                print(" ")
            print("____________________")
            IsUser = False
            ContFunc = False
        elif chooser == 6:
            print("IMPORTANT:")
            print(" to retun back to NERVcalc enter passkey")
            print(" there will be no prompt")
            dots = "......................................"
            time.sleep(4)
            for i in range(20):
                Scabies = int(random.random() * 5) + 0
                if Scabies == 1:
                    print("log(5)\n" + dots)
                    print("          " + str(math.log(5)))
                elif Scabies == 2:
                    print("ln(5)\n"+dots)
                    print("          " + str(math.log(5)))
                elif Scabies == 3:
                    print("10 x 6 + 10\n"+dots)
                    # Replicating Java's string concatenation: "          " + 10*6 becomes "          60"
                    # then "          60" + 10 becomes "          6010"
                    print("          " + str(10*6) + str(10))
                elif Scabies == 4:
                    print("12 + 67\n"+dots)
                    print("          " + str(12) + str(67))
                elif Scabies == 5:
                    print("log(20)\n"+dots)
                    print("          " + str(math.log(20)))
            input()  # Wait for an integer input (reads as string)
            print("USER IMP REC...")
            time.sleep(0.2)
            print("REDIRECTING...")
            time.sleep(2)
            print("__________")
        elif chooser == 1:
            print("______")
            print("TO SOLVE:")
            print("plug the given value to parameters and solve")
            print("___")
            print("if the equastion contains an X^2 then it will be a porlabora")
            print("graph by the 1,3,5,7 rule * run")
            print("___")
            print("enter 3 to see GRAPH")
            input()
            print("_____")
            print("TO GRAPH")
            print("if x is presented in the parameter as: x < # then y int")
            print(" will be 0")
            print("Y-int will be 'b' value connected to the equastion")
            print("enter 3 to return to menu")
            input()
        elif chooser == 2:
            print("______")
            print("#-3e^(7x+9) + 6 = -6")
            print("1- subtract 6 from noth sides")
            print("2- divide by 3")
            print("3- subtract 9 from both sides")
            print("4- solve top")
            print("5- divide by 7")
            print("final: -1.088")
            input()
        elif chooser == 3:
            print("______")
            print("#ln(5x - 2) - ln2 = 1")
            print("1- re-write => ln(A/B)")
            print("    ln(5x-2/2) = e")
            print("2- multiply both sides by 2")
            print("    get rid of denom")
            print("3- add 2 to both sides")
            print("4- divide by 5")
            print("5- (2e~5.436 + 2) /5")
            print("final: ~1.487")
        elif chooser == 4:
            print("______")
            print("log15(4-x) = log15(-2x + 2)")
            print("1- logb(A) = logb(B) => A=B")
            print("    4-x = -2x+2")
            print("2- add 2x to both sides")
            print("    4 + x = 2")
            print("3- subtract 4 from both sides")
            print("final: X = -2")
            input()
        elif chooser == 5:
            print("______")
            print("#log3(2) + log3(8 + x) = log3(x^(2) - 4x)")
            print("1- re-wrie as: logb(A)+logb(B) = log(AxB)")
            print("    log3(2)+log3(8+1)=log3(2(8+x))")
            print("Simplifys => log3(2(8+x)) = log3(x^2-4x)")
            print("2- remove logarythims")
            print("    16+2x=x^2-4x")
            print("simplifys => 0=x^2-6x-16")
            print("3- solve quadratic")
            input()
    # In Java: sc.close(); (not required in Python)
    
if __name__ == "__main__":
    main()
