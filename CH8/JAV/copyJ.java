package CH8.JAV;
import java.util.Scanner;
import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;

public class copyJ {
    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);
        System.out.println("problem number");
        System.out.print(">");  String ProbNum = sc.next();

        System.out.println("what is problem " + ProbNum );
        System.out.print(">");  String Poblem = sc.next();
         try(BufferedWriter writer = new BufferedWriter(new FileWriter("PROBjav.txt", true))){
            writer.write(ProbNum + " ~~~" + Poblem);
            writer.newLine();
            System.out.println("Entry saved successfully");
         }
         catch (IOException e){
            System.out.println("Error Writeinf file" + e.getMessage());
         }
         sc.close();
    }
}
