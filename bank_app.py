balance = 0
while True:
	print("Enter \n 1 for deposit \n 2 to withdraw \n 3 for balance")
	user_input = int(input(""))
	if user_input == 1:
		amount = int(input("Enter the amount you want to deposit: "))
		balance+=amount

	if user_input == 2:
		withdraw = int(input("Enter the amount you want to withdraw: "))
		if balance < withdraw:
			print("Insufficient funds")

		else: balance -= withdraw

	if user_input == 3:
		print("Your balance is ", balance)
