'''

prompt the user to enter an integer for today's day of the week
prompt the user to enter the number of days after today for a future day ahead
create the days of the week
make Sunday as 0, Monday as 1 ... Saturday as 6
display the future day of the week
'''


def sunday():
	userElapseInput = int(input("Enter the number of elapsed since today: "))
	if userElapseInput == 0:
		print(f"Today is {"Sunday"} and the future day is {"Sunday"}")

	if userElapseInput == 1:
		print(f"Today is {"Sunday"} and the future day is {"Monday"}")

	if userElapseInput == 2:
		print(f"Today is {"Sunday"} and the future day is {"Tuesday"}")
	
	if userElapseInput == 3:
		print(f"Today is {"Sunday"} and the future day is {"Wednesday"}")

	if userElapseInput == 4:
		print(f"Today is {"Sunday"} and the future day is {"Thursday"}")

	if userElapseInput == 5:
		print(f"Today is {"Sunday"} and the future day is {"Friday"}")

	if userElapseInput == 6:
		print(f"Today is {"Sunday"} and the future day is {"Saturday"}")




def monday():
	userElapseInput = int(input("Enter the number of elapsed since today: "))
	if userElapseInput == 0:
		print(f"Today is {"Monday"} and the future day is {"Sunday"}")

	if userElapseInput == 1:
		print(f"Today is {"Monday"} and the future day is {"Monday"}")

	if userElapseInput == 2:
		print(f"Today is {"Monday"} and the future day is {"Tuesday"}")
	
	if userElapseInput == 3:
		print(f"Today is {"Monday"} and the future day is {"Wednesday"}")

	if userElapseInput == 4:
		print(f"Today is {"Monday"} and the future day is {"Thursday"}")

	if userElapseInput == 5:
		print(f"Today is {"Monday"} and the future day is {"Friday"}")

	if userElapseInput == 6:
		print(f"Today is {"Monday"} and the future day is {"Saturday"}")



def tuesday():
	userElapseInput = int(input("Enter the number of elapsed since today: "))
	if userElapseInput == 0:
		print(f"Today is {"Tuesday"} and the future day is {"Sunday"}")

	if userElapseInput == 1:
		print(f"Today is {"Tuesday"} and the future day is {"Monday"}")

	if userElapseInput == 2:
		print(f"Today is {"Tuesday"} and the future day is {"Tuesday"}")
	
	if userElapseInput == 3:
		print(f"Today is {"Tuesday"} and the future day is {"Wednesday"}")

	if userElapseInput == 4:
		print(f"Today is {"Tuesday"} and the future day is {"Thursday"}")

	if userElapseInput == 5:
		print(f"Today is {"Tuesday"} and the future day is {"Friday"}")

	if userElapseInput == 6:
		print(f"Today is {"Tuesday"} and the future day is {"Saturday"}")



def wednesday():
	userElapseInput = int(input("Enter the number of elapsed since today: "))
	if userElapseInput == 0:
		print(f"Today is {"Wednesday"} and the future day is {"Sunday"}")

	if userElapseInput == 1:
		print(f"Today is {"Wednesday"} and the future day is {"Monday"}")

	if userElapseInput == 2:
		print(f"Today is {"Wednesday"} and the future day is {"Tuesday"}")
	
	if userElapseInput == 3:
		print(f"Today is {"Wednesday"} and the future day is {"Wednesday"}")

	if userElapseInput == 4:
		print(f"Today is {"Wednesday"} and the future day is {"Thursday"}")

	if userElapseInput == 5:
		print(f"Today is {"Wednesday"} and the future day is {"Friday"}")

	if userElapseInput == 6:
		print(f"Today is {"Wednesday"} and the future day is {"Saturday"}")


def thursday():
	userElapseInput = int(input("Enter the number of elapsed since today: "))
	if userElapseInput == 0:
		print(f"Today is {"Thursday"} and the future day is {"Sunday"}")

	if userElapseInput == 1:
		print(f"Today is {"Thursday"} and the future day is {"Monday"}")

	if userElapseInput == 2:
		print(f"Today is {"Thursday"} and the future day is {"Tuesday"}")
	
	if userElapseInput == 3:
		print(f"Today is {"Thursday"} and the future day is {"Wednesday"}")

	if userElapseInput == 4:
		print(f"Today is {"Thursday"} and the future day is {"Thursday"}")

	if userElapseInput == 5:
		print(f"Today is {"Thursday"} and the future day is {"Friday"}")

	if userElapseInput == 6:
		print(f"Today is {"Thursday"} and the future day is {"Saturday"}")

def friday():
	userElapseInput = int(input("Enter the number of elapsed since today: "))
	if userElapseInput == 0:
		print(f"Today is {"Friday"} and the future day is {"Sunday"}")

	if userElapseInput == 1:
		print(f"Today is {"Friday"} and the future day is {"Monday"}")

	if userElapseInput == 2:
		print(f"Today is {"Friday"} and the future day is {"Tuesday"}")
	
	if userElapseInput == 3:
		print(f"Today is {"Friday"} and the future day is {"Wednesday"}")

	if userElapseInput == 4:
		print(f"Today is {"Friday"} and the future day is {"Thursday"}")

	if userElapseInput == 5:
		print(f"Today is {"Friday"} and the future day is {"Friday"}")

	if userElapseInput == 6:
		print(f"Today is {"Friday"} and the future day is {"Saturday"}")



def saturday():
	userElapseInput = int(input("Enter the number of elapsed since today: "))
	if userElapseInput == 0:
		print(f"Today is {"Saturday"} and the future day is {"Sunday"}")

	if userElapseInput == 1:
		print(f"Today is {"Saturday"} and the future day is {"Monday"}")

	if userElapseInput == 2:
		print(f"Today is {"Saturday"} and the future day is {"Tuesday"}")
	
	if userElapseInput == 3:
		print(f"Today is {"Saturday"} and the future day is {"Wednesday"}")

	if userElapseInput == 4:
		print(f"Today is {"Saturday"} and the future day is {"Thursday"}")

	if userElapseInput == 5:
		print(f"Today is {"Saturday"} and the future day is {"Friday"}")

	if userElapseInput == 6:
		print(f"Today is {"Saturday"} and the future day is {"Saturday"}")

def the_main():
	userInput = int(input("Enter Today's day: "))

	match userInput:
		case 0: sunday() 
		case 1: monday()
		case 2: tuesday()
		case 3: wednesday()
		case 4: thursday()
		case 5: friday()
		case 6: saturday()
		case _: print("Invalid input")




the_main()
























