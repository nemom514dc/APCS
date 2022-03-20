public class input_string{
public static void main(String args[]){
java.io.InputStream in = System.in;
        char c;
        try {
            System.out.print("請輸入字串：");
            while ((c = (char) in.read()) > 0) {

                System.out.print(c);

                if (c == '\n')// 換行符號
                    System.out.print("請輸入字串：");

            }
        } catch (java.io.IOException ex) {
            ex.printStackTrace();
        }
    }
}