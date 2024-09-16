'''
step 1: create a function called palindrome
step 2: the palindrome function takes in a number
step 3: calculate the palindrome in the function and store as reverse
step 4: check if the number is equal to the reversed number, then return "it is a palindrome". else return "it is not a palindrome"

step 1: create a function called prime
step 2: the function should take in a number 
step 3: check if the inputted number is a prime number
step 4: if the number is a prime number return true, else return false

step 1: create a function called palindrome_prime
step 2: the function will take in a number as the parameter
step 3: the palindrome function and the prime function should be called in this function 
step 4: this function will check if the two conditions have been met
step 5: if the condition is been met it retuns true, else it returns false

'''




def palindrome(number):
	reverse = 0
	original_number = number
	while number != 0:
		reverse = reverse * 10 + number % 10
		number = number // 10
	if original_number == reverse:
		return "its a palindrome"
	else: return "its not a palindrome"


def prime(number):
	original_number = number
	if number <= 1:
		return False
	for prime in range(2, int(number ** 0.5) + 1):
		if original_number % prime == 0:
			return False
	return True



def palindrome_prime(number):
	return palindrome(number) and prime(number) 
