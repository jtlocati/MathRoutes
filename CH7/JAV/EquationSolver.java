package CH7.JAV;
import java.util.Scanner;
    public class EquationSolver {
        public String Expon(String equastion) {
            // 3^(2x+3) = 81^((x-2))
            double modRB = 0; // Initialize modRB
            
            // Finds right base
            String RightBase = equastion.substring(equastion.indexOf("=") + 1, equastion.indexOf("^", equastion.indexOf("="))).trim();
            System.out.println("Right Base: " + RightBase);
    
            // Finds left base
            String LeftBase = equastion.substring(0, equastion.indexOf("^")).trim();
            System.out.println("Left Base: " + LeftBase);
    
            // Finds left parentheses content
            int leftParStart = equastion.indexOf("^(") + 2; // Move past "^("
            int leftParEnd = equastion.indexOf(")", leftParStart);
            String LeftPar = equastion.substring(leftParStart, leftParEnd).trim();
    
            // Finds right parentheses content
            int rightParStart = equastion.indexOf("^((") + 3; // Move past "^(("
            int rightParEnd = equastion.indexOf("))", rightParStart);
            String RightPar = equastion.substring(rightParStart, rightParEnd).trim();
    
            System.out.println("Left Par: " + LeftPar);
            System.out.println("Right Par: " + RightPar);
    
            // Parse bases into double
            double RBINT = Double.parseDouble(RightBase);
            double LBINT = Double.parseDouble(LeftBase);
    
            // Convert LeftPar and RightPar to int safely
            int RPINT = safeParseInt(RightPar);
            int LPINT = safeParseInt(LeftPar);
    
            System.out.println("Parsed Parentheses Values: " + LPINT + " + " + RPINT + " = " + (LPINT + RPINT));
    
            // Loop to find the exponent conversion factor
            for (int i = 0; i < 10; i++) { // Safety limit to prevent infinite loops
                modRB = Math.pow(LBINT, i);
                if (modRB == RBINT) {
                    System.out.println("✅ Base Conversion Found: " + LBINT + "^" + i + " = " + RBINT);
                    break;
                }
            }
            
            return equastion;
        }
    
        // Helper function to safely parse integers from strings with validation
        public static int safeParseInt(String str) {
            try {
                return Integer.parseInt(str.replaceAll("[^0-9-]", "")); // Remove non-numeric characters
            } catch (NumberFormatException e) {
                System.out.println(" Warning: Could not parse '" + str + "' as an integer. Defaulting to 0.");
                return 0;
            }
        }
    
    public static void main(String[] args) {
        EquationSolver player = new EquationSolver();
        System.out.println(player.Expon("3^(2x+3)=81^(x-2)"));
    }
}
/*
 *         System.out.println("🔹 Enter an equation to solve for x.");
        System.out.println("💡 Input Format Examples:");
        System.out.println("  - Exponential:  3^(2x+3) = 81^(x-2)");
        System.out.println("  - Exponential with e:  (2e^x + 1)(e^x - 3) = 0");
        System.out.println("  - Logarithmic:  log(x) - 10 = 8");
        System.out.println("  - Natural Log:  ln(x) + 5 = 1");
        System.out.println("  - Linear:  2x + 5 = 9");
        System.out.print("\nEnter equation: ");
 */