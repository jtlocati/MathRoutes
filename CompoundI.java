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
    //finds valur for timeframe (T)
    public String CompoundIntrestTP(String finret, double Begin, double intrate, int timepr, double itera, double total){
        intrate *= .01;
        double TPcomp1 = (intrate / itera);
            TPcomp1 += 1;
            double TPcomp2 = (total / Begin);
        double TPstep21 = (Math.log(TPcomp1));
            double TPstep22 = (Math.log(TPcomp2));
        double TPstep3 = (TPstep22/TPstep21);
        TPstep3 /= itera;
        finret = ("The final time frame is: " + TPstep3);
        return finret;
    }
    //finds value for starting value  (P)
    public String CompoundIntrestSV(String finret, double Begin, double intrate, int timepr, double itera, double total){
        intrate *= .01;
        double DomCom1 = (intrate / itera ) + 1;
            double DomExe = (itera * timepr);
                double findomcom = (Math.pow(DomCom1, DomExe));
        double retfin = (total / findomcom);
        finret = ("final inital value is: " + retfin);
        return finret;
    }
    // Solves for total output (A)
    public String CompoundIntrestFV(String finret, double Begin, double intrate, int timepr, double itera, double total){
        intrate *= .01;
        double Expon = (itera * timepr);
            double parathe = (intrate / itera) + 1;
                double parathefin = (Math.pow(parathe, Expon));
        double finnig = (parathefin * Begin);
        finret = ("final output (A) is: " + finnig);
        return finret;
    }
    //solveing for (R)
    public String CompoundIntrestIR(String finret, double Begin, double intrate, int timepr, double itera, double total){
        intrate *= .01;
        double insidesqrt = (total / Begin);
            double outSideSqurt = (itera * timepr);
        double MstInPar = (Math.pow(insidesqrt, 1.0 / outSideSqurt));
        double mstEquation = ((MstInPar - 1) * itera);
        finret = ("the final rate is: " + mstEquation);
        return finret;

    }
    //finds value for # of itterations (N)
    public String CompoundIntrestIV(String finret, double Begin, double intrate, int timepr, double itera, double total, String IholderGen){
        boolean itfound = false;
        String finRetFon = "";
        String[] valholdStr = {"Yearly", "Quartarly", "monthly"};
            int[] valholdInt = {1, 4, 12};
            for( int i = 0; i < valholdStr.length; i++){
                double insidePar = ((intrate / i) + 1 );
                    double forSol = (Math.pow(insidePar, valholdInt[i]));
                if(forSol == total + total*.05 || forSol == total - total*.05){
                    finRetFon = ("itteration found at: " + valholdInt[i] + " or: " + valholdStr[i]);
                    itfound = true;
                    break;
                }
                else{
                    System.out.println("cannot determine...." + i);
                }
            }
                if (itfound == true){
                    finret = ("itteration found: " + finRetFon);
                }
                else{
                    finret = ("itterate cannot be found, closest itteration: " + valholdInt[0]);
                }
                return finret;
        // following code is optimal but buggy ---
        /*intrate *= .01;
        double Iholder = 0;
                boolean IGenTru = false;
                for (int i = 0; i < total; i++){
                    double parathe = ((intrate / i) + 1);   
                        double temp = (i * itera);
                            double tempPlaya = (Math.pow(parathe, temp));
                    if(tempPlaya == total + total*.05 || tempPlaya == total - total*.05){
                        Iholder = i;
                        break;
                    }
                    else{
                        System.out.println("no equastion found\n" + i);
                    }
                }
                if (Iholder == 1){
                    IholderGen = "Yearly";
                    IGenTru = true;  
                }
                else if(Iholder == 4){
                    IholderGen = "quartarly";
                    IGenTru = true;
                }
                else if(Iholder == 12){
                    IholderGen = "monthly";
                    IGenTru = true;
                }

                if(IGenTru == true){
                    finret = ("the mising iteration count is " + Iholder + " or " + IholderGen);
                    return finret;
                }
                else{
                    finret = ("the mising iteration count is " + Iholder);
                    return finret;
                } */
            
    }


    public static void main (String [] args){
        String BVcheck;
        int beginValINT = -1;
            String IRcheck;
            int IntrestRte = -1;
                String TPcheck;
                int TimePer = -1;
                    String ITcheck;
                    int itteration = -1;
                        String TOTcheck;
                        int Total = -1; 
        Scanner sc = new Scanner(System.in);
            CompoundI workerB = new CompoundI();
        System.out.println("continue with Compounding intrests? Y/N");
        String confirm = sc.next().toLowerCase();
        if(confirm.equals("y")){
                System.out.println("if the value is missing input: \"m\"");
                System.out.println("what is the begining value?");
                String beginVal = sc.next().toLowerCase();
                try{
                    beginValINT = Integer.parseInt(beginVal);
                } catch(NumberFormatException e){
                    BVcheck = beginVal;
                }
                System.out.println("what is the interest rate (enter as full number)?");
                String intRate = sc.next().toLowerCase();
                try{
                    IntrestRte = Integer.parseInt(intRate);
                } catch(NumberFormatException e){
                    IRcheck = intRate;
                }

                System.out.println("what is the time period?");
                String TimePersus = sc.next().toLowerCase();
                try{
                    IntrestRte = Integer.parseInt(TimePersus);
                } catch(NumberFormatException e){
                    TPcheck = TimePersus;
                }
                //TODO add functionlaity to word input for itteration
                System.out.println("what is the number of itterations");
                //System.out.println("yearly, annualy, monthly");
                //System.out.println("(A) input as number");
                //System.out.println("(B) input word value");
                String its = sc.next().toLowerCase();
                try{
                    itteration = Integer.parseInt(its);
                }catch(NumberFormatException e){
                    ITcheck = its;
                }
                System.out.println("what is the total output");
                String outp = sc.next().toLowerCase();
                try{
                    Total = Integer.parseInt(outp);
                } catch(NumberFormatException e){
                    TOTcheck = outp;
                }
                if(beginVal.equals("m")){
                    System.out.println(workerB.CompoundIntrestSV("", 0, IntrestRte, TimePer, itteration, Total));
                }
                else if(intRate.equals("m")){
                    System.out.println(workerB.CompoundIntrestIR("", beginValINT, 0, TimePer, itteration, Total));
                }
                else if(TimePersus.equals("m")){
                    System.out.println(workerB.CompoundIntrestTP("", beginValINT, IntrestRte, 0, itteration, Total));
                }
                else if(its.equals("m")){
                    System.out.println(workerB.CompoundIntrestIV("", beginValINT, IntrestRte, TimePer, 0, Total, ""));
                }
                else if(outp.equals("m")){
                    System.out.println(workerB.CompoundIntrestFV("", beginValINT, IntrestRte, TimePer, itteration, 0));
                }
                else{
                    System.out.println("error when reciveing data, confirm inputs and try again");
                }

                }
            //REMINDER: CompoundIntrestIV contains one exstra parameter for the Stringed itteration list
        sc.close();
        }
    }

