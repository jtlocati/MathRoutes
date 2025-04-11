//Algabra Quizz on fractions and simplification
package NOTEV.JAV;

import java.util.Scanner;

public class NoteSpaceAlg3 {
public static void main(String[] args) throws InterruptedException {
    NoteSpaceAlg3 player = new NoteSpaceAlg3();
    Scanner sc = new Scanner(System.in);
    boolean ContFunc = true;
    boolean IsUserPly = true;
    String seperator = "................................";
    while(ContFunc == true && IsUserPly == true){
        System.out.println("alg factoring Quiz 1");
        System.out.println("(1)3/x-5");
        System.out.println("(2)X-4/x(2)x-8");
        System.out.println("(3)3/x+7/3x-12/2x-8");
        System.out.println("(4)x(2)-2x-48/x(2)+10+24");
        System.out.println("(5)2x+1/2-x+x-3/x+1");
        System.out.println("(8)x/x+4-x+36/x^(2)-16");
        System.out.println("(9)x+2/x(2)-4/x/x-2");
        System.out.println("(10)x/x(2)-9/x-3/x");
        System.out.println("(6)Force Flood");
        System.out.println("(7)Force Quit");
        System.out.print(">");        int chooser = sc.nextInt();
        if(chooser == 7){
            System.out.println("QUITTING....");
            Thread.sleep(200);
            for(int i = 0; i < 30; i++){
                System.out.println(" ");
            }
            System.out.println("____________________");
            IsUserPly = false;
                ContFunc = false;
        }
        else if(chooser == 6){
            System.out.println("IMPORTANT:\n to retun back to NERVcalc enter passkey\n there will be no prompt");
            Thread.sleep(4000);
            for (int i = 0; i < 20; i++){
                int Scabies = (int) (Math.random() * 5) + 0;
                if(Scabies == 1){
                    System.out.println("123/45\n" + seperator);
                    System.out.println("                           2.733");
                    System.out.println(seperator);
                }
                else if(Scabies == 2){
                    System.out.println("124+34\n" + seperator);
                    System.out.println("                            158");
                    System.out.println(seperator);
                }
                else if(Scabies == 3){
                    System.out.println("10 x 6 + 10\n" + seperator);
                    System.out.println("                            " + 10*6+10);
                    System.out.println(seperator);
                }
                else if(Scabies == 4){
                    System.out.println("12 + 67\n" + seperator);
                    System.out.println("                              " + (12 + 67));
                    System.out.println(seperator);
                }
                else if(Scabies == 5){
                    System.out.println("log(20)\n" + seperator);
                    System.out.println("                              1.3");
                    System.out.println(seperator);
                }
            }
            int cont = sc.nextInt();
            if(cont == 4922){
            System.out.println("USER IMP REC...");
            Thread.sleep(200);
            System.out.println("REDIRECTING...");
            Thread.sleep(2000);
            System.out.println("__________");
            }
            else{
                System.out.println("this aint it fam");
            }
        }
        else if (chooser == 1){
            System.out.println(seperator);
            System.out.println("X = 0 when do is undefined");
            System.out.println("x-5=0, x=5");
        }
        else if(chooser == 2){
            System.out.println(seperator);
            System.out.println("factor top & bottom");
            System.out.println("x-4 ->(x-2),\nBottom -(x-4)(x+2)");
            System.out.println("cancel out (2+x)");
            System.out.println("final: 4, -2");
            sc.nextInt();
        }
        else if(chooser == 3){
            System.out.println("simplify:\n3x-12 =>3(x-4)\n2x-8 => 2(x-4)");
            System.out.println("Exspression becomes:\n3/x+7/3(x-4)/2(x-4)\n=3/x+7*2(x-4)/3(x-4)");
            System.out.println("cancel out 3,(x-4)");
            System.out.println("Final: 2/x+7");
            sc.nextInt();
        }
        else if(chooser == 4){
            System.out.println("Factor:\n bottom(x+4),(x+6), \ntop(x+4)(x+6)");
            System.out.println("cancel(x+6)\nfinal:(x-8)/x+4");
        }
        else if(chooser == 5){
            System.out.println("make some shit up");
            System.out.println("final: \n3x^(2)-2+7/x^(2)-x-3");
            sc.nextInt();
        }
        else if(chooser==8){
            System.out.println("final:\nx-9/x-4");
            sc.nextInt();
        }
        else if(chooser==9){
            System.out.println("factor Bottom:\n(x-2),(x+2)");
            System.out.println("becomes:\nx+2/(x-2)(x+2)*x-2/x\nFinal: 1/x");
            sc.nextInt();
        }
        else if(chooser==10){
            System.out.println("somplifyy to: x/(x+3),(x-3)/x+3");
            System.out.println("cancel out x+3");
            System.out.println("becomes: x/x(3-x)\n final:1/x-3");
            sc.nextInt();
        }
    }
    sc.close();
}
}

