/*
write a program that reads the numbers only from range 0 to 1000
prompt the user for input
if the number inputted is lower than zero or higher than 1000, display numbers at this range is not allowed
if the number inputted is at the range, calculate the sum of the number
display the sum
*/


import java.util.Scanner;

public class Task4{

	public static void main(String[] args){

		Scanner scanner = new Scanner(System.in);

		System.out.print("Enter an integer number starting from range 0 to 1000: ");
		int userInput = scanner.nextInt();

		if(userInput < 0 || userInput > 1000){

			System.out.println("Numbers at this range is not allowed");

		}

		int reverse = 0;

		int sumOfTheNumbers = 0;

		while(userInput != 0){

			reverse = (reverse * 10) + userInput % 10;

			userInput = userInput / 10;

			sumOfTheNumbers += reverse;

		}
		
		System.out.println(reverse);
		System.out.print(sumOfTheNumbers);

	}

}