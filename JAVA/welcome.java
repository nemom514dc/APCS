public class welcome{
public static void main(String args[]){
java.io.InputStream in = System.in;
        int r;
        try {
            System.out.print("½Ð¿é¤J¥b®|(cm):");
            while ((r = (int) in.read()) > 0) {
                  int area=r*r;
                  int b=r;
                  System.out.println(area);
                  System.out.print(b);
            }
        } catch (java.io.IOException ex) {
            ex.printStackTrace();
        }
}
}