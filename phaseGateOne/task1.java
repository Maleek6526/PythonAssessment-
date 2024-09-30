/*
write a code that generates two integer
the range of the number should be between 0 to 100
prompt the user to guess the sum of the two integers
if the user got it right, display answer is correct
if the user got it wrong, display false
*/

import java.util.Scanner;
public class Task1{

	public static void main(String[] args){

		Scanner scanner = new Scanner(System.in);

		int firstRandomNumber = (int) (Math.random()*100);

		int secondRandomNumber = (int) (Math.random()*100);

		System.out.print("Guess the sum of the two integers: ");
	
		int userGuesses = scanner.nextInt();


		int sumOfTheRandomNumbers = firstRandomNumber + secondRandomNumber;

	if(userGuesses != sumOfTheRandomNumbers){

		System.out.println("False");

	}

	if(userGuesses == sumOfTheRandomNumbers){

		System.out.printf("Answer is correct! the answer was %d", sumOfTheRandomNumbers);

	}

	}


}