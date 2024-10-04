'''
1. write two functions 
2. the fist function should take reverse, while the second takes palindrome
3. The first function returns a reverse number
4. The second function checks maybe the number is a palindrome or not
'''
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
