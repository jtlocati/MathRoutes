import java.util.Scanner;

public class ExitRep {

  public static void main(String [] args) throws InterruptedException{
    //contains easter eggs.
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
    Scanner sc = new Scanner(System.in);
    boolean continues = true;
    while (continues == true) {
        
    System.out.println("continue using function? Y/N");
    String confirm = sc.next().toLowerCase();
    if(confirm.equals("y")){
        System.out.println("\rheres yo numbers nigga\n");
    }
    else{
        int randomQuip = ((int) (Math.random()* references.length));
        System.out.println(references[randomQuip]);
        for (int i = 0; i < 13; i++){
            int randomsus = (1 + (int)(Math.random() * 9999));
            System.out.print("\rclosing file: " + randomsus );
            Thread.sleep(500);
            System.out.print("\r");
            if(i < 1){
            Thread.sleep(300);
            System.out.println("> This ensures data is not traceable");
            }
        }
            Thread.sleep(2000);
            continues = false;
            break;
    }
}
    System.out.println("");
    System.out.println("\rHome: Functions");
    System.out.println("(1)log");
    System.out.println("(2)exponental");
    System.out.println("(3)compounding");
    sc.close();
  }
}

