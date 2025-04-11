package CH8.JAV;

import java.util.Scanner;

public class FunctionsINV{
    public static void main(String [] args) throws InterruptedException{
        Scanner sc = new Scanner(System.in);
            FunctionsINV player = new FunctionsINV();
        String[] users = {"jet"};
            int[] passkey = {4922};
        boolean IsUser = false;
        int collector = 0;
        //user login
        while(IsUser == false){
            System.out.println("enter passkey");
                System.out.print(">" ); int passint = sc.nextInt();
            if(passint == passkey[0]){
                System.out.println("Hello " + users[0]);
                IsUser = true;
            }
            else{
                collector++;
                System.out.println(Math.abs(collector-3) + " attempts rememaining");
                if(collector >= 3){
                    System.out.println("must wait 30 seconds before next login attempt");
                    Thread.sleep(30000);
                }
            }
        }
        int GxLeng = 0 ;
            int FxLeng = 0;
        System.out.println("Welcome to NERVcalc");
        System.out.println("plese enter equastion type for component one");
        System.out.println("(1)polynomal: \n(2)single factor");
        System.out.print(">");int chooser = sc.nextInt();
        if(chooser == 1){
            System.out.println("how long is this polynomal?\n");
             FxLeng = sc.nextInt();
        }
        else{
            System.out.println("is the ");
        }


        sc.close();
    }
}