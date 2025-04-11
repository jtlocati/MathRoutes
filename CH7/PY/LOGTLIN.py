import sys

class LogLinForm:
    def LogTOling(self, equastion, ret):
        # Initialize variables
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
            Yfind = equastion[Bindex+1:Yindex]
        else:
            ret = "error, try input again."
        print("Y: " + Yfind)
        print("B: " + Bfind)
        print("X: " + Xfind)
        ret = ("final: " + Bfind + "^" + Xfind + " = " + Yfind)
        return ret

    def LinTOlog(self, equastion, ret):
        #exsample equastion == 11^2 = 121
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
            ret = "input error, try again (error message #1)"
        if Xindex > 0:
            Xbreak = equastion[Bindex+1:Xindex]
        else:
            ret = "input error, try again (error message #2)"
        if Yindex > 0:
            pass
        else:
            ret = "input error, try againe (error message #3)"

        print("B: " + Bbreak)
        print("X: " + Xbreak)
        print("Y: " + Ybreak)
        ret = ("final: LOG" + Bbreak + "(" + Ybreak + ") = " + Xbreak)
        return ret

if __name__ == '__main__':
    # Simulate Scanner sc = new Scanner(System.in);
    player = LogLinForm()
    print("continue with equastion converstion? Y/N")
    confirm = input().lower()
    if confirm == "y":
        print(">>what is the form of converstion?")
        print(">(1)EX => LOG")
        print(">(2)LOG => EX")
        try:
            confirmIN = int(input())
        except ValueError:
            print("Invalid input. Exiting.")
            sys.exit(1)
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
    # No explicit re