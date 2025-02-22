import math
import random
import time

class JAVAFINALCH6COMP:
    def Exiter(self, ret):
        # public String Exiter(String ret) throws InterruptedException{
        references = [
            "See you Space Cowboy...",
            "See you at the finish line...",
            "I really want to stay at your house...",
            "May the force be with you...",
            "Mission completed, exiting...",
            "Ill take you to the moon...",
            "You have become death, destroyer of worlds...",
            "Only you can prevent V-buck Scams...",
            "Dont dig straght down...",
            "Dont forget to thank the bus driver...",
            "How disgusting...",
            "Fly me to the moon...",
            "You musin't run away...",
            "Gotta catch them all (at leat this functon)...",
            "Terminateing function, (dramaticly eats potato chip)...",
            "Ill be baaak...",
            "Why So Serious     - The Jonkler",
            "I Came, I Saw, I Compiled...",
            "Ask not what your program can do for you, but what you can do for your program..."
        ]
        randit = int(random.random() * len(references)) + 0
        print(references[randit])
        time.sleep(0.2)  # Thread.sleep(200);
        print(">>this ensures data is not tracable")
        for i in range(0, 5):
            print("\rclosing UsrFile_" + str(int(random.random() * 9999)) + "0")
            time.sleep(0.5)  # Thread.sleep(500);
            print("\r", end="")
        ret = "done!"
        return ret
    # Richer Scale DEF
    def RicherScaleEN(self, Magnitude, ret):
        # public String RicherScaleEN(double Magnitude, String ret) {
        power = (Magnitude * (1.5))
        power2u = (power + 11.8)
        # Extract integer and decimal parts 
        power2uDIV = power2u - math.floor(power2u)
        Econtaner = math.pow(10, power2uDIV)
        Econtaner = round(Econtaner * 100.0) / 100.0  # Round for display
        # Compute total energy
        totalEnergy = math.pow(10, power2u)
        # Print results
        print("> total Energy output (Uncompressed): " + str(totalEnergy))
        ret = "> E ~ " + str(Econtaner) + " x 10^" + str(int(power2u - power2uDIV))
        return ret
    # Richer Scale DEF end------
    # Compounding DEF--------
    # Finds value for timeframe (T)
    def CompoundIntrestTP(self, finret, Begin, intrate, timepr, itera, total):
        # public String CompoundIntrestTP(String finret, double Begin, double intrate, int timepr, double itera, double total){
        intrate *= 0.01
        TPcomp1 = (intrate / itera) + 1
        TPcomp2 = (total / Begin)
        if TPcomp1 <= 0 or TPcomp2 <= 0:
            return "Error: Invalid input for logarithm."
        TPstep21 = math.log(TPcomp1)
        TPstep22 = math.log(TPcomp2)
        TPstep3 = (TPstep22 / TPstep21) / itera
        finret = "The final time frame is: " + str(TPstep3)
        return finret
    # Finds value for starting value (P)
    def CompoundIntrestSV(self, finret, Begin, intrate, timepr, itera, total):
        # public String CompoundIntrestSV(String finret, double Begin, double intrate, int timepr, double itera, double total){
        intrate *= 0.01
        DomCom1 = (intrate / itera) + 1
        DomExe = (itera * timepr)
        findomcom = math.pow(DomCom1, DomExe)
        retfin = (total / findomcom)
        finret = "Final initial value is: " + str(retfin)
        return finret
    # Solves for total output (A)
    def CompoundIntrestFV(self, finret, Begin, intrate, timepr, itera, total):
        # public String CompoundIntrestFV(String finret, double Begin, double intrate, int timepr, double itera, double total){
        intrate *= 0.01
        Expon = (itera * timepr)
        parathe = (intrate / itera) + 1
        parathefin = math.pow(parathe, Expon)
        finnig = (parathefin * Begin)
        finret = "Final output (A) is: " + str(finnig)
        return finret
    # Solving for interest rate (R)
    def CompoundIntrestIR(self, finret, Begin, intrate, timepr, itera, total):
        # public String CompoundIntrestIR(String finret, double Begin, double intrate, int timepr, double itera, double total){
        if Begin <= 0 or total <= 0 or timepr <= 0:
            return "Error: Invalid inputs for interest rate calculation."
        insidesqrt = (total / Begin)
        outSideSqurt = (itera * timepr)
        MstInPar = math.pow(insidesqrt, 1.0 / outSideSqurt)
        mstEquation = ((MstInPar - 1) * itera)
        finret = "The final rate is: " + str(mstEquation * 100) + "%"
        return finret
    # Finds value for # of iterations (N)
    def CompoundIntrestIV(self, finret, Begin, intrate, timepr, itera, total, IholderGen):
        # public String CompoundIntrestIV(String finret, double Begin, double intrate, int timepr, double itera, double total, String IholderGen){
        itfound = False
        finRetFon = ""
        valholdStr = ["Yearly", "Quarterly", "Monthly"]
        valholdInt = [1, 4, 12]
        for i in range(0, len(valholdStr)):
            insidePar = ((intrate / valholdInt[i]) + 1)
            forSol = math.pow(insidePar, (valholdInt[i] * timepr))
            if abs(forSol - total) <= total * 0.05:  # Allow small margin of error
                finRetFon = "Iteration found at: " + str(valholdInt[i]) + " or: " + valholdStr[i]
                itfound = True
                break
        if itfound:
            finret = "Iteration found: " + finRetFon
        else:
            finret = "Iteration cannot be found, closest iteration: " + str(valholdInt[0])
        return finret
    # End of Compound DEF
    # LOG convert DEF
    def LogTOling(self, equastion, ret):
        # public String LogTOling(String equastion, String ret){
        Bfind = ""
        Yfind = ""
        Xfind = equastion[equastion.rfind("}")+1:]
        Bindex = equastion.find("(")
        Yindex = equastion.find(")")
        if Bindex > 0:
            Bfind = equastion[3:Bindex]
        else:
            ret = "error, try input again."
        if Yindex > 0:
            Yfind = equastion[Bindex + 1:Yindex]
        else:
            ret = "error, try input again."
        print("Y: " + Yfind)
        print("B: " + Bfind)
        print("X: " + Xfind)
        ret = "final: " + Bfind + "^" + Xfind + " = " + Yfind
        return ret
    def LinTOlog(self, equastion, retLTL):
        # public String LinTOlog(String equastion, String retLTL){
        Bbreak = ""
        Xbreak = ""
        Ybreak = ""
        Bindex = equastion.find("^")
        Xindex = equastion.find("{")
        Yindex = equastion.find("}")
        Ybreak = equastion[equastion.rfind("}")+1:]
        if Bindex > 0:
            Bbreak = equastion[0:Bindex]
        else:
            retLTL = "input error, try again (error message #1)"
        if Xindex > 0:
            Xbreak = equastion[Bindex + 1:Xindex]
        else:
            retLTL = "input error, try again (error message #2)"
        if Yindex > 0:
            pass
        else:
            retLTL = "input error, try againe (error message #3)"
        print("B: " + Bbreak)
        print("X: " + Xbreak)
        print("Y: " + Ybreak)
        retLTL = "final: LOG" + Bbreak + "(" + Ybreak + ") = " + Xbreak
        return retLTL
    # End of LOG convert DEF
    # Exponental DEF
    def evaluate(self, B, Growth, HarTime, HarTime2, KowHardTime, wordtime2, wordtime22, howman):
        # public double evaluate(int B, int Growth, int HarTime, int HarTime2, int KowHardTime, String wordtime2, String wordtime22, int howman) {
        cosTime = 0
        timecheckword = (wordtime2 != "")
        timecheckknown = (KowHardTime != 1010)  # Ensure time frame is correctly checked
        optio = ["day", "year", "month", "hour", "second", "millisecond", "week"]
        Strwo1 = ""
        Strwo2 = ""
        # Match input time unit with predefined list
        for option in optio:
            if wordtime2 == option:
                Strwo1 = option
                break
        for option in optio:
            if wordtime22 == option:
                Strwo2 = option
                break
        # Time converstion Table:
        if Strwo1 == "day":
            if Strwo2 == "year":
                cosTime = 365 * howman
            elif Strwo2 == "month":
                cosTime = 30 * howman
            elif Strwo2 == "hour":
                cosTime = 24 * howman
            elif Strwo2 == "second":
                cosTime = 86400 * howman
            elif Strwo2 == "millisecond":
                cosTime = 86400000 * howman
            elif Strwo2 == "week":
                cosTime = (1.0 / 7) * howman
            else:
                cosTime = howman  # Same unit
        elif Strwo1 == "year":
            if Strwo2 == "day":
                cosTime = (1.0 / 365) * howman
            elif Strwo2 == "month":
                cosTime = 12 * howman
            elif Strwo2 == "hour":
                cosTime = 8760 * howman
            elif Strwo2 == "second":
                cosTime = 31536000 * howman
            elif Strwo2 == "millisecond":
                cosTime = 31536000000 * howman
            elif Strwo2 == "week":
                cosTime = 52 * howman
            else:
                cosTime = howman
        elif Strwo1 == "month":
            if Strwo2 == "year":
                cosTime = (1.0 / 12) * howman
            elif Strwo2 == "day":
                cosTime = 30 * howman
            elif Strwo2 == "hour":
                cosTime = 720 * howman
            elif Strwo2 == "second":
                cosTime = 2592000 * howman
            elif Strwo2 == "millisecond":
                cosTime = 2592000000 * howman
            elif Strwo2 == "week":
                cosTime = (1.0 / 4) * howman
            else:
                cosTime = howman
        elif Strwo1 == "hour":
            if Strwo2 == "day":
                cosTime = (1.0 / 24) * howman
            elif Strwo2 == "year":
                cosTime = (1.0 / 8760) * howman
            elif Strwo2 == "month":
                cosTime = (1.0 / 720) * howman
            elif Strwo2 == "second":
                cosTime = 3600 * howman
            elif Strwo2 == "millisecond":
                cosTime = 3600000 * howman
            elif Strwo2 == "week":
                cosTime = (1.0 / 168) * howman
            else:
                cosTime = howman
        elif Strwo1 == "second":
            if Strwo2 == "day":
                cosTime = (1.0 / 86400) * howman
            elif Strwo2 == "year":
                cosTime = (1.0 / 31536000) * howman
            elif Strwo2 == "month":
                cosTime = (1.0 / 2592000) * howman
            elif Strwo2 == "hour":
                cosTime = (1.0 / 3600) * howman
            elif Strwo2 == "millisecond":
                cosTime = 1000 * howman
            elif Strwo2 == "week":
                cosTime = (1.0 / 604800) * howman
            else:
                cosTime = howman
        elif Strwo1 == "millisecond":
            if Strwo2 == "day":
                cosTime = (1.0 / 86400000) * howman
            elif Strwo2 == "year":
                cosTime = (1.0 / 31536000000) * howman
            elif Strwo2 == "month":
                cosTime = (1.0 / 2592000000) * howman
            elif Strwo2 == "hour":
                cosTime = (1.0 / 3600000) * howman
            elif Strwo2 == "second":
                cosTime = (1.0 / 1000) * howman
            elif Strwo2 == "week":
                cosTime = (1.0 / 604800000) * howman
            else:
                cosTime = howman
        elif Strwo1 == "week":
            if Strwo2 == "day":
                cosTime = 7 * howman
            elif Strwo2 == "year":
                cosTime = (1.0 / 52) * howman
            elif Strwo2 == "month":
                cosTime = (1.0 / 4) * howman
            elif Strwo2 == "hour":
                cosTime = 168 * howman
            elif Strwo2 == "second":
                cosTime = 604800 * howman
            elif Strwo2 == "millisecond":
                cosTime = 604800000 * howman
            else:
                cosTime = howman
        else:
            print("Invalid time unit entered.")
            return -1
        # If a known timeframe is provided
        if timecheckknown and HarTime == 0 and HarTime2 == 0:
            cosTime = KowHardTime
        elif not timecheckknown:  # If we don’t know the timeframe, calculate using difference
            cosTime = howman  # Ensure the time difference from input is used
        # Calculate final exponential growth
        fincomp1 = (Growth * 0.01) + 1
        fincomp2 = math.pow(fincomp1, cosTime)
        finisher = B * fincomp2
        print("Time: " + str(cosTime))
        print("Growth rate: " + str(fincomp1))
        print("Initial value: " + str(B))
        return finisher
    # End of compunding DEF
    # LOG missing value 
    @staticmethod
    def solveLog(base, exponent, result):
        # public static String solveLog(int base, int exponent, int result) {
        if base == -1:
            missingBase = math.pow(result, 1.0 / exponent)
            solution = "LOG?(%d) = %d \u2192 Base = %.2f" % (result, exponent, missingBase)
        elif exponent == -1:
            missingExponent = math.log(result) / math.log(base)
            solution = "LOG%d(%d) = __ \u2192 Exponent = %.2f" % (base, result, missingExponent)
        elif result == -1:
            missingResult = math.pow(base, exponent)
            solution = "LOG%d(?) = %d \u2192 Result = %.2f" % (base, exponent, missingResult)
        else:
            solution = "Invalid input. Please restart."
        return solution

