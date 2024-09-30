'''
prompt the user to enter three integers
display then in decreasing order

'''


first_user_input = int(input("Enter the first number: "))
second_user_input = int(input("Enter the first number: "))
third_user_input = int(input("Enter the first number: "))

if first_user_input < second_user_input and first_user_input < third_user_input and second_user_input < third_user_input:
	print(f"{first_user_input},{second_user_input},{third_user_input}")

if second_user_input < first_user_input and second_user_input < third_user_input and first_user_input < third_user_input:
	print(f"{second_user_input},{first_user_input},{third_user_input}")

if third_user_input < first_user_input and third_user_input < second_user_input and first_user_input < second_user_input:
	print(f"{third_user_input},{first_user_input},{second_user_input}")
