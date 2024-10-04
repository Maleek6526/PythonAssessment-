def reverse(numbers):
	reverse_number = ''
	for number in range(len(numbers)-1, -1, -1):
		reverse_number += numbers[number]
	return reverse_number		


def palindrome(user_input):
	reversed_number = reverse(user_input)
	if user_input == reversed_number:
		print("This number is a palindrome")
	else:
		print("This is not a palindrome")

data = input("Enter a number: ")
print(palindrome(data))
