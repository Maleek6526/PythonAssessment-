'''
1. create a function that takes two integer as a string
2. trun them to integer
3. find the sum of the two integers
4. retun the sum as string 
'''


def number_to_string(input_one, input_two):
	number_one = int(input_one)
	number_two = int(input_two)
	addition = number_one + number_two
	my_string = str(addition)
	return my_string

first_input = input("Enter the first input: ")
second_input = input("Enter the second input: ")
print(number_to_string(first_input, second_input))