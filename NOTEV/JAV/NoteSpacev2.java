package NOTEV.JAV;
import java.util.Scanner;
public class NoteSpacev2{
public static void main(String[]args) throws InterruptedException{
    String seperator = "................................";
    int LocalChooser = 0;
    Scanner sc = new Scanner(System.in);
    boolean ContNotes = true;
        boolean ContFunc = true;
            boolean IsUser = false;
    String[] Users = {"Jet", "izzy", "wyatt"};
    int[] PassKey = {4922, 123456, 909772,};
    int AttLef = 0;
    int ContGate = 0;
    int TotWongTac = 0;
    int Chooser2 =0;
    //user login
    while (IsUser == false){
        System.out.println("Please enter Passkey:");
        System.out.print(">");
        int Password = sc.nextInt();
        for(int i = 0; i < Users.length; i++){
            int DictatorPASS = PassKey[i];
            if(DictatorPASS == Password){
                System.out.println("______");
                System.out.println("USER => " + Users[i]);
                System.out.println("Hello " + Users[i] + " Welcome to NERVcalc");
                IsUser = true;
            }
            ContGate++;
            if (DictatorPASS != Password && ContGate >= Users.length){
                 AttLef++;
                 System.out.println("______");
                 System.out.println("inccorect password:\nattemps left " + (Math.abs(AttLef-3)) );
                 System.out.println("______");
                 ContGate = 0;
            }
            if(AttLef >= 3){
                TotWongTac++;
                System.out.println("______");
                System.out.println("Password limit reached:\n must wait " + (AttLef * 5 * TotWongTac) + " seconds");
                System.out.println("______");
                Thread.sleep(AttLef*5000*TotWongTac);
                AttLef = 0;
            }
        }

    }
    while(ContFunc == true && IsUser == true){
        System.out.println("______");
        System.out.println("ALG TEST 1");
        System.out.println("(1)3x+5, if x <= -2\n-2x-7, if x>-2"); // two lines
        System.out.println("(2)x-1, if x<=-2\n~2x-1, if -2 < x <=4\n~-3x+8, if x>4");//three lines
        System.out.println("(6)Force Flood");
        System.out.println("(7)Force Quit");
        System.out.println("(8)see more");
        System.out.print(">");        int chooser = sc.nextInt();
        if(chooser == 8){
            System.out.println(seperator);
            System.out.println("(3)peicewise graph");
            System.out.println("(4)use f/g(x) to solve");
            System.out.println("(5)use f/g/h to solve");
            System.out.println("(9)inverse: f(x)=-2x-5");
            System.out.println("(10)inverse: f(x)=x/3+10");
            System.out.println("(11)inverse?: f(x)=1/x-2\n~g(x)=1/x+2");//two lines
            System.out.println("(12)BONUS");
            System.out.println("(6)Force Flood");
            System.out.println("(7)Force Quit");
            System.out.print(">");   Chooser2 = sc.nextInt();
        }
        else if(chooser == 7 || Chooser2 == 7){
            System.out.println("QUITTING....");
            Thread.sleep(200);
            for(int i = 0; i < 30; i++){
                System.out.println(" ");
            }
            System.out.println("____________________");
            IsUser = false;
                ContFunc = false;
        }
        else if(chooser == 6 || Chooser2 == 6){
            System.out.println("IMPORTANT:\n to retun back to NERVcalc enter passkey\n there will be no prompt");
            Thread.sleep(4000);
            for (int i = 0; i < 20; i++){
                int Scabies = (int) (Math.random() * 5) + 0;
                if(Scabies == 1){
                    System.out.println("log(5)\n"+seperator);
                    System.out.println("          "+Math.log(5));
                }
                else if(Scabies == 2){
                    System.out.println("ln(5)\n"+seperator);
                    System.out.println("            "+ Math.log(5));
                }
                else if(Scabies == 3){
                    System.out.println("10 x 6 + 10\n"+seperator);
                    System.out.println("            "+10*6+10);
                }
                else if(Scabies == 4){
                    System.out.println("12 + 67\n"+seperator);
                    System.out.println("            "+12 + 67);
                }
                else if(Scabies == 5){
                    System.out.println("log(20)\n"+seperator);
                    System.out.println("            "+Math.log(20));
                }
            }
            sc.nextInt();
            System.out.println("USER IMP REC...");
            Thread.sleep(200);
            System.out.println("REDIRECTING...");
            Thread.sleep(2000);
            System.out.println("__________");
        }
        else if (chooser == 1 || Chooser2 == 1){
            System.out.println("~forx<=-2 use 3x+5");
            System.out.println("~at-2 f(-2)=-6+5=-1");
            System.out.println("~graph (-2,-1) closed ->");
            System.out.println("(1)next:");
            LocalChooser =sc.nextInt();
            if(LocalChooser == 1){
                for(int i =0; i<9; i++){
                    System.out.println(" ");
                }
                System.out.println("for x>-2 use -2x-7");
                System.out.println("f(x)=4-7=-3");
                System.out.println("graph: -3 open ->");
            }
            sc.nextInt();
        }
        else if(chooser == 2 || Chooser2 == 2){
            System.out.println(seperator);
            System.out.println("7>4->f(x)=-3x+8");
            System.out.println("f(7=-3(7)+8=)\n-21+8=-13");
            System.out.println("final: -13");
            sc.nextInt();
        }
        else if(chooser == 3 || Chooser2 == 3){
            System.out.println(seperator);
            System.out.println("2, x<=4");
            System.out.println("x-2, 4<x<1");
            System.out.println("4x-6, x>=1");
            System.out.println("how? IDK make it look like your doing shit");
            sc.nextInt();
        }
        else if(chooser == 4 || Chooser2 == 4){
            System.out.println(seperator);
            System.out.println("______");
            System.out.println("sollve for: g(f(-3))");
            System.out.println("f(-3)=2(-3)+1=-6+1=-5");
            System.out.println("slove for: g(-5)");
            System.out.println("g(-5)=2(-5)-6=>\n-10-6=-16");
            System.out.println("final: -16");
            sc.nextInt();
        }
        else if(chooser == 5 || Chooser2 == 5){
            System.out.println(seperator);
            System.out.println("______");
            System.out.println("finding: g(f(x))");
            System.out.println("g(f(x))=g(9-x)=(9-x)^2+(9-x)");
            System.out.println("=81-18x+x^2+9-x");
            System.out.println("x^2-19x+90");
            System.out.println("final: x^2-19x+90");
            System.out.println("(1)see h(f(x))");
            LocalChooser = sc.nextInt();
            if(LocalChooser == 1){
                System.out.println("h(f(x)=(9-x)-2)");
                System.out.println("=7-x");
                sc.nextInt();
            }
            sc.nextInt();
        }
        else if(chooser==9 || Chooser2 == 9){
            System.out.println(seperator);
            System.out.println("y=2x-5");
            System.out.println("x=2y-5");
            System.out.println("x+5=2y");
            System.out.println("final: f-1(x)=x-5/2");
            sc.nextInt();
        }
        else if(chooser==10 || Chooser2 == 10){
            System.out.println(seperator);
            System.out.println("x=y/3");
            System.out.println("3*x-10=y/3*3");
            System.out.println("final: f-1(x)=3*x*10");
            sc.nextInt();
        }
        else if(chooser==11 || Chooser2 == 11){
            System.out.println(seperator);
            System.out.println("g(1.x - 2)=>(1/x-2)+2");
            System.out.println("1/(1/x) => x");
            System.out.println("second:");
            System.out.println("f(1/x-2 => x+2=x)");
            sc.nextInt();
        }
        else if(chooser == 12 || Chooser2 ==  12){
            System.out.println(seperator);
            System.out.println("The shop charges $130 for up to 1 hour.");
            System.out.println("$70 per additional hour after the first.");
            System.out.println("final: 130, 0<x<=1\n130+70(x-1), x>1");
            sc.nextInt();
        }
        }
        sc.close();
    }
}
