import java.util.Scanner;

public class test_multiple_v2{
	public static void main(String args[]){
		Scanner input=new Scanner(System.in);
		System.out.print("請輸入數字:");
		int a=input.nextInt();
		char[] b={ '0','0','0','0' };
		
		if(a%3==0)
			b[0]='3';
		else
			b[0]='0';
		if(a%5==0)
			b[1]='5';
		else
			b[1]='0';
		if(a%7==0)
			b[2]='7';
		else
			b[2]='0';
		if(a%11==0)
			b[3]='1';
		else
			b[3]='0';
		
		if(!(b[0]=='0' && b[1]=='0' && b[2]=='0' && b[3]=='0')){ 
			System.out.print("它是");
			if(b[0]=='3')
				System.out.print("3 ");
			if(b[1]=='5')
				System.out.print("5 ");
			if(b[2]=='7')
				System.out.print("7 ");
			if(b[3]=='1')
				System.out.print("11");
			System.out.println("的倍數");
		}
		
		if(!(b[0]=='3' && b[1]=='5' && b[2]=='7' && b[3]=='1')){
			System.out.print("它不是");
			if(b[0]=='0')
				System.out.print("3 ");
			if(b[1]=='0')
				System.out.print("5 ");
			if(b[2]=='0')
				System.out.print("7 ");
			if(b[3]=='0')
				System.out.print("11");
			System.out.print("的倍數");
		}
	}
}