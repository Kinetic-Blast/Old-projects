
public class Fib {
	static int calls;
	
	public static int fib(int n , int tabs) {
		calls++;
		if (n==0 ||n ==1) {
			for (int i = 0; i< tabs; i++) {System.out.print("\t");}
			
			if (n == 0) {System.out.println("fib(0) --> 0");}
			
			if (n == 1) {System.out.println("fib(1) --> 1");}
			
			return n;}
		
		int result = fib(n-1, tabs+1);
		
		for (int i = 0; i < tabs; i++) {System.out.print("\t");}
		
		System.out.println("fib("+n+")");
		result += fib(n-2,tabs+1);
		return result;}
	
	public static void main(String args []) {
		calls = 0;
		fib(20,0);}}
