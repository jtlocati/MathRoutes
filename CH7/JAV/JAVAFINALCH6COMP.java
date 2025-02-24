package CH7.JAV;

/*TODO---
 * make outputs return below prompt line
 * change input types to be below prompt
 * change compounding intrest missing var to "A"
 * change prompts to be >= 31 chars
 * make a: "not sure" prompt on menu
 * show calculations function for ALL - (converstion)
 * Fix Exponental time converstion table IF it throws error on calculator or if words are too hard to type on calculator
 * manage HalfLIFE calling
 */
/*CheckList:
 * compunding--
 *      Def \/
 *      Calling
 * Richer Scale--
 *      Def\/
 *      Calling
 * Log convert--
 *      Def\/
 *      Calling
 *  Expononetal--
 *      Def
 *      Calling
 * EXIT REP IMPLICATION :(
 * Log Proof--
 *      Code
 *      Def
 *      Calling
 * Exponental--
 *      Def\/
 *      calling
 */
//Exit Rep DEF
import java.util.Scanner;
public class JAVAFINALCH6COMP {
public String Exiter(String ret) throws InterruptedException{
    String[] references = {
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
    };
    int randit = (int)(Math.random() * references.length) + 0;
    System.out.println(references[randit]);
    Thread.sleep(200);
    System.out.println(">>this ensures data is not tracable");
    for(int i = 0; i <= 4; i++){
        System.out.println("\rclosing UsrFile_" + (int)(Math.random() * 9999) + 0);
        Thread.sleep(500);
        System.out.print("\r");
    }
    ret = ("done!");
    return ret;
}
//Richer Scale DEF
    public String RicherScaleEN(double Magnitude, String ret) {
        double power = (Magnitude * (1.5));
        double power2u = (power + 11.8);

        // Extract integer and decimal parts 
        double power2uDIV = power2u - Math.floor(power2u); 
        double Econtaner = Math.pow(10, power2uDIV);
        Econtaner = Math.round(Econtaner * 100.0) / 100.0; // Round for display

        // Compute total energy
        double totalEnergy = Math.pow(10, power2u);

        // Print results
        System.out.println("> total Energy output (Uncompressed): " + totalEnergy);
        ret = ("> E ~ " + Econtaner + " x 10^" + (int)(power2u - power2uDIV));
        return ret;
    }
//Richer Scale DEF end------
//Compounding DEF--------
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
//end of Compound DEF
//LOG convert DEF
public String LogTOling(String equastion, String ret){
    String Bfind = "";
        String Yfind = "";
            String Xfind = equastion.substring(equastion.lastIndexOf("}")+1);
    int Bindex = equastion.indexOf("(");
        int Yindex = equastion.indexOf(")");
    if(Bindex > 0){
        Bfind = equastion.substring(3,Bindex);
    }else{ret = "error, try input again.";}
    if (Yindex > 0) {
        Yfind = equastion.substring(Bindex + 1, Yindex);
    }else{ret = "error, try input again.";}
    System.out.println("Y: " + Yfind);
    System.out.println("B: " + Bfind);
    System.out.println("X: " + Xfind);
    ret = ("final: " + Bfind + "^" + Xfind + " = " + Yfind);
    return ret;
}
public String LinTOlog(String equastion, String retLTL){
    //exsample equastion == 11^2 = 121
    String Bbreak = "";
        String Xbreak = "";
            String Ybreak = ""; 
    int Bindex = equastion.indexOf("^");
        int Xindex = equastion.indexOf("{");
            int Yindex = equastion.indexOf("}"); 
            Ybreak = equastion.substring(equastion.lastIndexOf("}")+1);
    if(Bindex > 0){
        Bbreak = equastion.substring(0, Bindex);
    }else{retLTL = "input error, try again (error message #1)";}
    if(Xindex > 0){
        Xbreak = equastion.substring(Bindex + 1, Xindex);
    }else{retLTL="input error, try again (error message #2)";}
    if(Yindex > 0 ){
    }else{retLTL="input error, try againe (error message #3)";}

    System.out.println("B: " + Bbreak);
    System.out.println("X: " + Xbreak);
    System.out.println("Y: " + Ybreak);
    retLTL = ("final: LOG" + Bbreak + "(" + Ybreak + ") = " + Xbreak);
    return retLTL;
}
//End of LOG convert DEF
//Exponental DEF
public double evaluate(int B, int Growth, int HarTime, int HarTime2, int KowHardTime, String wordtime2, String wordtime22, int howman) {
    double cosTime = 0;
    boolean timecheckword = !wordtime2.isEmpty();
    boolean timecheckknown = KowHardTime != 1010; // Ensure time frame is correctly checked

    String[] optio = {"day", "year", "month", "hour", "second", "millisecond", "week"}; 
    String Strwo1 = "", Strwo2 = "";

    // Match input time unit with predefined list
    for (String option : optio) {
        if (wordtime2.equals(option)) {
            Strwo1 = option;
            break;
        }
    }

    for (String option : optio) {
        if (wordtime22.equals(option)) {
            Strwo2 = option;
            break;
        }
    }

    // Time converstion Table:
    if (Strwo1.equals("day")) {
        if (Strwo2.equals("year")) cosTime = 365 * howman;
        else if (Strwo2.equals("month")) cosTime = 30 * howman;
        else if (Strwo2.equals("hour")) cosTime = 24 * howman;
        else if (Strwo2.equals("second")) cosTime = 86400 * howman;
        else if (Strwo2.equals("millisecond")) cosTime = 86400000 * howman;
        else if (Strwo2.equals("week")) cosTime = (1.0 / 7) * howman;
        else cosTime = howman; // Same unit
    } else if (Strwo1.equals("year")) {
        if (Strwo2.equals("day")) cosTime = (1.0 / 365) * howman;
        else if (Strwo2.equals("month")) cosTime = 12 * howman;
        else if (Strwo2.equals("hour")) cosTime = 8760 * howman;
        else if (Strwo2.equals("second")) cosTime = 31536000 * howman;
        else if (Strwo2.equals("millisecond")) cosTime = 31536000000L * howman;
        else if (Strwo2.equals("week")) cosTime = 52 * howman;
        else cosTime = howman;
    } else if (Strwo1.equals("month")) {
        if (Strwo2.equals("year")) cosTime = (1.0 / 12) * howman;
        else if (Strwo2.equals("day")) cosTime = 30 * howman;
        else if (Strwo2.equals("hour")) cosTime = 720 * howman;
        else if (Strwo2.equals("second")) cosTime = 2592000 * howman;
        else if (Strwo2.equals("millisecond")) cosTime = 2592000000L * howman;
        else if (Strwo2.equals("week")) cosTime = (1.0 / 4) * howman;
        else cosTime = howman;
    } else if (Strwo1.equals("hour")) {
        if (Strwo2.equals("day")) cosTime = (1.0 / 24) * howman;
        else if (Strwo2.equals("year")) cosTime = (1.0 / 8760) * howman;
        else if (Strwo2.equals("month")) cosTime = (1.0 / 720) * howman;
        else if (Strwo2.equals("second")) cosTime = 3600 * howman;
        else if (Strwo2.equals("millisecond")) cosTime = 3600000 * howman;
        else if (Strwo2.equals("week")) cosTime = (1.0 / 168) * howman;
        else cosTime = howman;
    } else if (Strwo1.equals("second")) {
        if (Strwo2.equals("day")) cosTime = (1.0 / 86400) * howman;
        else if (Strwo2.equals("year")) cosTime = (1.0 / 31536000) * howman;
        else if (Strwo2.equals("month")) cosTime = (1.0 / 2592000) * howman;
        else if (Strwo2.equals("hour")) cosTime = (1.0 / 3600) * howman;
        else if (Strwo2.equals("millisecond")) cosTime = 1000 * howman;
        else if (Strwo2.equals("week")) cosTime = (1.0 / 604800) * howman;
        else cosTime = howman;
    } else if (Strwo1.equals("millisecond")) {
        if (Strwo2.equals("day")) cosTime = (1.0 / 86400000) * howman;
        else if (Strwo2.equals("year")) cosTime = (1.0 / 31536000000L) * howman;
        else if (Strwo2.equals("month")) cosTime = (1.0 / 2592000000L) * howman;
        else if (Strwo2.equals("hour")) cosTime = (1.0 / 3600000) * howman;
        else if (Strwo2.equals("second")) cosTime = (1.0 / 1000) * howman;
        else if (Strwo2.equals("week")) cosTime = (1.0 / 604800000) * howman;
        else cosTime = howman;
    } else if (Strwo1.equals("week")) {
        if (Strwo2.equals("day")) cosTime = 7 * howman;
        else if (Strwo2.equals("year")) cosTime = (1.0 / 52) * howman;
        else if (Strwo2.equals("month")) cosTime = (1.0 / 4) * howman;
        else if (Strwo2.equals("hour")) cosTime = 168 * howman;
        else if (Strwo2.equals("second")) cosTime = 604800 * howman;
        else if (Strwo2.equals("millisecond")) cosTime = 604800000 * howman;
        else cosTime = howman;
    } else {
        System.out.println("Invalid time unit entered.");
        return -1;
    }


    // If a known timeframe is provided
    if (timecheckknown && HarTime == 0 && HarTime2 == 0) {
        cosTime = KowHardTime;
    } else if (!timecheckknown) {  // If we don’t know the timeframe, calculate using difference
        cosTime = howman;  // Ensure the time difference from input is used
    }

    // Calculate final exponential growth
    double fincomp1 = (Growth * 0.01) + 1;
    double fincomp2 = Math.pow(fincomp1, cosTime);
    double finisher = B * fincomp2;

    System.out.println("Time: " + cosTime);
    System.out.println("Growth rate: " + fincomp1);
    System.out.println("Initial value: " + B);

    return finisher;
}
//End of compunding DEF
//LOG missing value 
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
//End of LOG missing value DEF
//

