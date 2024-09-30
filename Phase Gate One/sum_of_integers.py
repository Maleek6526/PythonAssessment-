'''
write a program that reads the numbers only from range 0 to 1000
prompt the user for input
if the number inputted is lower than zero or higher than 1000, display numbers at this range is not allowed
if the number inputted is at the range, calculate the sum of the number
display the sum
'''

user_input = int(input("Enter an integer number starting from range 0 to 1000: "))

if user_input < 0 or user_input > 1000:
	print("Numbers at this range is not allowed")

reverse = 0

sum_of_the_numbers = 0
while user_input != 0:
	sum_of_the_numbers += user_input % 10	
	user_input = user_input // 10	
print(sum_of_the_numbers)
