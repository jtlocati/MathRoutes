import java.util.Scanner;
public class CompoundI {
    /*Library:
     * finret = final return (NULL)
     * begin = begining # (P) \/
     * intrate = intrest rate (R) \/
     * timepr = time period (T) \/ 
     * itera = iterations / # of times (N) \/
     * total = total output (A) \/
     */

    // Finds value for timeframe (T)
    public String CompoundIntrestTP(String finret, double Begin, double intrate, int timepr, double itera, double total){
        intrate *= 0.01;
        double TPcomp1 = (intrate / itera) + 1;
        double TPcomp2 = (total / Begin);
        
        if (TPcomp1 <= 0 || TPcomp2 <= 0) {
            return "Error: Invalid input for logarithm.";
        }
        
        double TPstep21 = Math.log(TPcomp1);
        double TPstep22 = Math.log(TPcomp2);
        double TPstep3 = (TPstep22 / TPstep21) / itera;
        
        finret = "The final time frame is: " + TPstep3;
        return finret;
    }

    // Finds value for starting value (P)
    public String CompoundIntrestSV(String finret, double Begin, double intrate, int timepr, double itera, double total){
        intrate *= 0.01;
        double DomCom1 = (intrate / itera) + 1;
        double DomExe = (itera * timepr);
        double findomcom = Math.pow(DomCom1, DomExe);
        double retfin = (total / findomcom);

        finret = "Final initial value is: " + retfin;
        return finret;
    }

    // Solves for total output (A)
    public String CompoundIntrestFV(String finret, double Begin, double intrate, int timepr, double itera, double total){
        intrate *= 0.01;
        double Expon = (itera * timepr);
        double parathe = (intrate / itera) + 1;
        double parathefin = Math.pow(parathe, Expon);
        double finnig = (parathefin * Begin);

        finret = "Final output (A) is: " + finnig;
        return finret;
    }

    // Solving for interest rate (R)
    public String CompoundIntrestIR(String finret, double Begin, double intrate, int timepr, double itera, double total){
        if (Begin <= 0 || total <= 0 || timepr <= 0) {
            return "Error: Invalid inputs for interest rate calculation.";
        }
        
        double insidesqrt = (total / Begin);
        double outSideSqurt = (itera * timepr);
        double MstInPar = Math.pow(insidesqrt, 1.0 / outSideSqurt);
        double mstEquation = ((MstInPar - 1) * itera);

        finret = "The final rate is: " + (mstEquation * 100) + "%";
        return finret;
    }

    // Finds value for # of iterations (N)
    public String CompoundIntrestIV(String finret, double Begin, double intrate, int timepr, double itera, double total, String IholderGen){
        boolean itfound = false;
        String finRetFon = "";
        String[] valholdStr = {"Yearly", "Quarterly", "Monthly"};
        int[] valholdInt = {1, 4, 12};

        for (int i = 0; i < valholdStr.length; i++) {
            double insidePar = ((intrate / valholdInt[i]) + 1);
            double forSol = Math.pow(insidePar, (valholdInt[i] * timepr));

            if (Math.abs(forSol - total) <= total * 0.05) {  // Allow small margin of error
                finRetFon = "Iteration found at: " + valholdInt[i] + " or: " + valholdStr[i];
                itfound = true;
                break;
            }
        }

        if (itfound) {
            finret = "Iteration found: " + finRetFon;
        } else {
            finret = "Iteration cannot be found, closest iteration: " + valholdInt[0];
        }

        return finret;
    }

    public static void main (String[] args) {
        Scanner sc = new Scanner(System.in);
        CompoundI workerB = new CompoundI();
        
        System.out.println("Continue with Compound Interest calculations? Y/N");
        String confirm = sc.next().toLowerCase();

        if (confirm.equals("y")) {
            System.out.println("If a value is missing, input: \"m\"");

            System.out.println("What is the beginning value?");
            String beginVal = sc.next();
            double beginValINT = -1;
            if (!beginVal.equals("m")) {
                beginValINT = Double.parseDouble(beginVal);
            }

            System.out.println("What is the interest rate (enter as full number, e.g., 7.5 for 7.5%)?");
            String intRate = sc.next();
            double IntrestRte = -1;
            if (!intRate.equals("m")) {
                IntrestRte = Double.parseDouble(intRate);
            }

            System.out.println("What is the time period?");
            String TimePersus = sc.next();
            int TimePer = -1;
            if (!TimePersus.equals("m")) {
                TimePer = Integer.parseInt(TimePersus);
            }

            System.out.println("What is the number of iterations?");
            String its = sc.next();
            double itteration = -1;
            if (!its.equals("m")) {
                itteration = Double.parseDouble(its);
            }

            System.out.println("What is the total output?");
            String outp = sc.next();
            double Total = -1;
            if (!outp.equals("m")) {
                Total = Double.parseDouble(outp);
            }

            // Determine which calculation to perform
            if (beginVal.equals("m")) {
                System.out.println(workerB.CompoundIntrestSV("", 0, IntrestRte, TimePer, itteration, Total));
            } else if (intRate.equals("m")) {
                System.out.println(workerB.CompoundIntrestIR("", beginValINT, 0, TimePer, itteration, Total));
            } else if (TimePersus.equals("m")) {
                System.out.println(workerB.CompoundIntrestTP("", beginValINT, IntrestRte, 0, itteration, Total));
            } else if (its.equals("m")) {
                System.out.println(workerB.CompoundIntrestIV("", beginValINT, IntrestRte, TimePer, 0, Total, ""));
            } else if (outp.equals("m")) {
                System.out.println(workerB.CompoundIntrestFV("", beginValINT, IntrestRte, TimePer, itteration, 0));
            } else {
                System.out.println("Error in input. Please check values and try again.");
            }
        }

        sc.close();
    }
}
