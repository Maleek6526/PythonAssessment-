/*
prompt the user to enter three integers
display then in decreasing order

*/

import java.util.Scanner;

public class Task2{

	public static void main(String[] args){

		Scanner scanner = new Scanner(System.in);

		System.out.println("Enter the first number: ");
		int firstUserInput = scanner.nextInt();

		System.out.println("Enter the second number: ");

		int secondUserInput = scanner.nextInt();


		System.out.println("Enter the third number: ");

		int thirdUserInput = scanner.nextInt();


	if(firstUserInput < secondUserInput && firstUserInput < thirdUserInput && secondUserInput < thirdUserInput){

		System.out.printf("%d,%d,%d", firstUserInput, secondUserInput,thirdUserInput );

	} 


	if(secondUserInput < firstUserInput && secondUserInput < thirdUserInput && firstUserInput < thirdUserInput){

		System.out.printf("%d,%d,%d", secondUserInput, firstUserInput, thirdUserInput);

	} 

	if(thirdUserInput < firstUserInput && thirdUserInput < secondUserInput && firstUserInput < secondUserInput){

		System.out.printf("%d,%d,%d", thirdUserInput, firstUserInput, secondUserInput);

	} 

}
}