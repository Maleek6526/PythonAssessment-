/*

prompt the user to enter an integer for today's day of the week
prompt the user to enter the number of days after today for a future day ahead
create the days of the week
make Sunday as 0, Monday as 1 ... Saturday as 6
display the future day of the week
*/

import java.util.Scanner;

public class Task3{

	public static void main(String[] args){

		theMain();

	}


	public static void theMain(){

		Scanner scanner = new Scanner(System.in);
		System.out.println("Enter Today's day: ");
		int userInput = scanner.nextInt();

		switch(userInput){
			
			case 0: sunday(); break;
			case 1: monday(); break;
			case 2: tuesday(); break;
			case 3: wednesday(); break;
			case 4: thursday(); break;
			case 5: friday(); break;
			case 6: saturday(); break;
			default: System.out.print("Invalid input");

		}
	}

	public static void sunday(){

		Scanner scanner = new Scanner(System.in);
		System.out.println("Enter the number of elapsed since today: ");
		int userElapseInput = scanner.nextInt();

		if(userElapseInput == 0){

			System.out.printf("Today is %s and the future day is %s", "Sunday", "Sunday");

		}

		if(userElapseInput == 1){

			System.out.printf("Today is %s and the future day is %s", "Sunday", "Monday");

		}

		if(userElapseInput == 2){

			System.out.printf("Today is %s and the future day is %s", "Sunday", "Tuesday");

		}

		if(userElapseInput == 3){

			System.out.printf("Today is %s and the future day is %s", "Sunday", "Wednesday");

		}

		if(userElapseInput == 4){

			System.out.printf("Today is %s and the future day is %s", "Sunday", "Thursday");

		}

		if(userElapseInput == 5){

			System.out.printf("Today is %s and the future day is %s", "Sunday", "Friday");

		}

		if(userElapseInput == 6){

			System.out.printf("Today is %s and the future day is %s", "Sunday", "Saturday");

		}

	}


	public static void monday(){

		Scanner scanner = new Scanner(System.in);
		System.out.println("Enter the number of elapsed since today: ");
		int userElapseInput = scanner.nextInt();

		if(userElapseInput == 0){

			System.out.printf("Today is %s and the future day is %s", "Monday", "Sunday");

		}

		if(userElapseInput == 1){

			System.out.printf("Today is %s and the future day is %s", "Monday", "Monday");

		}

		if(userElapseInput == 2){

			System.out.printf("Today is %s and the future day is %s", "Monday", "Tuesday");

		}

		if(userElapseInput == 3){

			System.out.printf("Today is %s and the future day is %s", "Monday", "Wednesday");

		}

		if(userElapseInput == 4){

			System.out.printf("Today is %s and the future day is %s", "Monday", "Thursday");

		}

		if(userElapseInput == 5){

			System.out.printf("Today is %s and the future day is %s", "Monday", "Friday");

		}

		if(userElapseInput == 6){

			System.out.printf("Today is %s and the future day is %s", "Monday", "Saturday");

		}

	}



	public static void tuesday(){

		Scanner scanner = new Scanner(System.in);
		System.out.println("Enter the number of elapsed since today: ");
		int userElapseInput = scanner.nextInt();

		if(userElapseInput == 0){

			System.out.printf("Today is %s and the future day is %s", "Tuesday", "Sunday");

		}

		if(userElapseInput == 1){

			System.out.printf("Today is %s and the future day is %s", "Tuesday", "Monday");

		}

		if(userElapseInput == 2){

			System.out.printf("Today is %s and the future day is %s", "Tuesday", "Tuesday");

		}

		if(userElapseInput == 3){

			System.out.printf("Today is %s and the future day is %s", "Tuesday", "Wednesday");

		}

		if(userElapseInput == 4){

			System.out.printf("Today is %s and the future day is %s", "Tuesday", "Thursday");

		}

		if(userElapseInput == 5){

			System.out.printf("Today is %s and the future day is %s", "Tuesday", "Friday");

		}

		if(userElapseInput == 6){

			System.out.printf("Today is %s and the future day is %s", "Tuesday", "Saturday");

		}

	}


