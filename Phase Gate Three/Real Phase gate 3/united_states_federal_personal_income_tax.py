'''

'''

def Single_filers():
	user_input = float(input("You claimed to be a single, please do enter your taxable income:  "))
	if user_input > 0:
		while user_input != 0:	
			ten_percent_calculation = (10 / 100) * 8350
			user_input = user_input - 8350
			
			if user_input != 0:	
			at_15% = user_input 
			addition = at_10% + user_input
			print(addition)	
		


def main():
	print(''' 
		Welcome to the United States Federal Personal Income Tax
		@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

		Press 0 for Single Filers
		Press 1 for Married Filing Jointly
		Press 2 for Married Filing Separately
		Press 3 for Head Of Household

		@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
	''')

	users_choice  int(input("Enter your choice: "))
	match users_choice:
		case 0: Single_filers() break
		case 1: Married_filing_jointly() break
		case 2: Married_filing_separately() break
		case 3: Head_of_household() break
		case _: print("Please follow the rules")



