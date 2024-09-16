'''
Step 1: Create a function named divide_or_square
stap 2: The function should take in a number as input
step 3: check if the number inputted is divisible by 5
step 4: if the number is diviible by 5, the function should return the squareroot of the number
step 5: if the number is not divisible by 5, the function should return the remainder when the number is divided by 5
step 6: handle potential edge cases like negative numbers and non integer input.

'''








import math
def divide_or_square(number):
	if number < 0:
		raise ValueError("Invalid Number")
	if number % 5 == 0: 
		return round(math.sqrt(number),2)
	else: return number % 5