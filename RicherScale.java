import java.util.Scanner;

public class RicherScale {
    
    public String RicherScaleEN(double Magnitude, String ret) {
        double power = (Magnitude * (1.5));
        double power2u = (power + 11.8);

        // Extract integer and decimal parts 
        double power2uDIV = power2u - Math.floor(power2u); 
        double Econtaner = Math.pow(10, power2uDIV);
        Econtaner = Math.round(Econtaner * 100.0) / 100.0; // Round for display

        // Compute total energy
        double totalEnergy = Math.pow(10, power2u);

        // Print results
        System.out.println("> total Energy output (Uncompressed): " + totalEnergy);
        ret = ("> E ~ " + Econtaner + " x 10^" + (int)(power2u - power2uDIV));
        return ret;
    }

    public static void main(String[] args) throws InterruptedException {
        Scanner sc = new Scanner(System.in);
        RicherScale player = new RicherScale();

        System.out.println("Continue with Richter Scale Calculations? (Y/N)");
        String confirm = sc.next().toLowerCase();

        if (confirm.equals("y")) {
            System.out.println("Input magnitude: ");
            double MAG = sc.nextDouble(); 

            System.out.println("Calculating...");
            Thread.sleep(2000);

            System.out.println(player.RicherScaleEN(MAG, ""));
        } else {
            System.out.println("Exiting...");
        }
        sc.close();
    }
}
