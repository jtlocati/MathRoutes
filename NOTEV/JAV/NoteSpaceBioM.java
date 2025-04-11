package NOTEV.JAV;

//biomed qizz 3.1.1 - 3.1.3

import java.util.Scanner;
import java.util.ArrayList;
public class NoteSpaceBioM{
public static void main(String[] args) throws InterruptedException {
    NoteSpaceBioM player = new NoteSpaceBioM();
    Scanner sc = new Scanner(System.in);
    boolean ContFunc = true;
    String seperator = "................................";
    while(ContFunc == true){
        System.out.println("______");
        System.out.println("biomed test 3.1 -> 3.3");
        System.out.println("(1)flow of blood through the body");
        System.out.println("(2)Conduction system");
        System.out.println("(3)EKG components");
        System.out.println("(4)Equastions");
        System.out.println("(5)");
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
            System.out.println("Right Atrum => Tricuspid valve");
            System.out.println("Right ventrical => Pulmanary val");
            System.out.println("pulmanary art => lungs => O2 <-> co2");
            System.out.println("Pulmanary vein => left atrium");
            System.out.println("Mitral => Left Ven => Aortic ven");
            System.out.println("Arota => Systemic Artaoies ");
            System.out.println("Systemic capill => O2 <-> Co2");
            System.out.println("Systemic ven => Systemic veins");
            System.out.println("vana cava");
            System.out.println("enter any number to see functions");
            sc.nextInt();
            System.out.println("Right Atrium");
            System.out.println("Receives deoxygenated blood from the body");
            sc.nextInt();
            
            System.out.println("Tricuspid Valve");
            System.out.println("Prevents backflow into right atrium");
            sc.nextInt();
            
            System.out.println("Right Ventricle");
            System.out.println("Pumps blood to lungs");
            sc.nextInt();
            
            System.out.println("Pulmonary Valve");
            System.out.println("Controls blood flow into pulmonary artery");
            sc.nextInt();
            
            System.out.println("Pulmonary Artery");
            System.out.println("Carries deoxygenated blood to lungs");
            sc.nextInt();
            
            System.out.println("Lungs");
            System.out.println("Exchange CO₂ for O₂");
            sc.nextInt();
            
            System.out.println("Pulmonary Vein");
            System.out.println("Returns oxygenated blood to heart");
            sc.nextInt();
            
            System.out.println("Left Atrium");
            System.out.println("Receives oxygenated blood from lungs");
            sc.nextInt();
            
            System.out.println("Mitral (Bicuspid) Valve");
            System.out.println("Prevents backflow into left atrium");
            sc.nextInt();
            
            System.out.println("Left Ventricle");
            System.out.println("Pumps oxygenated blood to the body");
            sc.nextInt();
            
            System.out.println("Aortic Valve");
            System.out.println("Controls blood flow into aorta");
            sc.nextInt();
            
            System.out.println("Aorta");
            System.out.println("Distributes oxygenated blood to body");
            sc.nextInt();
            
            System.out.println("Systemic Arteries");
            System.out.println("Carry oxygen-rich blood to tissues");
            sc.nextInt();
            
            System.out.println("Systemic Arterioles");
            System.out.println("Regulate blood flow to capillaries");
            sc.nextInt();
            
            System.out.println("Systemic Capillaries");
            System.out.println("Exchange oxygen and nutrients with cells");
            sc.nextInt();
            
            System.out.println("Systemic Venules");
            System.out.println("Collect deoxygenated blood from tissues");
            sc.nextInt();
            
            System.out.println("Systemic Veins");
            System.out.println("Return blood to the heart");
            sc.nextInt();
            
            System.out.println("Inferior/Superior Vena Cava");
            System.out.println("Bring deoxygenated blood to right atrium");
            sc.nextInt();
            
        }
        else if(chooser == 2){
            System.out.println(seperator);
            System.out.println("SA Node => AV Node");
            System.out.println("Bundle of His => Right Bundle Branch");
            System.out.println("Left Bundle Branch => Purkinje Fibers");
            sc.nextInt();
        }
        else if(chooser == 3){
            System.out.println(seperator);
            System.out.println("deflections:");
            System.out.println("upwards or downwards trend");
            sc.nextInt();
            System.out.println(seperator);
            System.out.println("pwave");
            System.out.println("shows atrial depolarization\nwhen sa node fires leading\nto and atrialcoontract");
            sc.nextInt();
            System.out.println(seperator);
            System.out.println("QRS Complex");
            System.out.println("consists of the QRS complex allinging\n with ventrical contractions");
            sc.nextInt();
            System.out.println(seperator);
            System.out.println("PR Segment");
            System.out.println("delayed eletrical contractions\nallowing for ventricals to be\nfilled with blood");
            sc.nextInt();
            System.out.println(seperator);
            System.out.println("St segment");
            System.out.println("heart is pumping blood");
            System.out.println("St wave");
            System.out.println("after pr the heart is repolarized ");
            System.out.println("(1)see exsample");
            System.out.println(">");          sc.nextInt();
            System.out.println("___/\\__u/\\u__/\\");
            System.out.println("   P    Q R S   T");
            sc.nextInt();
        }
        else if(chooser == 4){
            System.out.println(seperator);
            System.out.println("(1)Cardiac output");
            System.out.println("(2)ABI");
            int EquChoo = sc.nextInt();
            if(EquChoo ==1){
                System.out.println(seperator);
            System.out.println("CO = HR * SV");
            System.out.println("stroke vol = amound of\nblood pumped with each pump");
            System.out.println("enter HR");
            System.out.print(">");      int HR = sc.nextInt();
            System.out.println("enter SV");
            System.out.print(">");     int SV = sc.nextInt();
            System.out.println(seperator);
            System.out.println("the Cardiac output is :" + Math.abs(HR*SV));
            }
            else if(EquChoo == 2){
                double fin = 0;
                double Nif = 0;
                System.out.println(seperator);
                System.out.println("ABI = \nHigh Right anke pressur/high arm pressure");
                System.out.println("what is the higher right leg pressure?");
                System.out.print(">");     int HIGarm = sc.nextInt();
                System.out.println("what is the higher arm pressure?");
                System.out.print(">");     int HIGLeg = sc.nextInt();
                System.out.println(seperator);
                System.out.println("what is the higher left leg pressure");
                System.out.print(">");     int HIGarm2 = sc.nextInt();
                double Sol1 = (Math.abs(HIGLeg/HIGarm2));
                double Sol2 = (Math.abs(HIGLeg/HIGarm));
                if(Sol1 > Sol2){
                    fin = Sol1;
                    Nif = Sol2;
                }
                else{
                    fin = Sol2;
                    Nif = Sol1;
                }
                System.out.println(seperator);
                System.out.println("solution 1 = " + Nif);
                System.out.println("solution 2 = "  + fin);
                System.out.println(fin + " is the correct sollution");
            }
        }
        else if(chooser == 5){
            sc.nextInt();
        }
    }
    sc.close();
}
}

    
