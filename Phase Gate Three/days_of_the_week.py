'''
1. Allow input from the console
2. Don"t allow a number lesser than 1 and greater than 7
3. Save the input
4. Print out the day the input falls
'''

number_of_day_check = int(input("Enter number ranging from 1 to 7:"))
if number_of_day_check >= 1 or number_of_day_check  <= 7:
	match number_of_day_check:
		case 1: print("Monday")
		case 2: print("Tuesday")
		case 3: print("Wednesday")
		case 4: print("Thursday")
		case 5: print("Friday")
		case 6: print("Saturday")
		case 7: print("Sunday")
		case _: print("Please input the correct number")
