/*
create a variable called 'a' and input numbers ranging from 1 to 5
create a variable called 'b' and input numbers ranging from 2 to 6
create a variable called 'a**b' and input the value of a raise to power b
*/

public class Task5{

	public static void main(String[] args){

		System.out.println("a \t b \t a**b");


		for(int count = 1; count <= 5; count++){

			System.out.println(count);

		}

		for(int count = 2; count <= 6; count++){

			System.out.printf("\t%d",count);

		}

	}

}