	public static void wednesday(){

		Scanner scanner = new Scanner(System.in);
		System.out.println("Enter the number of elapsed since today: ");
		int userElapseInput = scanner.nextInt();

		if(userElapseInput == 0){

			System.out.printf("Today is %s and the future day is %s", "Wednesday", "Sunday");

		}

		if(userElapseInput == 1){

			System.out.printf("Today is %s and the future day is %s", "Wednesday", "Monday");

		}

		if(userElapseInput == 2){

			System.out.printf("Today is %s and the future day is %s", "Wednesday", "Tuesday");

		}

		if(userElapseInput == 3){

			System.out.printf("Today is %s and the future day is %s", "Wednesday", "Wednesday");

		}

		if(userElapseInput == 4){

			System.out.printf("Today is %s and the future day is %s", "Wednesday", "Thursday");

		}

		if(userElapseInput == 5){

			System.out.printf("Today is %s and the future day is %s", "Wednesday", "Friday");

		}

		if(userElapseInput == 6){

			System.out.printf("Today is %s and the future day is %s", "Wednesday", "Saturday");

		}

	}


	public static void thursday(){

		Scanner scanner = new Scanner(System.in);
		System.out.println("Enter the number of elapsed since today: ");
		int userElapseInput = scanner.nextInt();

		if(userElapseInput == 0){

			System.out.printf("Today is %s and the future day is %s", "Thursday", "Sunday");

		}

		if(userElapseInput == 1){

			System.out.printf("Today is %s and the future day is %s", "Thursday", "Monday");

		}

		if(userElapseInput == 2){

			System.out.printf("Today is %s and the future day is %s", "Thursday", "Tuesday");

		}

		if(userElapseInput == 3){

			System.out.printf("Today is %s and the future day is %s", "Thursday", "Wednesday");

		}

		if(userElapseInput == 4){

			System.out.printf("Today is %s and the future day is %s", "Thursday", "Thursday");

		}

		if(userElapseInput == 5){

			System.out.printf("Today is %s and the future day is %s", "Thursday", "Friday");

		}

		if(userElapseInput == 6){

			System.out.printf("Today is %s and the future day is %s", "Thursday", "Saturday");

		}

	}


	public static void friday(){

		Scanner scanner = new Scanner(System.in);
		System.out.println("Enter the number of elapsed since today: ");
		int userElapseInput = scanner.nextInt();

		if(userElapseInput == 0){

			System.out.printf("Today is %s and the future day is %s", "Friday", "Sunday");

		}

		if(userElapseInput == 1){

			System.out.printf("Today is %s and the future day is %s", "Friday", "Monday");

		}

		if(userElapseInput == 2){

			System.out.printf("Today is %s and the future day is %s", "Friday", "Tuesday");

		}

		if(userElapseInput == 3){

			System.out.printf("Today is %s and the future day is %s", "Friday", "Wednesday");

		}

		if(userElapseInput == 4){

			System.out.printf("Today is %s and the future day is %s", "Friday", "Thursday");

		}

		if(userElapseInput == 5){

			System.out.printf("Today is %s and the future day is %s", "Friday", "Friday");

		}

		if(userElapseInput == 6){

			System.out.printf("Today is %s and the future day is %s", "Friday", "Saturday");

		}

	}

	public static void saturday(){

		Scanner scanner = new Scanner(System.in);
		System.out.println("Enter the number of elapsed since today: ");
		int userElapseInput = scanner.nextInt();

		if(userElapseInput == 0){

			System.out.printf("Today is %s and the future day is %s", "Saturday", "Sunday");

		}

		if(userElapseInput == 1){

			System.out.printf("Today is %s and the future day is %s", "Saturday", "Monday");

		}

		if(userElapseInput == 2){

			System.out.printf("Today is %s and the future day is %s", "Saturday", "Tuesday");

		}

		if(userElapseInput == 3){

			System.out.printf("Today is %s and the future day is %s", "Saturday", "Wednesday");

		}

		if(userElapseInput == 4){

			System.out.printf("Today is %s and the future day is %s", "Saturday", "Thursday");

		}

		if(userElapseInput == 5){

			System.out.printf("Today is %s and the future day is %s", "Saturday", "Friday");

		}

		if(userElapseInput == 6){

			System.out.printf("Today is %s and the future day is %s", "Saturday", "Saturday");

		}

	}
}