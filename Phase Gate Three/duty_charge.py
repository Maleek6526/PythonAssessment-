'''
1. Allow input from the console
2. Save the input as cost of the car
3. print out the duty charge to be paid
'''

cost_of_the_car = int(input("Enter the cost of the car: "))
if cost_of_the_car > 0:
	if cost_of_the_car < 2500000:
		duty_charge = (5 / 100) * cost_of_the_car
		print(duty_charge)
	elif cost_of_the_car >= 2500000 and cost_of_the_car <= 5000000:
		duty_charge = (10 / 100) * cost_of_the_car
		print(duty_charge)
	elif cost_of_the_car >= 5000000 and cost_of_the_car <= 10000000:
		duty_charge = (15 / 100) * cost_of_the_car
		print(duty_charge)
	elif cost_of_the_car > 10000000:
		duty_charge = (20 / 100) * cost_of_the_car
		print(duty_charge)
else:
	print("Invalid")