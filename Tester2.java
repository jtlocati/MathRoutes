public class Tester2{
    public static void main(String[]args)throws InterruptedException{
        System.out.println("test");
        for(int i = 0; i< 34; i++){
            System.out.println(i + "itterrations");
            System.out.print(".");
            Thread.sleep(200);
        }
    }
}