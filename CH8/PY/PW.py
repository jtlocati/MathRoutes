import time

class PieceWise:
    def SighnIn(self, voided):
        # Scanner sc = new Scanner(System.in);
        # Using input() for console input in Python
        IsUser = False
        users = ["Jet", "Izzy", "Wyatt"]
        passkey = [4922, 123456, 1234]
        Continuer = 0
        while IsUser == False:
            nigglet = False
            contCount = 0
            print("enter passkey:")
            print(">", end="")
            password = int(input())
            for i in range(len(users)):
                if passkey[i] == password:
                    print("hello: " + users[i])
                    IsUser = True
                    nigglet = True
                elif password != passkey[i] and nigglet == True:
                    print("wrong passkey")
                    contCount += 1
                    print("Attempts Reamining: " + str(abs(contCount - 3)))
                if contCount >= 3:
                    Continuer += 1
                    print("incorrect limit reached: \nmust wait: " + str(contCount * 10 * (Continuer)) + " Seconds ")
                    time.sleep(contCount * Continuer)
        voided = ""
        return voided

    def RunneR(self, leng, doubles, SQRT):
        for i in range(leng):
            if doubles[i] == True:
                pass
        voider = ""
        return voider

if __name__ == '__main__':
    # Scanner sc = new Scanner(System.in);
    # Using input() for console input in Python
    Player = PieceWise()
    print(Player.SighnIn(""))
    print("How many parameters?\ni.e: x<=4")
    print(">", end="")
    parameters = int(input())
    doubles = [False] * parameters
    LSDval = [0] * len(doubles)
    RSDval = [0] * len(doubles)
    for i in range(parameters):
        print("does parameter " + str(i+1) + " flloow the format of:\n(1)x(</>)//#\n(2)# (>/<) X (</>) #")
        doubless = int(input())
        if doubless == 1:
            doubles[i] = True
        else:
            doubles[i] = False
    for i in range(len(doubles)):
        if doubles[i] == True:
            print("Parameter" + str(i+1) + "what is the value for:\n _ (</>) X (</>) #")
            LSDval[i] = int(input())
            print("Parameter " + str(i+1) + "what is the value for:\n # (</>) X (</>) _")
            print(">", end="")
            RSDval[i] = int(input())
    print("does the equastion contain contain an x^2")
    print(">", end="")
    YEEEESSSS = input().lower()
    isSQRT = False
    if YEEEESSSS == "y":
        isSQRT = True