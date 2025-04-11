package CH8.JAV;

import java.util.Scanner;

import java.util.Arrays;
/*TODO:
* add a ">" to all user inputs
* add Seperators to classes 
* show work for all functions 
 */
public class FUNCTIONS2 {
    
    ///\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/
    //PROJECT VOIDED TILL FURTHER DEMAND
    //\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/

    /*//Function for adding arrays
    public String[] FUNCadd(int[]Fx, int[]Gx, int length) throws InterruptedException{
        Scanner sc = new Scanner(System.in);
    for(int i = 0; i<length;i++){
        int added = (Fx[i] + Gx[i]);
        String seperator = "";
        if(added > 0){
            seperator = "+";
        }
        System.out.print( seperator + added + "x^" + Math.abs(i-length) + " ");
    }
    System.out.println("show work?");
    String Chooser = sc.next().toLowerCase();
    if(Chooser.equals("y")){
        System.out.println("1- Identify property:");
        System.out.println("~(F+G)(x) => f(x)+G(x)");
        System.out.println("2- " + Arrays.toString(Fx) +" "+ Arrays.toString(Gx) + "\nadd like values" );
        System.out.println("final: ");
    }
    else{
        System.out.println("IGHT...");
        Thread.sleep(500);
    }
    String[] test = {";)"};
    sc.close();
    return test;
    }
    public String FUNCsub(int[]Fx, int[]Gx, int lenth )throws InterruptedException{
        Scanner sc = new Scanner(System.in);
        for(int i = 0; i<lenth;i++){
            int added = (Fx[i] - Gx[i]);
            String seperator = "";
            if(added > 0){
                seperator = "+";
            }
            System.out.print( seperator + " " + added + "x^" + Math.abs(i-lenth) + " ");
    }
    String voiding = "";

    return (voiding);
}
public String[] FUNCmult(int[] Fx, int[] Gx, int lent, int lentShor) {
    System.out.println("meow");
    int Expon = 0;
    int product = 0;
    String Seperator = "";
    //Multiplicatio V1.1
    /*for (int i = lent - 1; i >= 0; i--) {  // ✅ FIX: Start at lent-1 (last valid index)
        if (Fx[i] > 0 && Gx[i] > 0) {
            product = Fx[i] * Gx[i];
        }
        else if (Fx[i] == 0 && Gx[i] == 0) {
            if (Fx[i] == 0) {
                Fx[i] = 1;
            }
            else if (Gx[i] == 0) {
                Gx[i] = 1;
            }
            product = Fx[i] * Gx[i];
        }

        if (i == 0) {
            Expon = 1;
        } else {
            Expon = i + i; // ✅ FIX: Avoid incorrect exponent calculations
        }

        if (product < 0) {
            Seperator = "-";  // ✅ FIX: `i < 0` in the condition made no sense
        } 
        else if (product > 0) {
            Seperator = "+";
        }

        System.out.print(" " + Seperator + " " + product + "x^" + Expon + " ");
    }
    //Multiplication v1.2
    for(int i = lent; i > 0;i--){
        boolean Exponadd = true;
        if(Fx[i] == 0 || Gx[i]==0){
            if(Fx[i]==0){
                Fx[i] = 1;
            }
            else if(Gx[i]==0){
                Gx[i]=1;
            }
            Exponadd = false;
        }
        for(int j = lentShor; j > 0; j--){
            if(Exponadd == false){
                Expon = (i);
            } 
            else{Expon = (i+i);}
            product = (Gx[j]*Fx[i]);
            if(product < 0 && i<5){
                Seperator = "-";
            }
            else if(product > 0 && i<5){
                Seperator = "+";
            }
            else{Seperator = "";}
        }
        System.out.print(" " +  Seperator + product + "x^"+Expon + " ");
    }
    String[] voider = {""};
    return voider;
} */

    public String[] FUNCdiv(int[] Fx, int[] Gx, int lent, int lentSHOR){
        String[] teat = {" "};
        return teat;
    }
    public static void main(String[] args) throws InterruptedException{
        Scanner sc = new Scanner(System.in);
        boolean LOCK = false;
        int[] Passkey = {4922};
        String[] Users = {"Jet"}; 
        int collector = 0;
        int longWay = 0;
            int ShorWay = 0;
            //password protection w/ TBP
            //WAISTABLE:
            while (LOCK == false){
                System.out.println("enter passkey:");
                System.out.print(">");
                int pass = sc.nextInt();
                if(pass == Passkey[0]){
                    System.out.println("Hello " + Users[0]);
                    LOCK=true;
                }
                else{
                    collector++;
                    System.out.println("passkey inccorect " + (Math.abs(collector-3)) + "\nremain");
                    if(collector==3){
                        System.out.println("inccorect limit reached\nwait 30 seconds");
                        Thread.sleep(30000);
                        collector=0;
                    }
                }

            }
            //END OF WAISTABLE
            FUNCTIONS2 player = new FUNCTIONS2();
                String Seperator = "______";
        System.out.println("how long is F(x)?(exponent)");
        int FXleng = sc.nextInt();
        int[] FXhol = new int[FXleng];
        for(int i = 0; i<FXleng;i++){
        if(i==FXleng-1){
            System.out.println("what is the value connected to: x");
        }
        else{
            System.out.println("what is the value connected to: x^" + Math.abs(i-FXleng));
        }
        FXhol[i] = sc.nextInt();
        }
        System.out.println(Arrays.toString(FXhol));

        //Creates and assighns values to GX Holder for future functions

        int[] GXhol = new int[FXleng];

        //Gathers information for GXleng
        System.out.println("Entry for g(x)");
        int Gxleng = sc.nextInt();
        System.out.println("if the component does not exist enter '0'");
        System.out.println("REMINDER: if a varible is left as 'x^3' or x\ninput 1");
        for(int i = 0; i<FXleng; i++){
            System.out.println("what is the value connected to: x^"+Math.abs(i-FXleng));
            GXhol[i]=sc.nextInt();
        }
        System.out.println(Arrays.toString(GXhol));

        //improved ui for Calculators
        System.out.println("Choose the Function Type:");
        for(int i = 5; i > 0; i--){
            System.out.println("\rWait...." + i + " seconds");
            Thread.sleep(1000);
        }
        for(int i = 0; i <= 10; i++){
            System.out.println(" ");
        }
        if(FXleng < Gxleng){
            ShorWay = Gxleng;
            longWay = FXleng; 
        }
        else{
            ShorWay = FXleng;
            longWay = Gxleng;
        }
        //initeates selection
        System.out.println(Seperator);
        System.out.println("(1)(F+G)(x) BETA");
        System.out.println("(2)(F-G)(x) BETA");
        System.out.println("(3)(FG)(x) BETA");
        System.out.println("(4)(F/G)(x) BETA");
        int Chooser = sc.nextInt();
        System.out.println(Seperator);

        //Runs Chosen function
        /*if(Chooser==1){
            player.FUNCadd(FXhol, GXhol, FXleng);
            System.out.println(player);
        }
        else if(Chooser==2){
            System.out.println(player.FUNCsub(FXhol, GXhol, FXleng));
        }
        else if(Chooser == 3){
            System.out.println("ppp");
            System.out.println(player.FUNCmult(FXhol, GXhol, FXleng, ShorWay));
        }
        else if(Chooser == 4){
            System.out.println(player.FUNCdiv(FXhol, GXhol, longWay, ShorWay));
        }*/

        sc.close();
    }
}
