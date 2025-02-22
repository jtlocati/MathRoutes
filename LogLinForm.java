import java.util.Scanner;
public class LogLinForm{
    public String LogTOling(String equastion, String ret){
        String Bfind = "";
            String Yfind = "";
                String Xfind = equastion.substring(equastion.lastIndexOf("}")+1);
        int Bindex = equastion.indexOf("(");
            int Yindex = equastion.indexOf(")");
        if(Bindex > 0){
            Bfind = equastion.substring(3,Bindex);
        }else{ret = "error, try input again.";}
        if (Yindex > 0) {
            Yfind = equastion.substring(Bindex + 1, Yindex);
        }else{ret = "error, try input again.";}
        System.out.println("Y: " + Yfind);
        System.out.println("B: " + Bfind);
        System.out.println("X: " + Xfind);
        ret = ("final: " + Bfind + "^" + Xfind + " = " + Yfind);
        return ret;
    }
    public String LinTOlog(String equastion, String ret){
        //exsample equastion == 11^2 = 121
        String Bbreak = "";
            String Xbreak = "";
                String Ybreak = ""; 
        int Bindex = equastion.indexOf("^");
            int Xindex = equastion.indexOf("{");
                int Yindex = equastion.indexOf("}"); 
                Ybreak = equastion.substring(equastion.lastIndexOf("}")+1);
        if(Bindex > 0){
            Bbreak = equastion.substring(0, Bindex);
        }else{ret = "input error, try again (error message #1)";}
        if(Xindex > 0){
            Xbreak = equastion.substring(Bindex + 1, Xindex);
        }else{ret="input error, try again (error message #2)";}
        if(Yindex > 0 ){
        }else{ret="input error, try againe (error message #3)";}

        System.out.println("B: " + Bbreak);
        System.out.println("X: " + Xbreak);
        System.out.println("Y: " + Ybreak);
        ret = ("final: LOG" + Bbreak + "(" + Ybreak + ") = " + Xbreak);
        return ret;
    }
    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);
            LogLinForm player = new LogLinForm();
        System.out.println("continue with equastion converstion? Y/N");
        String confirm = sc.next().toLowerCase();
        if(confirm.equals("y")){
        System.out.println(">>what is the form of converstion?");
        System.out.println(">(1)EX => LOG");
        System.out.println(">(2)LOG => EX");
            int confirmIN = sc.nextInt();
        if(confirmIN == 1){
            System.out.println(">>pleae enter equastion: ");
            System.out.println("= -> {}");
            System.out.println( "11\u00B2 = 121 (would be inputed as): 11^2{}121");
                String equastion = sc.next();
            System.out.println(player.LinTOlog(equastion, ""));
        }
        else if(confirmIN == 2){
            System.out.println(">>pleae enter equastion: ");
            System.out.println("log2(8) = 3, inputed as: log2(8){}3");
            String equastion = sc.next();
            System.out.println(player.LogTOling(equastion, ""));
        }
    }
    sc.close();
    }
}