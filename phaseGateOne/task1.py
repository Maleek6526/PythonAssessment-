'''
write a code that generates two integer
the range of the number should be between 0 to 100
prompt the user to guess the sum of the two integers
if the user got it right, display answer is correct
if the user got it wrong, display false
'''



import random
first_random_number = random.randint(0, 100)
second_random_number = random.randint(0, 100)

userGuesses = int(input("Guess the sum of the two integers: "))

sum_of_the_random_numbers = first_random_number + second_random_number

if userGuesses != sum_of_the_random_numbers:
	print("False")

if userGuesses == sum_of_the_random_numbers:
	print("Answer is correct!")


