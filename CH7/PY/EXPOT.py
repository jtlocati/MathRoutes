import math

# package CH7.JAV;

class Exponental:

    def evaluate(self, B, Growth, HarTime, HarTime2, KowHardTime, wordtime2, wordtime22, howman):
        cosTime = 0.0
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

if __name__ == '__main__':
    sc = None  # Placeholder for scanner concept; using input() in Python
    workerB = Exponental()

    print("Continue with Exponential graph? (Y/N)")
    confirm = input().strip().lower()

    if confirm == "y":
        print("Start value:")
        sv = int(input())

        print("Growth percentage (enter full number):")
        print("if this is a Half Life problem enter \"0000\"")
        pcVal = int(input())

        print("Do you know the time frame? (Y/N)")
        know = input().strip().lower()

        if know == "y":
            print("Enter the timeframe:")
            HardCodeTF = int(input())
            finalcomp3 = (pcVal * 0.01) + 1
            finalcomp2 = math.pow(finalcomp3, HardCodeTF)
            finalcomp1 = sv * finalcomp2
            print(finalcomp1)
            # print(workerB.evaluate(sv, pcVal, 0, 0, HardCodeTF, "", "", 0))
        else:
            print("Is the question based on:")
            print("(1) Difference in time (e.g., 1990 -> 2020)")
            print("(2) Growth over a period (e.g., grows X amount in 5 days, how much in 5 years)")
            print("(3) HalfLife")
            confgrad = int(input())

            if confgrad == 1:
                print("Enter two timeframes:")
                print("Year 1: ", end="")
                yearone = int(input())
                print("Year 2: ", end="")
                yeartwo = int(input())
                print(workerB.evaluate(sv, pcVal, yearone, yeartwo, 1010, "", "", 0))
            elif confgrad == 2:
                print("Include two of the following time units: \"day\", \"year\", \"month\", \"hour\", \"second\", \"millisecond\", \"week\"")
                print("(if there is only on time of measurement, put the same unit of measurement for both inputs)")
                print("Timeframe one: ", end="")
                tfONE = input().strip().lower()
                print("Timeframe two: ", end="")
                tfTWO = input().strip().lower()
                print("How many times (e.g., how much will it grow in 5 years): ", end="")
                howm = int(input())
                print(workerB.evaluate(sv, pcVal, 0, 0, 1010, tfONE, tfTWO, howm))
            else:
                print("Half-Life")
                HalfLife = int(input())
                print("over how many years?")
                HLyears = int(input())
                HLTF3 = HLyears / HalfLife
                HTLF2 = math.pow(0.5, HLTF3)
                HLfinal = HTLF2 * sv
                print("Final Remains:  " + str(HLfinal))
                print("Final loss:  " + str(abs(sv - HLfinal)))
    # In Python, no need to close the scanner
