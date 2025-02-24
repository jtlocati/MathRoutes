import math

class CompoundI:
    """Library:
     * finret = final return (NULL)
     * begin = begining # (P) \/
     * intrate = intrest rate (R) \/
     * timepr = time period (T) \/
     * itera = iterations / # of times (N) \/
     * total = total output (A) \/
     """

    # Finds value for timeframe (T)
    def CompoundIntrestTP(self, finret, Begin, intrate, timepr, itera, total):
        intrate *= 0.01
        TPcomp1 = (intrate / itera) + 1
        TPcomp2 = (total / Begin)
        
        if (TPcomp1 <= 0) or (TPcomp2 <= 0):
            return "Error: Invalid input for logarithm."
        
        TPstep21 = math.log(TPcomp1)
        TPstep22 = math.log(TPcomp2)
        TPstep3 = (TPstep22 / TPstep21) / itera
        
        finret = "The final time frame is: " + str(TPstep3)
        return finret

    # Finds value for starting value (P)
    def CompoundIntrestSV(self, finret, Begin, intrate, timepr, itera, total):
        intrate *= 0.01
        DomCom1 = (intrate / itera) + 1
        DomExe = (itera * timepr)
        findomcom = math.pow(DomCom1, DomExe)
        retfin = (total / findomcom)

        finret = "Final initial value is: " + str(retfin)
        return finret

    # Solves for total output (A)
    def CompoundIntrestFV(self, finret, Begin, intrate, timepr, itera, total):
        intrate *= 0.01
        Expon = (itera * timepr)
        parathe = (intrate / itera) + 1
        parathefin = math.pow(parathe, Expon)
        finnig = (parathefin * Begin)

        finret = "Final output (A) is: " + str(finnig)
        return finret

    # Solving for interest rate (R)
    def CompoundIntrestIR(self, finret, Begin, intrate, timepr, itera, total):
        if (Begin <= 0) or (total <= 0) or (timepr <= 0):
            return "Error: Invalid inputs for interest rate calculation."
        
        insidesqrt = (total / Begin)
        outSideSqurt = (itera * timepr)
        MstInPar = math.pow(insidesqrt, 1.0 / outSideSqurt)
        mstEquation = ((MstInPar - 1) * itera)
        
        finret = "The final rate is: " + str(mstEquation * 100) + "%"
        return finret

    # Finds value for # of iterations (N)
    def CompoundIntrestIV(self, finret, Begin, intrate, timepr, itera, total, IholderGen):
        itfound = False
        finRetFon = ""
        valholdStr = ["Yearly", "Quarterly", "Monthly"]
        valholdInt = [1, 4, 12]

        for i in range(len(valholdStr)):
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

def main():
    workerB = CompoundI()
    
    print("Continue with Compound Interest calculations? Y/N")
    confirm = input().lower()

    if confirm == "y":
        print("If a value is missing, input: \"m\"")

        print("What is the beginning value?")
        beginVal = input()
        beginValINT = -1
        if beginVal != "m":
            beginValINT = float(beginVal)

        print("What is the interest rate (enter as full number, e.g., 7.5 for 7.5%)?")
        intRate = input()
        IntrestRte = -1
        if intRate != "m":
            IntrestRte = float(intRate)

        print("What is the time period?")
        TimePersus = input()
        TimePer = -1
        if TimePersus != "m":
            TimePer = int(TimePersus)

        print("What is the number of iterations?")
        its = input()
        itteration = -1
        if its != "m":
            itteration = float(its)

        print("What is the total output?")
        outp = input()
        Total = -1
        if outp != "m":
            Total = float(outp)

        # Determine which calculation to perform
        if beginVal == "m":
            print(workerB.CompoundIntrestSV("", 0, IntrestRte, TimePer, itteration, Total))
        elif intRate == "m":
            print(workerB.CompoundIntrestIR("", beginValINT, 0, TimePer, itteration, Total))
        elif TimePersus == "m":
            print(workerB.CompoundIntrestTP("", beginValINT, IntrestRte, 0, itteration, Total))
        elif its == "m":
            print(workerB.CompoundIntrestIV("", beginValINT, IntrestRte, TimePer, 0, Total, ""))
        elif outp == "m":
            print(workerB.CompoundIntrestFV("", beginValINT, IntrestRte, TimePer, itteration, 0))
        else:
            print("Error in input. Please check values and try again.")

if __name__ == "__main__":
    main()
