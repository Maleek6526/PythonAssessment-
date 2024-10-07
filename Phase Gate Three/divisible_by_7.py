'''
1. Allow input from the console
2. Save the input
3. Check if the number is divisible by 7
'''


numbers = int(input("Enter number: "))
number_check = 7
if numbers % number_check == 0:
	print("It is divisible by 7")
else:
	print("It is not divisible by 7")