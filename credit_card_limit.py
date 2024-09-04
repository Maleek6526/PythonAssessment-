account_number = int(input("Enter your account number: "))
balance = int(input("Enter your balance at the beginning of the month: "))
total_charges = int(input("Enter total charges: "))
total_credit = int(input("Enter your total credit: "))
credit_limit = 	int(input("Enter your credit limit: "))

new_balance = balance + total_charges - total_credit;

print(new_balance)

if new_balance > credit_limit:

	print("Credit Limit Exceeded")


