package CH8.JAV;


import java.util.Scanner;
import java.util.ArrayList;
import java.util.Arrays;

public class PieceWise {
    public String SighnIn(String voided) throws InterruptedException{
        Scanner sc = new Scanner(System.in);
        boolean IsUser = false;
        String[] users = {"Jet", "Izzy", "Wyatt"};
            int[] passkey = {4922, 123456, 1234};
        int Continuer = 0;
        while(IsUser == false){
            boolean nigglet = false;
            int contCount = 0;
            System.out.println("enter passkey:");
                System.out.print(">"); int password = sc.nextInt();
            for(int i = 0; i < users.length;i++){
                if(passkey[i] == password){
                    System.out.println("hello: " + users[i]);
                    IsUser = true;
                    nigglet = true;
                }
                else if(password!=passkey[i] && nigglet == true){
                System.out.println("wrong passkey");
                contCount++;
                System.out.println("Attempts Reamining: " + (Math.abs(contCount-3)));
            }
            if(contCount>=3){
                Continuer++;
                System.out.println("incorrect limit reached: \nmust wait: " + (contCount*10*(Continuer)) + " Seconds ");
                Thread.sleep(contCount*Continuer*1000);
            }
            }
        }
        voided = "";
        return voided;
    }
    public String RunneR(int leng, boolean[] doubles, boolean[] SQRT){
        for(int i = 0; i<leng;i++){
            if(doubles[i]==true){

            }
        }


        String voider = "";
        return voider;
    }
    public static void main(String [] args) throws InterruptedException{
        Scanner sc = new Scanner(System.in);
            PieceWise Player = new PieceWise();
        System.out.println(Player.SighnIn(""));
        System.out.println("How many parameters?\ni.e: x<=4");
        System.out.print(">");  int parameters = sc.nextInt();
        boolean[] doubles = new boolean[parameters];
        int[] LSDval = new int[doubles.length];
            int[] RSDval = new int[doubles.length];

        for(int i = 0; i < parameters;i++){
            System.out.println("does parameter " + (i+1) + " flloow the format of:\n(1)x(</>)//#\n(2)# (>/<) X (</>) #");
            int doubless = sc.nextInt();
            if(doubless == 1){
                doubles[i] = true;
            }        
            else{
                doubles[i]=false;
            }
         }
         for(int i = 0; i< doubles.length; i++){
            if(doubles[i] == true){
                System.out.println("Parameter" + (i+1) + "what is the value for:\n _ (</>) X (</>) #");
                LSDval[i] = sc.nextInt();
                System.out.println("Parameter "+ (i+1) + "what is the value for:\n # (</>) X (</>) _");
                System.out.print(">");   RSDval[i]=sc.nextInt();
            }
         }
         System.out.println("does the equastion contain contain an x^2");
         System.out.print(">"); String YEEEESSSS = sc.next().toLowerCase();
         boolean isSQRT = false;
         if(YEEEESSSS.equals("y")){
            isSQRT = true;
         }

        }
    }
