'''
1. write a function named divide_or_square
2. The function should take in number as parameter
3. if the number is divisible by 5, the function should return the numbers squareroot
4. else it should return the remainder when divided by 5
5. Handle potential edge cases like negative number and non integer inputs.

'''
import math

def divide_or_square(number):		
	if type(number)!= 'int':
		return 0

	if number > 0:
		if number % 5 == 0:
			return math.sqrt(number)
		else:
			remainder = number % 5
			return remainder


user_input = input("Enter a number: ")
print(divide_or_square(user_input))
	