if __name__ == '__main__':
    # public static void main(String []args) throws InterruptedException{
    player = JAVAFINALCH6COMP()
    # Scanner sc = new Scanner(System.in);
    # user info storage
    user = "Isssy"
    passkey = 123456
    WrongCount = 0
    Confirm = ""
    ChooserTEMP = 0
    cholms = 0
    CompQuit = False
    FuncQuit = False
    IsUser = False
    contTOmin = False
    print("welcome to NERVcalc")
    while IsUser == False:
        print("pleae enter passkey")
        print(">", end="")
        try:
            UserPass = int(input())
        except:
            UserPass = 0
        if UserPass == passkey:
            print("hello " + user)
            IsUser = True
        else:
            WrongCount += 1
            print("passkey enterd is inncorect, please try again\n" + "Trys left: " + str(abs(WrongCount - 3)))
        if WrongCount >= 3:
            Sleep = WrongCount
            Sleep *= 10
            print("mistake limit reached, please re-start machine and try again")
            print("must wait " + str(Sleep) + " Seconds")
            Sleep *= 1000
            time.sleep(Sleep / 1000.0)
    while CompQuit == False:
        FuncQuit = False
        Chooser = 0
        print("---------")
        print("please select Math Function below")
        print("(1)Logarithm")
        print("(2)Equation")
        print("(3)Exit NERVcalc")
        print("(4)Not Sure?")
        print(">", end="")
        try:
            Chooser = int(input())
        except:
            Chooser = 0
        if Chooser == 4:
            # seporators may need to be removed
            print("------")
            print("(1)Logirythim")
            print("simplify")
            print("missing value")
            print("LOG => EX")
            print("Finding 'X'")
            print("----")
            print("(2)Equastion")
            print("exponental model")
            print("Richer Scale")
            print("Compunding")
            print("---")
            print("(3)Exit NERVcalc")
            print("leave calculator")
            print(">", end="")
            try:
                ChooserTEMP = int(input())
            except:
                ChooserTEMP = 0
        elif Chooser == 3:
            print("Exit? Y/N")
            Confirm = input().lower()
            if Confirm == "y":
                print("Exiting File...")
                print(player.Exiter(""))
                CompQuit = True
        elif Chooser == 1:
            while FuncQuit == False:
                print("# logarythms")
                print("____")
                print("(1)Evaluate EX")
                print("(2)missing value")
                print("(3) LOG => EX")
                print("(4)Finding X")
                print("(5)Single Log")
                try:
                    LOGCHOO = int(input())
                except:
                    LOGCHOO = 0
                if LOGCHOO == 1:
                    print("What is the format of the problem?")
                    print("(1) log8(64)")
                    print("(2) log2(9^2)")
                    print("(3) log2(4) + log4(64)")
                    print("(4) ln(1)")
                    try:
                        choice = int(input())
                    except:
                        choice = 0
                    if choice == 1:
                        print("# log8(64)")
                        print("Enter base (e.g., 8): ")
                        try:
                            base = int(input())
                        except:
                            base = 0
                        print("Enter number (e.g., 64): ")
                        try:
                            num = int(input())
                        except:
                            num = 0
                        result = math.log(num) / math.log(base)
                        print("log8(64) = " + str(result))
                    elif choice == 2:
                        print("# log2(9^2)")
                        print("enter value inplace of '2'")
                        try:
                            log2 = int(input())
                        except:
                            log2 = 0
                        print("# log2(9)")
                        print("input number replaceing '9'")
                        try:
                            rep9 = float(input())
                        except:
                            rep9 = 0
                        print("# log2(9^2)")
                        print("enter value replaceing '^2'")
                        try:
                            powwow = float(input())
                        except:
                            powwow = 0
                        FS = (rep9 / log2)
                        FS *= powwow
                        print("final: " + str(FS))
                    elif choice == 3:
                        print("How many components?")
                        try:
                            NumComp = int(input())
                        except:
                            NumComp = 0
                        Bools = [False] * NumComp  # True for positive, false for negative
                        compHold = [False] * (NumComp - 1)  # True for +, False for -
                        PosHold = [0] * NumComp  # Stores positive logarithm results
                        NegHold = [0] * NumComp  # Stores negative logarithm results
                        NumOfPos = 0
                        NumOfNeg = 0
                        i = 0
                        while i < NumComp:
                            print("Is component " + str(i + 1) + " Positive or Negative? (+/-)")
                            sign = input()
                            if sign == "+":
                                NumOfPos += 1
                                Bools[i] = True
                                i += 1
                            elif sign == "-":
                                NumOfNeg += 1
                                Bools[i] = False
                                i += 1
                            else:
                                print("Invalid input, please enter + or -")
                        # Step 2: Compute Positive Logarithm Values
                        for i in range(NumOfPos):
                            print("# logA(B) + logC(D)")
                            print("Enter base A for logA(B): ")
                            try:
                                logA = int(input())
                            except:
                                logA = 0
                            print("Enter value B: ")
                            try:
                                valB = float(input())
                            except:
                                valB = 0
                            print("Enter base C for logC(D): ")
                            try:
                                logC = int(input())
                            except:
                                logC = 0
                            print("Enter value D: ")
                            try:
                                valD = float(input())
                            except:
                                valD = 0
                            log1 = math.log(valB) / math.log(logA)
                            log2 = math.log(valD) / math.log(logC)
                            result = log1 + log2  # Addition case
                            PosHold[i] = result
                            print("log" + str(logA) + "(" + str(valB) + ") = " + str(log1))
                            print("log" + str(logC) + "(" + str(valD) + ") = " + str(log2))
                            print("Final result: " + str(result))
                        # Step 3: Compute Negative Logarithm Values
                        for i in range(NumOfNeg):
                            print("# logA(B) - logC(D)")
                            print("Enter base A for logA(B): ")
                            try:
                                logA = int(input())
                            except:
                                logA = 0
                            print("Enter value B: ")
                            try:
                                valB = float(input())
                            except:
                                valB = 0
                            print("Enter base C for logC(D): ")
                            try:
                                logC = int(input())
                            except:
                                logC = 0
                            print("Enter value D: ")
                            try:
                                valD = float(input())
                            except:
                                valD = 0
                            log1 = math.log(valB) / math.log(logA)
                            log2 = math.log(valD) / math.log(logC)
                            result = log1 - log2  # Subtraction case
                            NegHold[i] = result
                            print("log" + str(logA) + "(" + str(valB) + ") = " + str(log1))
                            print("log" + str(logC) + "(" + str(valD) + ") = " + str(log2))
                            print("Final result: " + str(result))
                        finalPositiveSum = 0
                        finalNegativeSum = 0
                        for i in range(NumOfPos):
                            finalPositiveSum += PosHold[i]
                        for i in range(NumOfNeg):
                            finalNegativeSum += NegHold[i]
                        finalResult = finalPositiveSum - finalNegativeSum
                        print("_____________________")
                        print("Total Positive Sum: " + str(finalPositiveSum))
                        print("Total Negative Sum: " + str(finalNegativeSum))
                        print("Final Computed Result: " + str(finalResult))
                        print("_____________________")
                    elif choice == 4:
                        print("# ln(x)")
                        print("Enter a number for ln(x):")
                        try:
                            num = float(input())
                        except:
                            num = 0
                        if num <= 0:
                            print("Error: ln(x) is undefined for x <= 0.")
                        else:
                            result = math.log(num)
                            print("ln(" + str(num) + ") = " + str(result))
                    elif choice == 5:
                        pass
                    else:
                        print("Invalid choice.")
                elif LOGCHOO == 2:
                    print("________")
                    print("Select which value is missing:")
                    print("(1) LOG__ 64 = 3")
                    print("(2) LOG4 64 = __")
                    print("(3) LOG 4 __ = 3")
                    try:
                        choice = int(input())
                    except:
                        choice = 0
                    base = -1
                    exponent = -1
                    result = -1
                    if choice == 1:
                        print("(1) LOG__ 64 = 3")
                        print("Enter value in place of \"64\"")
                        try:
                            result = int(input())
                        except:
                            result = -1
                        print("(1) LOG__ 64 = 3")
                        print("Enter value in place for \"3\"")
                        try:
                            exponent = int(input())
                        except:
                            exponent = -1
                    elif choice == 2:
                        print("(2) LOG4 64 = __")
                        print("Enter value in place of \"4\"")
                        try:
                            base = int(input())
                        except:
                            base = -1
                        print("(2) LOG4 64 = __")
                        print("Enter value in place of \"64\"")
                        try:
                            result = int(input())
                        except:
                            result = -1
                    elif choice == 3:
                        print("(3) LOG 4 __ = 3")
                        print("Enter value in place of \"4\"")
                        try:
                            base = int(input())
                        except:
                            base = -1
                        print("(3) LOG 4 __ = 3")
                        print("Enter value in place of \"3\"")
                        try:
                            exponent = int(input())
                        except:
                            exponent = -1
                    else:
                        print("Invalid choice.")
                        exit(0)
                    print(JAVAFINALCH6COMP.solveLog(base, exponent, result))
                elif LOGCHOO == 3:
                    print("____")
                    print(">>what is the form of converstion?")
                    print(">(1)EX => LOG")
                    print(">(2)LOG => EX")
                    try:
                        confirmIN = int(input())
                    except:
                        confirmIN = 0
                    if confirmIN == 1:
                        print(">>pleae enter equastion: ")
                        print("= -> {}")
                        print("11\u00B2 = 121 (would be inputed as): 11^2{}121")
                        equastion = input()
                        print(player.LinTOlog(equastion, ""))
                    elif confirmIN == 2:
                        print(">>pleae enter equastion: ")
                        print("log2(8) = 3, inputed as: log2(8){}3")
                        equastion = input()
                        print(player.LogTOling(equastion, ""))
                elif LOGCHOO == 4:
                    print("function has not been added...")
                elif LOGCHOO == 5:
                    print("function has not been added")
                else:
                    print("input not recognized, Try again")
                print("continue?")
                Confirm = input().lower()
                if Confirm == "n":
                    print(player.Exiter(""))
                    FuncQuit = True
                    Chooser = 0
                else:
                    pass
        elif Chooser == 2:
            while FuncQuit == False:
                print("#Equastions")
                print("_____")
                print("(1)Exponental Model")
                print("(2)Richer Scale")
                print("(3)Compounding")
                try:
                    ChooserEQU = int(input())
                except:
                    ChooserEQU = 0
                print("_____")
                if ChooserEQU == 1:
                    print("Start value:")
                    try:
                        sv = int(input())
                    except:
                        sv = 0
                    print("Growth percentage (enter full number):")
                    print("if this is a Half Life problem enter \"0000\"")
                    try:
                        pcVal = int(input())
                    except:
                        pcVal = 0
                    print("Do you know the time frame? (Y/N)")
                    know = input().lower()
                    if know == "y":
                        print("Enter the timeframe:")
                        try:
                            HardCodeTF = int(input())
                        except:
                            HardCodeTF = 0
                        finalcomp3 = (pcVal * 0.01) + 1
                        finalcomp2 = math.pow(finalcomp3, HardCodeTF)
                        finalcomp1 = sv * finalcomp2
                        print(finalcomp1)
                    else:
                        print("Is the question based on:")
                        print("(1) Difference in time (e.g., 1990 -> 2020)")
                        print("(2) Growth over a period (e.g., grows X amount in 5 days, how much in 5 years)")
                        print("(3) HalfLife")
                        try:
                            confgrad = int(input())
                        except:
                            confgrad = 0
                        if confgrad == 1:
                            print("Enter two timeframes:")
                            print("Year 1: ", end="")
                            try:
                                yearone = int(input())
                            except:
                                yearone = 0
                            print("Year 2: ", end="")
                            try:
                                yeartwo = int(input())
                            except:
                                yeartwo = 0
                            print(player.evaluate(sv, pcVal, yearone, yeartwo, 1010, "", "", 0))
                        elif confgrad == 2:
                            print("Include two of the following time units: \"day\", \"year\", \"month\", \"hour\", \"second\", \"millisecond\", \"week\"")
                            print("(if there is only on time of measurement, put the same unit of measurement for both inputs)")
                            print("Timeframe one: ", end="")
                            tfONE = input().lower()
                            print("Timeframe two: ", end="")
                            tfTWO = input().lower()
                            print("How many times (e.g., how much will it grow in 5 years): ", end="")
                            try:
                                howm = int(input())
                            except:
                                howm = 0
                            print(player.evaluate(sv, pcVal, 0, 0, 1010, tfONE, tfTWO, howm))
                        else:
                            print("Half-Life")
                            try:
                                HalfLife = int(input())
                            except:
                                HalfLife = 0
                            print("over how many years?")
                            try:
                                HLyears = int(input())
                            except:
                                HLyears = 0
                            HLTF3 = HLyears / HalfLife
                            HTLF2 = math.pow(0.5, HLTF3)
                            HLfinal = HTLF2 * sv
                            print("Final Remains:  " + str(HLfinal))
                            print("Final loss:  " + str(abs(sv - HLfinal)))
                elif ChooserEQU == 2:
                    print("Input magnitude: ")
                    try:
                        MAG = float(input())
                    except:
                        MAG = 0.0
                    print("Calculating...")
                    time.sleep(2)
                    print(player.RicherScaleEN(MAG, ""))
                elif ChooserEQU == 3:
                    print("If a value is missing, input: \"m\"")
                    print("What is the beginning value?")
                    beginVal = input()
                    beginValINT = -1
                    if beginVal != "m":
                        try:
                            beginValINT = float(beginVal)
                        except:
                            beginValINT = -1
                    print("What is the interest rate (enter as full number, e.g., 7.5 for 7.5%)?")
                    intRate = input()
                    IntrestRte = -1
                    if intRate != "m":
                        try:
                            IntrestRte = float(intRate)
                        except:
                            IntrestRte = -1
                    print("What is the time period?")
                    TimePersus = input()
                    TimePer = -1
                    if TimePersus != "m":
                        try:
                            TimePer = int(TimePersus)
                        except:
                            TimePer = -1
                    print("What is the number of iterations?")
                    its = input()
                    itteration = -1
                    if its != "m":
                        try:
                            itteration = float(its)
                        except:
                            itteration = -1
                    print("What is the total output?")
                    outp = input()
                    Total = -1
                    if outp != "m":
                        try:
                            Total = float(outp)
                        except:
                            Total = -1
                    if beginVal == "m":
                        print(player.CompoundIntrestSV("", 0, IntrestRte, TimePer, itteration, Total))
                    elif intRate == "m":
                        print(player.CompoundIntrestIR("", beginValINT, 0, TimePer, itteration, Total))
                    elif TimePersus == "m":
                        print(player.CompoundIntrestTP("", beginValINT, IntrestRte, 0, itteration, Total))
                    elif its == "m":
                        print(player.CompoundIntrestIV("", beginValINT, IntrestRte, TimePer, 0, Total, ""))
                    elif outp == "m":
                        print(player.CompoundIntrestFV("", beginValINT, IntrestRte, TimePer, itteration, 0))
                        print("Error in input. Please check values and try again.")
                print("continue?")
                Confirm = input().lower()
                if Confirm == "n":
                    print(player.Exiter(""))
                    FuncQuit = True
                    Chooser = 0
            # End of while(FuncQuit == false)
        print("continue?")
        Confirm = input().lower()
        if Confirm == "n":
            print(player.Exiter(""))
            CompQuit = True
    # sc.close();
    print("Final los")
    
