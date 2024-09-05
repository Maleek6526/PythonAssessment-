user_input = int(input("Enter a four digit integer: "))

first_number = user_input // 1000
last_number = user_input % 10
third_number = user_input // 10
final_third_number = third_number % 10
second_number = third_number // 10
final_second_number = second_number % 10

print(f"The number you inputed is: {first_number}{final_second_number}{final_third_number}{last_number}")

first_digit = (first_number+7)%10
second_digit = (final_second_number+7)%10
third_digit = (final_third_number+7)%10
fourth_digit = (last_number+7)%10

print(f"Encrypted = {third_digit}{fourth_digit}{first_digit}{second_digit}")

