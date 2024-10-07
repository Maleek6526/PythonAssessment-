def single_filers():
	user_input = float(input("You claimed to be a single, please do enter your taxable income:  "))
	if user_input > 0:
		balance = user_input - 8350
		at_10 = (10 / 100) * 8350
		print(at_10)
		return at_10
		if balance > 0:
			new_balance = (15 / 100) * balance
			addition = at_10 + new_balance
			print(addition)
		return addition


def married_filing_jointly():
	user_input = float(input("You claimed to be a Married_filing_jointly, please do enter your taxable income:  "))
	if user_input > 0:
		balance = user_input - 16700
		at_10% = (10 / 100) * 16700
		print(at_10%)
		return at_10%
		if balance > 0:
			new_balance = (15 / 100) * balance
			addition = at_10% + at_15%
			print(addition)
		return addition

def married_filing_separately():
	user_input = float(input("You claimed to be a Married Filing Separately, please do enter your taxable income:  "))
	if user_input > 0:
		balance = user_input - 8350
		at_10% = (10 / 100) * 8350
		print(at_10%)
		return at_10%
		if balance > 0:
			new_balance = (15 / 100) * balance
			addition = at_10% + at_15%
			print(addition)
		return addition


def head_of_household():
	user_input = float(input("You claimed to be a Married Filing Separately, please do enter your taxable income:  "))
	if user_input > 0:
		balance = user_input - 11950
		at_10% = (10 / 100) * 11950
		print(at_10%)
		return at_10%
		if balance > 0:
			new_balance = (15 / 100) * balance
			addition = at_10% + at_15%
			print(addition)
		return addition

			
			
		


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
		case 0: single_filers() break
		case 1: married_filing_jointly() break
		case 2: married_filing_separately() break
		case 3: head_of_household() break
		case _: print("Please follow the rules")

main()


