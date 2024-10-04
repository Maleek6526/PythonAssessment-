'''
1. Write a program that allows input ranging from 1000 to 3000
2. print in arrays
'''


user_input = int(input("Enter a number: "))

if user_input > 999 and user_input  < 3001:
	first_digit_removal = user_input // 1000
	digit_two = user_input % 1000
	second_digit_removal = digit_two // 100
	digit_three = digit_two % 100
	third_digit_removal = digit_three // 10
	fourth_digit_removal = digit_three % 10	
else:
	print("Out of range")



if first_digit_removal % 2 == 0 and second_digit_removal % 2 == 0 and third_digit_removal % 2 == 0 and fourth_digit_removal % 2 == 0:
	arr = [first_digit_removal, second_digit_removal, third_digit_removal, fourth_digit_removal]
	print(arr)
else:
	print("Integers Inputted is not an Even number!")



