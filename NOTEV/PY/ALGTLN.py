import time
import random

class NoteSpaceAlg3:
    pass

def main():
    # Create an instance of NoteSpaceAlg3
    player = NoteSpaceAlg3()
    # Initialize Scanner equivalent and control variables
    ContFunc = True
    IsUserPly = True
    seperator = "................................"
    while ContFunc == True and IsUserPly == True:
        print("alg factoring Quiz 1")
        print("(1)3/x-5")
        print("(2)X-4/x(2)x-8")
        print("(3)3/x+7/3x-12/2x-8")
        print("(4)x(2)-2x-48/x(2)+10+24")
        print("(5)2x+1/2-x+x-3/x+1")
        print("(8)x/x+4-x+36/x^(2)-16")
        print("(9)x+2/x(2)-4/x/x-2")
        print("(10)x/x(2)-9/x-3/x")
        print("(6)Force Flood")
        print("(7)Force Quit")
        print(">", end="")
        chooser = int(input())
        if chooser == 7:
            print("QUITTING....")
            time.sleep(0.2)
            for i in range(30):
                print(" ")
            print("____________________")
            IsUserPly = False
            ContFunc = False
        elif chooser == 6:
            print("IMPORTANT:\n to retun back to NERVcalc enter passkey\n there will be no prompt")
            time.sleep(4)
            for i in range(20):
                Scabies = int(random.random() * 5)  # Generates 0-4 as in the Java code
                if Scabies == 1:
                    print("123/45\n" + seperator)
                    print("                           2.733")
                    print(seperator)
                elif Scabies == 2:
                    print("124+34\n" + seperator)
                    print("                            158")
                    print(seperator)
                elif Scabies == 3:
                    print("10 x 6 + 10\n" + seperator)
                    print("                            " + str(10 * 6 + 10))
                    print(seperator)
                elif Scabies == 4:
                    print("12 + 67\n" + seperator)
                    print("                              " + str(12 + 67))
                    print(seperator)
                elif Scabies == 5:
                    print("log(20)\n" + seperator)
                    print("                              1.3")
                    print(seperator)
            cont = int(input())
            if cont == 4922:
                print("USER IMP REC...")
                time.sleep(0.2)
                print("REDIRECTING...")
                time.sleep(2)
                print("__________")
            else:
                print("this aint it fam")
        elif chooser == 1:
            print(seperator)
            print("X = 0 when do is undefined")
            print("x-5=0, x=5")
            input()
        elif chooser == 2:
            print(seperator)
            print("factor top & bottom")
            print("x-4 ->(x-2),\nBottom -(x-4)(x+2)")
            print("cancel out (2+x)")
            print("final: 4, -2")
            input()
        elif chooser == 3:
            print("simplify:\n3x-12 =>3(x-4)\n2x-8 => 2(x-4)")
            print("Exspression becomes:\n3/x+7/3(x-4)/2(x-4)\n=3/x+7*2(x-4)/3(x-4)")
            print("cancel out 3,(x-4)")
            print("Final: 2/x+7")
            input()
        elif chooser == 4:
            print("Factor:\n bottom(x+4),(x+6), ")
            print("top(x+4)(x+6)")
            print("cancel(x+6)\nfinal:(x-8)/x+4")
            input()
        elif chooser == 5:
            print("make some shit up")
            print("final: \n3x^(2)-2+7/x^(2)-x-3")
            input()
        elif chooser == 8:
            print("final:\nx-9/x-4")
            input()
        elif chooser == 9:
            print("factor Bottom:\n(x-2),(x+2)")
            print("becomes:\nx+2/(x-2)(x+2)*x-2/x\nFinal: 1/x")
            input()
        elif chooser == 10:
            print("somplifyy to: x/(x+3),(x-3)/x+3")
            print("cancel out x+3")
            print("becomes: x/x(3-x)\n final:1/x-3")
            input()

if __name__ == '__main__':
    main()
