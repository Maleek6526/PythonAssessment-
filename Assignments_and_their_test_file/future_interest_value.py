'''
step 1: create a function called future_interest_value
step 2: the function should take in 3 parameters
step 3: the inputted parameters should be calculated in the function with formula
step 4: the function should return the future interest value
'''





def future_interest_value(investment_amount, monthly_interest_rate, years):
	addition = 1
	number_of_months = 12
	future_interest_value = investment_amount*(addition + monthly_interest_rate)**(years*number_of_months)
	return round(future_interest_value, 2)