package CH7.JAV;
import java.util.Scanner;

public class logarythems {

    // Function to solve for missing logarithm components
    public static String solveLog(int base, int exponent, int result) {
        String solution;

        // Case 1: Missing base (LOG__ 64 = 3)
        if (base == -1) {
            double missingBase = Math.pow(result, 1.0 / exponent);
            solution = String.format("LOG?(%d) = %d → Base = %.2f", result, exponent, missingBase);
        }
        // Case 2: Missing exponent (LOG4 64 = __)
        else if (exponent == -1) {
            double missingExponent = Math.log(result) / Math.log(base);
            solution = String.format("LOG%d(%d) = __ → Exponent = %.2f", base, result, missingExponent);
        }
        // Case 3: Missing result (LOG 4 __ = 3)
        else if (result == -1) {
            double missingResult = Math.pow(base, exponent);
            solution = String.format("LOG%d(?) = %d → Result = %.2f", base, exponent, missingResult);
        }
        else {
            solution = "Invalid input. Please restart.";
        }

        return solution;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.println("Select which value is missing:");
        System.out.println("(1) LOG__ 64 = 3");
        System.out.println("(2) LOG4 64 = __");
        System.out.println("(3) LOG 4 __ = 3");
        int choice = sc.nextInt();

        int base = -1, exponent = -1, result = -1;

        switch (choice) {
            case 1: // Missing base
                System.out.println("(1) LOG__ 64 = 3");
                System.out.println("Enter value in place of \"64\"");
                result = sc.nextInt();
                System.out.println("(1) LOG__ 64 = 3");
                System.out.println("Enter value in place for \"3\"");
                exponent = sc.nextInt();
                break;
            case 2: // Missing exponent
                System.out.println("(2) LOG4 64 = __");
                System.out.println("Enter value in place of \"4\"");
                base = sc.nextInt();
                System.out.println("(2) LOG4 64 = __");
                System.out.println("Enter value in place of \"64\"");
                result = sc.nextInt();
                break;
            case 3: // Missing result
                System.out.println("(3) LOG 4 __ = 3");
                System.out.println("Enter value in place of \"4\"");
                base = sc.nextInt();
                System.out.println("(3) LOG 4 __ = 3");
                System.out.println("Enter value in place of \"3\"");
                exponent = sc.nextInt();
                break;
            default:
                System.out.println("Invalid choice.");
                sc.close();
                return;
        }

        // Compute and display result
        System.out.println(solveLog(base, exponent, result));

        sc.close();
    }
}
