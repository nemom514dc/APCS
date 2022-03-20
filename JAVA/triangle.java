public class triangle{
public static void main(String args[]){
Scanner sca = new Scanner(System.in);//產生Scanner物件
 System.out.print("輸入 三角 形的 底(公分):");
int base = sca.nextInt();
System.out.print("輸入 三角 形的 高(公分):");
int height = sca.nextInt();
double area=(base*height)/2;
System.out.println("面積: "+area+"平方公分");
}//main()
}//class