    public static void main(String []args) throws InterruptedException{
        //initiations
        JAVAFINALCH6COMP player = new JAVAFINALCH6COMP();
        Scanner sc = new Scanner(System.in);
        //user info storage
        String user = "Isssy";
        int passkey = 123456;
        //Michalanious
        int WrongCount = 0;
        String Confirm;
        int ChooserTEMP = 0;
        int cholms = 0; 
        boolean CompQuit = false;
            boolean FuncQuit = false;
                boolean IsUser = false;
                    boolean contTOmin = false;
        System.out.println("welcome to NERVcalc");
        while (IsUser == false) {
            System.out.println("pleae enter passkey");
            System.out.print(">");
            int UserPass = sc.nextInt();
            if(UserPass == passkey){
                System.out.println("hello " + user);
                IsUser = true;
            }
            else {
                WrongCount++;
                System.out.println("passkey enterd is inncorect, please try again\n" + "Trys left: " +(Math.abs(WrongCount - 3)) );
            }
            if(WrongCount >= 3){
                int Sleep = WrongCount;
                Sleep *= 10;
                System.out.println("mistake limit reached, please re-start machine and try again");
                System.out.println("must wait " + (Sleep) + " Seconds");
                Sleep *= 1000;
                Thread.sleep(Sleep);
            }
        }
        while(CompQuit == false){
            FuncQuit = false;
            int Chooser = 0;
            System.out.println("---------\nplease select Math Function below");
            System.out.println("(1)Logarithm");
            System.out.println("(2)Equation");
            System.out.println("(3)Exit NERVcalc");
            System.out.println("(4)Not Sure?");
            System.out.println("(6)NOTES");
            System.out.print(">");
             Chooser = sc.nextInt();
            if(Chooser == 4){
                //seporators may need to be removed
                System.out.println("------");
                System.out.println("(1)Logirythim");
                System.out.println("simplify");
                System.out.println("missing value");
                System.out.println("LOG => EX");
                System.out.println("Finding 'X'");
                System.out.println("----");
                System.out.println("(2)Equastion");
                System.out.println("exponental model");
                System.out.println("Richer Scale");
                System.out.println("Compunding");
                System.out.println("---");
                System.out.println("(3)Exit NERVcalc");
                System.out.println("leave calculator");
                System.out.print(">");
                 ChooserTEMP = sc.nextInt();
            }
            else if(Chooser == 6){
                System.out.println(user.toUpperCase() + " Notes");
                System.out.println("");
            }
            else if(Chooser == 3){
                System.out.println("Exit? Y/N");
                 Confirm = sc.next().toLowerCase();
                if(Confirm.equals("y")){
                    System.out.println("Exiting File...");
                    System.out.println(player.Exiter(""));
                    CompQuit = true;
                }
            }
            else if(Chooser == 1){
            while(FuncQuit == false){
                System.out.println("# logarythms");
                System.out.println("____");
                System.out.println("(1)Evaluate EX");
                System.out.println("(2)missing value");
                System.out.println("(3) LOG => EX");
                System.out.println("(4)Finding X");
                System.out.println("(5)Single Log");
                int LOGCHOO = sc.nextInt();
                if (LOGCHOO==1) {
                    System.out.println("What is the format of the problem?");
                    System.out.println("(1) log8(64)");
                    System.out.println("(2) log2(9^2)");
                    System.out.println("(3) log2(4) + log4(64)");
                    System.out.println("(4) ln(1)");
                    
                    int choice = sc.nextInt();
            
                    if (choice == 1) {
                        System.out.println("# log8(64)");
                        System.out.println("Enter base (e.g., 8): ");
                        int base = sc.nextInt();
                        System.out.println("Enter number (e.g., 64): ");
                        int num = sc.nextInt();
            
                        // Correct logarithm calculation
                        double result = Math.log(num) / Math.log(base);
                        System.out.println("log8(64) = " + result);
                    } 
                    else if (choice == 2) {
                        System.out.println("# log2(9^2)");
                        System.out.println("enter value inplace of '2'");
                        int log2 = sc.nextInt();
                        System.out.println("# log2(9)");
                        System.out.println("input number replaceing '9'");
                        double rep9 = sc.nextDouble();
                        System.out.println("# log2(9^2)");
                        System.out.println("enter value replaceing '^2'");
                        double powwow = sc.nextInt();
                        double FS = (rep9/log2);
                        FS *= powwow;
                        System.out.println("final: " + FS);
                    } 
                    else if (choice == 3) {
                        double NH1 = 0, NH2 = 0, NH3 = 0, NH4 = 0;
                        double PH1 = 0, PH2 = 0, PH3 = 0, PH4 = 0;
                        
                        double[] NegHold = {NH1, NH2, NH3, NH4}; // Arguments (B) for log_A(B)
                        double[] PosHold = {PH1, PH2, PH3, PH4}; // Bases (A) for log_A(B)
                    
                        System.out.println("How many components?");
                        int NumComp = sc.nextInt();
                        
                        boolean[] Bools = new boolean[NumComp]; // True for addition, False for subtraction
                    
                        int posNEG = NumComp - 1;
                        for (int i = 0; i <= posNEG; i++) {
                            System.out.println("Adding or subtracting? (+/-)");
                            String posneg = sc.next();
                            Bools[i] = posneg.equals("+");
                        }
                    
                        for (int i = 0; i < NumComp; i++) { // Fix to avoid index errors
                            System.out.println("logA(B)");
                            System.out.print("Enter base 'A': ");
                            PosHold[i] = sc.nextDouble();
                            System.out.print("Enter argument 'B': ");
                            NegHold[i] = sc.nextDouble();
                        }
                    
                        // Compute logarithm results
                        double result = 0;
                        for (int i = 0; i < NumComp; i++) {
                            double logValue = Math.log(NegHold[i]) / Math.log(PosHold[i]); // log_A(B)
                            if (Bools[i]) {
                                result += logValue; // Addition
                            } else {
                                result -= logValue; // Subtraction
                            }
                        }
                    
                        // Display the final computed result
                        System.out.println("Final computed logarithm result: " + result);
                    }
                    
                    else if (choice == 4) {
                            System.out.println("# ln(x)");
                            System.out.println("Enter a number for ln(x):");
                            double num = sc.nextDouble();
                            if (num <= 0) {
                                System.out.println("Error: ln(x) is undefined for x <= 0.");
                            } else {
                                double result = Math.log(num);
                                System.out.println("ln(" + num + ") = " + result);
                            }
                        } 
                
                    else if(choice == 5){
                    }
                    else {
                        System.out.println("Invalid choice.");
                    }
                }
                else if(LOGCHOO == 2){
            System.out.println("________");
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

                }
                else if(LOGCHOO == 3){
                    System.out.println("____");
                    System.out.println(">>what is the form of converstion?");
                    System.out.println(">(1)EX => LOG");
                    System.out.println(">(2)LOG => EX");
                        int confirmIN = sc.nextInt();
                    if(confirmIN == 1){
                        System.out.println(">>pleae enter equastion: ");
                        System.out.println("= -> {}");
                        System.out.println( "11\u00B2 = 121 (would be inputed as): 11^2{}121");
                            String equastion = sc.next();
                        System.out.println(player.LinTOlog(equastion, ""));
                    }
                    else if(confirmIN == 2){
                        System.out.println(">>pleae enter equastion: ");
                        System.out.println("log2(8) = 3, inputed as: log2(8){}3");
                        String equastion = sc.next();
                        System.out.println(player.LogTOling(equastion, ""));
                    }
                }
                else if(LOGCHOO == 4){
                    System.out.println("function has not been added...");
                }
                else if(LOGCHOO == 5){
                    System.out.println("function has not been added");
                }
                else{System.out.println("input not recognized, Try again");}
                System.out.println("continue?");
                Confirm = sc.next().toLowerCase();
                if(Confirm.equals("n")){
                System.out.println(player.Exiter(""));
                FuncQuit = true;
                Chooser = 0;
                }
                else{}
            }
        }
        else if(Chooser ==2){
            while (FuncQuit == false) {
                System.out.println("#Equastions");
                System.out.println("_____");
                System.out.println("(1)Exponental Model");
                System.out.println("(2)Richer Scale");
                System.out.println("(3)Compounding");
                int ChooserEQU = sc.nextInt();
                System.out.println("_____");
                if(ChooserEQU == 1){
                    System.out.println("Start value:");
                    int sv = sc.nextInt();
        
                    System.out.println("Growth percentage (enter full number):");
                    System.out.println("if this is a Half Life problem enter \"0000\"" );
                    int pcVal = sc.nextInt();
        
                    System.out.println("Do you know the time frame? (Y/N)");
                    String know = sc.next().toLowerCase();
        
                    if (know.equals("y")) {
                        System.out.println("Enter the timeframe:");
                        int HardCodeTF = sc.nextInt();
                        double finalcomp3 = (pcVal * .01) + 1;
                            double finalcomp2 = Math.pow(finalcomp3, HardCodeTF);
                                double finalcomp1 = sv * finalcomp2;
                        System.out.println(finalcomp1);
                        //System.out.println(workerB.evaluate(sv, pcVal, 0, 0, HardCodeTF, "", "", 0));
                    } else {
                        System.out.println("Is the question based on:");
                        System.out.println("(1) Difference in time (e.g., 1990 -> 2020)");
                        System.out.println("(2) Growth over a period (e.g., grows X amount in 5 days, how much in 5 years)");
                        System.out.println("(3) HalfLife");
                        int confgrad = sc.nextInt();
        
                        if (confgrad == 1) {
                            System.out.println("Enter two timeframes:");
                            System.out.print("Year 1: ");
                            int yearone = sc.nextInt();
                            System.out.print("Year 2: ");
                            int yeartwo = sc.nextInt();
                            System.out.println(player.evaluate(sv, pcVal, yearone, yeartwo, 1010, "", "", 0));
                        } else if(confgrad == 2) {
                            System.out.println("Include two of the following time units: \"day\", \"year\", \"month\", \"hour\", \"second\", \"millisecond\", \"week\"");
                            System.out.println("(if there is only on time of measurement, put the same unit of measurement for both inputs)");
                            System.out.print("Timeframe one: ");
                            String tfONE = sc.next().toLowerCase();
                            System.out.print("Timeframe two: ");
                            String tfTWO = sc.next().toLowerCase();
                            System.out.print("How many times (e.g., how much will it grow in 5 years): ");
                            int howm = sc.nextInt();
        
                            System.out.println(player.evaluate(sv, pcVal, 0, 0, 1010, tfONE, tfTWO, howm));
                        }else{
                                System.out.println("Half-Life");
                                int HalfLife = sc.nextInt();
                                    System.out.println("over how many years?");
                                    int HLyears = sc.nextInt();
                            double HLTF3 = HLyears / HalfLife;
                                double HTLF2 = Math.pow(.5, HLTF3);
                                    double HLfinal = HTLF2 * sv;
                            System.out.println("Final Remains:  " + HLfinal);
                            System.out.println("Final loss:  " + (Math.abs(sv - HLfinal)));  
        
                        }
                    }
                } 
                else if(ChooserEQU ==2){
                    System.out.println("Input magnitude: ");
                    double MAG = sc.nextDouble(); 
        
                    System.out.println("Calculating...");
                    Thread.sleep(2000);
        
                    System.out.println(player.RicherScaleEN(MAG, ""));
                } 
                else if(ChooserEQU == 3){
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
                System.out.println(player.CompoundIntrestSV("", 0, IntrestRte, TimePer, itteration, Total));
            } else if (intRate.equals("m")) {
                System.out.println(player.CompoundIntrestIR("", beginValINT, 0, TimePer, itteration, Total));
            } else if (TimePersus.equals("m")) {
                System.out.println(player.CompoundIntrestTP("", beginValINT, IntrestRte, 0, itteration, Total));
            } else if (its.equals("m")) {
                System.out.println(player.CompoundIntrestIV("", beginValINT, IntrestRte, TimePer, 0, Total, ""));
            } else if (outp.equals("m")) {
                System.out.println(player.CompoundIntrestFV("", beginValINT, IntrestRte, TimePer, itteration, 0));
            } else {
                System.out.println("Error in input. Please check values and try again.");
            }
                }
                }
                System.out.println("continue?");
                Confirm = sc.next().toLowerCase();
                if(Confirm.equals("n")){
                System.out.println(player.Exiter(""));
                FuncQuit = true;
                Chooser = 0;
                }
            }
        }
        sc.close();
        }
    }