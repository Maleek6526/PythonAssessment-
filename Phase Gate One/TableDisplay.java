/*
create a variable called 'a' and input numbers ranging from 1 to 5
create a variable called 'b' and input numbers ranging from 2 to 6
create a variable called 'a**b' and input the value of a raise to power b
*/

public class TableDisplay{

	public static void main(String[] args){

		System.out.println("a \t b \t a**b");

		System.out.printf("1 \t 2 \t %d%n", (int) Math.pow(1, 2));
		System.out.printf("2 \t 3 \t %d%n", (int) Math.pow(2, 3));
		System.out.printf("3 \t 4 \t %d%n", (int) Math.pow(3, 4));
		System.out.printf("4 \t 5 \t %d%n", (int) Math.pow(4, 5));
		System.out.printf("5 \t 6 \t %d%n", (int) Math.pow(5, 6));
		

	}

}