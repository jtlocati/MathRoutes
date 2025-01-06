import java.util.Scanner;
public class SinDiv{
    public Double workerb(double a, double b, double c, double d, int f){
        double finish =0;
        int buck = 0;
        double X3 = 0;

        Scanner valone = new Scanner(System.in);
            Scanner valtwo = new Scanner(System.in);
                Scanner valthree = new Scanner(System.in);
                        Scanner DivVal = new Scanner(System.in);
                            Scanner len = new Scanner(System.in);
                                System.out.println("what is the length of the function? ");
                        f = len.nextInt();
        if (f == 4){
        System.out.println("what is the first value? ");
            a = valone.nextDouble();
        System.out.println("what is the second value? ");
            b = valtwo.nextDouble();
        System.out.println("What is the third value? ");
            c = valthree.nextDouble();
        System.out.println("What is the fourth value? ");
            d = DivVal.nextDouble();
        }
        else{
            System.out.println("what is the first value? ");
            a = valone.nextDouble();
        System.out.println("what is the second value? ");
            b = valtwo.nextDouble();
        System.out.println("What is the fourth value? ");
            d = DivVal.nextDouble();
        c = 1;

        }
        double fucy [] = {a, b, c, d,};
        for (int i = 0;  i >= fucy.length; i++){ 
            buck += 0;
            if (buck > 1){
                X3 = fucy[i] - fucy [i + 1];
                

            }
        } 
        return finish;
    }
    public static void main(String []args){
        SinDiv player = new SinDiv();
        player.workerb(0, 0,0, 0, 0);

    } 
}