import java.util.Scanner;
public class RicherScale {
    //Solves for missing energy output (E)
/*Library:
 * power = magnitude of earthquake (M)
 * Ret E = tatal Magnitude (E) 
 */
//void RetE == 0
    public String RicherScaleEN(double Magnitude, String ret){
        double power = (Magnitude * (1.5));
            double power2u = (power + 11.8);
                double power2uDIV = (power2u % 1); 
        double Ediv = (Math.round(power2uDIV * 100.0) / 100.0);
            double Econtaner = ((Math.pow(10, Ediv)));
                Econtaner = Math.round(Econtaner * 100.0) / 100.0;
        System.out.println("> total Energy output (Uncompressed): " + (Math.pow(10, power2u) * Econtaner));
        ret = ("> E ~ " + Econtaner + " = 10^" + (power2u - power2uDIV));
        return ret;
    }
    public static void main (String [] args) throws InterruptedException{
        Scanner sc = new Scanner(System.in);
            RicherScale player = new RicherScale();
    System.out.println("continue with RicherScle Calculations?, Y/N");
        String confirm = sc.next().toLowerCase();
    if(confirm.equals("y")){
        System.out.println("input magnitude: ");
        double MAG = sc.nextInt();
        System.out.println("calculateing...");
        Thread.sleep(200);
        System.out.println(player.RicherScaleEN(MAG, ""));
    }
    else{
        System.out.println("Exiting...");
    }
    sc.close();
    }
}
