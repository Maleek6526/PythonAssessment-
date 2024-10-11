investment_amount = float(input("Enter the investment amount: "))
number_of_years = int(input("Enter the number of years: "))
percentage = int(input("Enter the percentage: "))

print(f"Years \t Interest \t Amount")



for count in range(1, number_of_years+1):

	interest_rate = (10/100) * investment_amount
	balance = investment_amount + interest_rate

	print(f"{count}\t {interest_rate:,.2f}\t{balance:,.2f}")

	investment_amount = balance