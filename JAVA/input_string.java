public class input_string{
public static void main(String args[]){
java.io.InputStream in = System.in;
        char c;
        try {
            System.out.print("�п�J�r��G");
            while ((c = (char) in.read()) > 0) {

                System.out.print(c);

                if (c == '\n')// ����Ÿ�
                    System.out.print("�п�J�r��G");

            }
        } catch (java.io.IOException ex) {
            ex.printStackTrace();
        }
    }
}