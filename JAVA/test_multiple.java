import java.util.Scanner;
public class test_multiple{
 public static void main(String args[]){
  Scanner input=new Scanner(System.in);
  System.out.print("叫块计:");
  int a=input.nextInt();
  if(a%3==0)
   System.out.println("硂琌3计");
  else
   System.out.println("硂ぃ琌3计");
  if(a%5==0)
   System.out.println("硂琌5计");
  else
   System.out.println("硂ぃ琌5计");
  if(a%7==0)
   System.out.println("硂琌7计");
  else
   System.out.println("硂ぃ琌7计");
  if(a%11==0)
   System.out.println("硂琌11计");
  else
   System.out.println("硂ぃ琌11计");
 }
}