import java.util.Scanner;
public class test_multiple{
 public static void main(String args[]){
  Scanner input=new Scanner(System.in);
  System.out.print("�п�J�Ʀr:");
  int a=input.nextInt();
  if(a%3==0)
   System.out.println("�o�O3������");
  else
   System.out.println("�o���O3������");
  if(a%5==0)
   System.out.println("�o�O5������");
  else
   System.out.println("�o���O5������");
  if(a%7==0)
   System.out.println("�o�O7������");
  else
   System.out.println("�o���O7������");
  if(a%11==0)
   System.out.println("�o�O11������");
  else
   System.out.println("�o���O11������");
 }
}