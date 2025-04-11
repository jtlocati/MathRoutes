package LandingComp;
import java.util.Scanner;
public class UserLOG {
    //TODO"
    /*
     * fix password limit function, 
     *      issues with entry restriction
     *      issule with  boolean reset after inccoret
     */
    public void Agree(){
        Scanner sc = new Scanner(System.in);
        String Seperator = "......................";
        System.out.println("NervCalc Terms of Service (3/22/24)");
        System.out.println(Seperator);
        System.out.println("(1)INTENDED USE");
        System.out.println("NERVcalc is designed solely for educational support outside of the classroom. It is not to be used during:\n~In-class quizzes, tests, or exams\n~Standardized or national testing environments\n~The ACT, SAT, AP Exams, or any other proctored assessments\nUse of NERVcalc in any formal assessment setting is strictly prohibited.");
        System.out.println("$$$press any number to continue");
        sc.next();
        System.out.println(Seperator);
        System.out.println("(2)ACEDEMIC RESPONSIBILITY");
        System.out.println("You are fully responsible for ensuring that your use of NERVcalc aligns with your schools academic integrity policies. NERVcalc is a supplementary study tool. NOT TO BE USED AS A TOOL FOR TEST TAKING.");
        System.out.println("$$$press any number to continue");      sc.nextInt();
        System.out.println(Seperator);
        System.out.println("(3)USER ASSUMES ALL RISK");
        System.out.println("By using NERVcalc, you accept full liability for any academic, disciplinary, or institutional consequences that may result from its misuse.");
        System.out.println("$$$press any number to continue");      sc.nextInt();
        System.out.println(Seperator);
        System.out.println("(4)NO AFFILIATION");
        System.out.println("NERVcalc is an independent tool and is not affiliated with or endorsed by any school, testing agency, or educational institution.");
        System.out.println("$$$press any number to continue");      sc.nextInt();
        System.out.println(Seperator);
        System.out.println("(5)NO LIABLILITY");
        System.out.println("NERVcalc and its Creators is not liable for any misuse of the calculator. If disciplinary action is taken against a user due to improper use, NERVcalc and its creators hold no responsibility.");
        System.out.println("$$$press any number to return to start page");      sc.nextInt();
        System.out.println("Agree Y/N");
        sc.next().toLowerCase();
    }
public boolean showDisclaimer() throws InterruptedException {
    UserLOG player = new UserLOG();
    Scanner sc = new Scanner(System.in);
    boolean Continue = false;
    Thread.sleep(3000);

    while (Continue == false) {
        System.out.println("DISCLAIMER:");
        System.out.println("NERVcalc is intended for non-test purposes only.");
        System.out.println("Please follow your school's academic integrity policy.");
        System.out.println("By proceeding, you agree to the NERVcalc Terms of Service.");
        System.out.println("(1) View Terms of Service\nProceed? Y/N");
        System.out.print("> ");

        String proceed = sc.next();

        if (proceed.equals("y")||proceed.equals("n")) {
            return true;
        } 
        else{
            player.Agree();
            return true;
        }
    }
    return true; // Fallback return
}
    public boolean IsUsers() throws InterruptedException{
        String Seperator = "................................";
        Scanner sc = new Scanner(System.in);
        boolean IsUser = false;
        int ATTLEF = 0;
        int ATTSG2 = 1;
        String[] Users = {"jet", "Izzy", "Wyatt", "Lucas", "Brendain", "Ross"};
        int[] PassKey = {4922, 123456, 909772, 1234, 12345, 1920};
        //passkey recignition
        while(IsUser == false){
            System.out.println("please enter your respective passkey:");
            System.out.print(">");     int catcher =  sc.nextInt();
            for(int i =0; i< Users.length;i++){
                if(catcher == PassKey[i]){
                    System.out.println("USER => " + Users[i]);
                    System.out.println("Hello " + Users[i] + " welcome to NERVcalc");
                IsUser = true;
                }
            }

        }
        //psskey rec v1.1
        /*while (IsUser == false){
        System.out.println("Plese enter passkey:");
        System.out.print(">");    int PasskeyIMP = sc.nextInt();
        for(int i = 0; i<Users.length; i++){
            if(ATTLEF > 3){
                ATTLEF = 0;
                ATTSG2++;
            }

            if(PasskeyIMP == PassKey[i]){
                System.out.println("USER => " + Users[i]);
                System.out.println("Hello " + Users[i] + " welcome to NERVcalc");
                IsUser = true;
            }
        }
        if(IsUser == false){
            System.out.println(Seperator);
        System.out.println("Passkey inncorrect\n " + Math.abs(ATTLEF-3) +" Remain");
        ATTLEF++;
        }
        if(ATTLEF == 3){
            if(ATTSG2 > 0){
                System.out.println(Seperator);
                System.out.println("Passkey input limit reached\nplease wait " + Math.abs((ATTLEF * 10) * ATTSG2) + " Seconds");
                Thread.sleep(Math.abs((ATTLEF * 10) * ATTSG2) * 1000);
            }
            System.out.println(Seperator);
            System.out.println("Passkey input limit reached\nplease wait" + Math.abs(ATTLEF * 10) + "Seconds");
            Thread.sleep(ATTLEF*1000);
        }
    }*/
    return IsUser;
    }
    
    public static void main(String[]args)throws InterruptedException{
        //prompts for Agree and Disclaimer
        String Seperator = "................................";
        UserLOG player = new UserLOG();
        Scanner sc = new Scanner(System.in);
        boolean IsHeUser = player.IsUsers();
        boolean Borat = player.showDisclaimer();

        if(IsHeUser == true && Borat == true){
            System.out.println(Seperator);
            //INPUT CODE
        }
        else{
            System.out.println("ERROR: " + (int)(Math.random()*999));
        }
        sc.close();
    } 
    
}
