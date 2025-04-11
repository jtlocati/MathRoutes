package NOTEV.JAV;

import java.util.Scanner;
public class NOTESv2{
public static void main(String[]args) throws InterruptedException{
    Scanner sc = new Scanner(System.in);
    boolean ContNotes = true;
        boolean ContFunc = true;
            boolean IsUser = false;
    String[] Users = {"Jet", "izzy", "wyatt"};
    int[] PassKey = {4922, 123456, 909772};
    int AttLef = 0;
    int ContGate = 0;
    int TotWongTac = 0;
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
        System.out.println("(1)PecieWise");
        System.out.println("(2)-3e^(7x+9) + 6 = -6");
        System.out.println("(3)ln(5x - 2) - ln2 = 1");
        System.out.println("(4)log15(4-x) = log15(-2x + 2)");
        System.out.println("(5)log3(2) + log3(8 + x) = log3(x^(2) - 4x)");
        System.out.println("(6)Force Flood");
        System.out.println("(7)Force Quit");
        System.out.println(">");        int chooser = sc.nextInt();
        if(chooser == 7){
            System.out.println("QUITTING....");
            Thread.sleep(200);
            for(int i = 0; i < 30; i++){
                System.out.println(" ");
            }
            System.out.println("____________________");
            IsUser = false;
                ContFunc = false;
        }
        else if(chooser == 6){
            System.out.println("IMPORTANT:\n to retun back to NERVcalc enter passkey\n there will be no prompt");
            Thread.sleep(4000);
            for (int i = 0; i < 20; i++){
                int Scabies = (int) (Math.random() * 5) + 0;
                if(Scabies == 1){
                    System.out.println("log(5)\n____________________________");
                    System.out.println("          "+Math.log(5));
                }
                else if(Scabies == 2){
                    System.out.println("ln(5)\n____________________________");
                    System.out.println("          "+ Math.log(5));
                }
                else if(Scabies == 3){
                    System.out.println("10 x 6 + 10\n____________________________");
                    System.out.println("          "+10*6+10);
                }
                else if(Scabies == 4){
                    System.out.println("12 + 67\n____________________________");
                    System.out.println("          "+12 + 67);
                }
                else if(Scabies == 5){
                    System.out.println("log(20)\n____________________________");
                    System.out.println("          "+Math.log(20));
                }
            }
            sc.nextInt();
            System.out.println("USER IMP REC...");
            Thread.sleep(200);
            System.out.println("REDIRECTING...");
            Thread.sleep(2000);
            System.out.println("__________");
        }
        else if (chooser == 1){
            System.out.println("______");
            System.out.println("TO SOLVE:");
            System.out.println("plug the given value to parameters and solve");
            System.out.println("___");
            System.out.println("if the equastion contains an X^2 then it will be a porlabora");
            System.out.println("graph by the 1,3,5,7 rule * run");
            System.out.println("___");
            System.out.println("TO GRAPH");
            System.out.println("if x is presented in the parameter as: x < # then y int\n will be 0");
            System.out.println("Y-int will be 'b' value connected to the equastion");
            System.out.print("enter 3 to return to menu");
            System.out.println();
            sc.nextInt();
        }
        else if(chooser == 2){
            System.out.println("______");
            System.out.println("#-3e^(7x+9) + 6 = -6");
            System.out.println("1- subtract 6 from noth sides");
            System.out.println("2- divide by 3");
            System.out.println("3- subtract 9 from both sides");
            System.out.println("4- solve top");
            System.out.println("5- divide by 7");
            System.out.println("final: -1.088");
            sc.nextInt();
        }
        else if(chooser == 3){
            System.out.println("______");
            System.out.println("#ln(5x - 2) - ln2 = 1");
            System.out.println("1- re-write => ln(A/B)");
            System.out.println("    ln(5x-2/2) = e");
            System.out.println("2- multiply both sides by 2");
            System.out.println("    get rid of denom");
            System.out.println("3- add 2 to both sides");
            System.out.println("4- divide by 5");
            System.out.println("5- (2e~5.436 + 2) /5");
            System.out.println("final: ~1.487");
        }
        else if(chooser == 4){
            System.out.println("______");
            System.out.println("log15(4-x) = log15(-2x + 2)");
            System.out.println("1- logb(A) = logb(B) => A=B");
            System.out.println("    4-x = -2x+2");
            System.out.println("2- add 2x to both sides");
            System.out.println("    4 + x = 2");
            System.out.println("3- subtract 4 from both sides");
            System.out.println("final: X = -2");
            sc.nextInt();
        }
        else if(chooser == 5){
            System.out.println("______");
            System.out.println("#log3(2) + log3(8 + x) = log3(x^(2) - 4x)");
            System.out.println("1- re-wrie as: logb(A)+logb(B) = log(AxB)");
            System.out.println("    log3(2)+log3(8+1)=log3(2(8+x))");
            System.out.println("Simplifys => log3(2(8+x)) = log3(x^2-4x)");
            System.out.println("2- remove logarythims");
            System.out.println("    16+2x=x^2-4x");
            System.out.println("simplifys => 0=x^2-6x-16");
            System.out.println("3- solve quadratic");
            sc.nextInt();
        }
    }
    sc.close();
}
}
