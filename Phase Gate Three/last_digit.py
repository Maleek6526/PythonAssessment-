'''
1. Allow input from the console
2. Save the input
3. Write a program that display the last digit of a number inputtesd from the console
'''

numbers = int(input("Enter number: "))
count = 0
counter_increment = 1
reverser_number = 10
while numbers != 0:
	last_digit = numbers % reverser_number
	count+=1
	if count == counter_increment:
		break

print(last_digit)