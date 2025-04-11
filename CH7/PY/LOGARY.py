import math

class logarythems:
    # Function to solve for missing logarithm components
    @staticmethod
    def solveLog(base, exponent, result):
        solution = ""
        # Case 1: Missing base (LOG__ 64 = 3)
        if base == -1:
            missingBase = math.pow(result, 1.0 / exponent)
            solution = "LOG?({0}) = {1} \u2192 Base = {2:.2f}".format(result, exponent, missingBase)
        # Case 2: Missing exponent (LOG4 64 = __)
        elif exponent == -1:
            missingExponent = math.log(result) / math.log(base)
            solution = "LOG{0}({1}) = __ \u2192 Exponent = {2:.2f}".format(base, result, missingExponent)
        # Case 3: Missing result (LOG 4 __ = 3)
        elif result == -1:
            missingResult = math.pow(base, exponent)
            solution = "LOG{0}(?) = {1} \u2192 Result = {2:.2f}".format(base, exponent, missingResult)
        else:
            solution = "Invalid input. Please restart."
        return solution

    @staticmethod
    def main():
        # Create a scanner-like interface using input()
        print("Select which value is missing:")
        print("(1) LOG__ 64 = 3")
        print("(2) LOG4 64 = __")
        print("(3) LOG 4 __ = 3")
        choice = int(input())
        
        base = -1
        exponent = -1
        result = -1

        if choice == 1:  # Missing base
            print("(1) LOG__ 64 = 3")
            print("Enter value in place of \"64\"")
            result = int(input())
            print("(1) LOG__ 64 = 3")
            print("Enter value in place for \"3\"")
            exponent = int(input())
        elif choice == 2:  # Missing exponent
            print("(2) LOG4 64 = __")
            print("Enter value in place of \"4\"")
            base = int(input())
            print("(2) LOG4 64 = __")
            print("Enter value in place of \"64\"")
            result = int(input())
        elif choice == 3:  # Missing result
            print("(3) LOG 4 __ = 3")
            print("Enter value in place of \"4\"")
            base = int(input())
            print("(3) LOG 4 __ = 3")
            print("Enter value in place of \"3\"")
            exponent = int(input())
        else:
            print("Invalid choice.")
            return

        # Compute and display result
        print(logarythems.solveLog(base, exponent, result))

if __name__ == "__main__":
    logarythems