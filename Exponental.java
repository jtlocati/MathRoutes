import java.util.Scanner;

public class Exponental {

    public double evaluate(int B, int Growth, int HarTime, int HarTime2, int KowHardTime, String wordtime2, String wordtime22, int howman) {
        double cosTime = 0;
        boolean timecheckword = !wordtime2.isEmpty();
        boolean timecheckknown = KowHardTime != 1010; // Ensure time frame is correctly checked

        String[] optio = {"day", "year", "month", "hour", "second", "millisecond", "week"}; 
        String Strwo1 = "", Strwo2 = "";

        // Match input time unit with predefined list
        for (String option : optio) {
            if (wordtime2.equals(option)) {
                Strwo1 = option;
                break;
            }
        }

        for (String option : optio) {
            if (wordtime22.equals(option)) {
                Strwo2 = option;
                break;
            }
        }

        // Time converstion Table:
        if (Strwo1.equals("day")) {
            if (Strwo2.equals("year")) cosTime = 365 * howman;
            else if (Strwo2.equals("month")) cosTime = 30 * howman;
            else if (Strwo2.equals("hour")) cosTime = 24 * howman;
            else if (Strwo2.equals("second")) cosTime = 86400 * howman;
            else if (Strwo2.equals("millisecond")) cosTime = 86400000 * howman;
            else if (Strwo2.equals("week")) cosTime = (1.0 / 7) * howman;
            else cosTime = howman; // Same unit
        } else if (Strwo1.equals("year")) {
            if (Strwo2.equals("day")) cosTime = (1.0 / 365) * howman;
            else if (Strwo2.equals("month")) cosTime = 12 * howman;
            else if (Strwo2.equals("hour")) cosTime = 8760 * howman;
            else if (Strwo2.equals("second")) cosTime = 31536000 * howman;
            else if (Strwo2.equals("millisecond")) cosTime = 31536000000L * howman;
            else if (Strwo2.equals("week")) cosTime = 52 * howman;
            else cosTime = howman;
        } else if (Strwo1.equals("month")) {
            if (Strwo2.equals("year")) cosTime = (1.0 / 12) * howman;
            else if (Strwo2.equals("day")) cosTime = 30 * howman;
            else if (Strwo2.equals("hour")) cosTime = 720 * howman;
            else if (Strwo2.equals("second")) cosTime = 2592000 * howman;
            else if (Strwo2.equals("millisecond")) cosTime = 2592000000L * howman;
            else if (Strwo2.equals("week")) cosTime = (1.0 / 4) * howman;
            else cosTime = howman;
        } else if (Strwo1.equals("hour")) {
            if (Strwo2.equals("day")) cosTime = (1.0 / 24) * howman;
            else if (Strwo2.equals("year")) cosTime = (1.0 / 8760) * howman;
            else if (Strwo2.equals("month")) cosTime = (1.0 / 720) * howman;
            else if (Strwo2.equals("second")) cosTime = 3600 * howman;
            else if (Strwo2.equals("millisecond")) cosTime = 3600000 * howman;
            else if (Strwo2.equals("week")) cosTime = (1.0 / 168) * howman;
            else cosTime = howman;
        } else if (Strwo1.equals("second")) {
            if (Strwo2.equals("day")) cosTime = (1.0 / 86400) * howman;
            else if (Strwo2.equals("year")) cosTime = (1.0 / 31536000) * howman;
            else if (Strwo2.equals("month")) cosTime = (1.0 / 2592000) * howman;
            else if (Strwo2.equals("hour")) cosTime = (1.0 / 3600) * howman;
            else if (Strwo2.equals("millisecond")) cosTime = 1000 * howman;
            else if (Strwo2.equals("week")) cosTime = (1.0 / 604800) * howman;
            else cosTime = howman;
        } else if (Strwo1.equals("millisecond")) {
            if (Strwo2.equals("day")) cosTime = (1.0 / 86400000) * howman;
            else if (Strwo2.equals("year")) cosTime = (1.0 / 31536000000L) * howman;
            else if (Strwo2.equals("month")) cosTime = (1.0 / 2592000000L) * howman;
            else if (Strwo2.equals("hour")) cosTime = (1.0 / 3600000) * howman;
            else if (Strwo2.equals("second")) cosTime = (1.0 / 1000) * howman;
            else if (Strwo2.equals("week")) cosTime = (1.0 / 604800000) * howman;
            else cosTime = howman;
        } else if (Strwo1.equals("week")) {
            if (Strwo2.equals("day")) cosTime = 7 * howman;
            else if (Strwo2.equals("year")) cosTime = (1.0 / 52) * howman;
            else if (Strwo2.equals("month")) cosTime = (1.0 / 4) * howman;
            else if (Strwo2.equals("hour")) cosTime = 168 * howman;
            else if (Strwo2.equals("second")) cosTime = 604800 * howman;
            else if (Strwo2.equals("millisecond")) cosTime = 604800000 * howman;
            else cosTime = howman;
        } else {
            System.out.println("Invalid time unit entered.");
            return -1;
        }


        // If a known timeframe is provided
        if (timecheckknown && HarTime == 0 && HarTime2 == 0) {
            cosTime = KowHardTime;
        } else if (!timecheckknown) {  // If we don’t know the timeframe, calculate using difference
            cosTime = howman;  // Ensure the time difference from input is used
        }

        // Calculate final exponential growth
        double fincomp1 = (Growth * 0.01) + 1;
        double fincomp2 = Math.pow(fincomp1, cosTime);
        double finisher = B * fincomp2;

        System.out.println("Time: " + cosTime);
        System.out.println("Growth rate: " + fincomp1);
        System.out.println("Initial value: " + B);

        return finisher;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Exponental workerB = new Exponental();

        System.out.println("Continue with Exponential graph? (Y/N)");
        String confirm = sc.next().toLowerCase();

        if (confirm.equals("y")) {
            System.out.println("Start value:");
            int sv = sc.nextInt();

            System.out.println("Growth percentage (enter full number):");
            System.out.println("if this is a Half Life problem enter \"0000\"" );
            int pcVal = sc.nextInt();

            System.out.println("Do you know the time frame? (Y/N)");
            String know = sc.next().toLowerCase();

            if (know.equals("y")) {
                System.out.println("Enter the timeframe:");
                int HardCodeTF = sc.nextInt();
                double finalcomp3 = (pcVal * .01) + 1;
                    double finalcomp2 = Math.pow(finalcomp3, HardCodeTF);
                        double finalcomp1 = sv * finalcomp2;
                System.out.println(finalcomp1);
                //System.out.println(workerB.evaluate(sv, pcVal, 0, 0, HardCodeTF, "", "", 0));
            } else {
                System.out.println("Is the question based on:");
                System.out.println("(1) Difference in time (e.g., 1990 -> 2020)");
                System.out.println("(2) Growth over a period (e.g., grows X amount in 5 days, how much in 5 years)");
                System.out.println("(3) HalfLife");
                int confgrad = sc.nextInt();

                if (confgrad == 1) {
                    System.out.println("Enter two timeframes:");
                    System.out.print("Year 1: ");
                    int yearone = sc.nextInt();
                    System.out.print("Year 2: ");
                    int yeartwo = sc.nextInt();
                    System.out.println(workerB.evaluate(sv, pcVal, yearone, yeartwo, 1010, "", "", 0));
                } else if(confgrad == 2) {
                    System.out.println("Include two of the following time units: \"day\", \"year\", \"month\", \"hour\", \"second\", \"millisecond\", \"week\"");
                    System.out.println("(if there is only on time of measurement, put the same unit of measurement for both inputs)");
                    System.out.print("Timeframe one: ");
                    String tfONE = sc.next().toLowerCase();
                    System.out.print("Timeframe two: ");
                    String tfTWO = sc.next().toLowerCase();
                    System.out.print("How many times (e.g., how much will it grow in 5 years): ");
                    int howm = sc.nextInt();

                    System.out.println(workerB.evaluate(sv, pcVal, 0, 0, 1010, tfONE, tfTWO, howm));
                }else{
                        System.out.println("Half-Life");
                        int HalfLife = sc.nextInt();
                            System.out.println("over how many years?");
                            int HLyears = sc.nextInt();
                    double HLTF3 = HLyears / HalfLife;
                        double HTLF2 = Math.pow(.5, HLTF3);
                            double HLfinal = HTLF2 * sv;
                    System.out.println("Final Remains:  " + HLfinal);
                    System.out.println("Final loss:  " + (Math.abs(sv - HLfinal)));  

                }
            }
        }
        sc.close();
    }
}

