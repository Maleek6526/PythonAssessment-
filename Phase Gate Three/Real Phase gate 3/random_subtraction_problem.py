'''
1. Generate two diffenet random numbers
2. Make the user solve the subtraction of the two numbers
3. Allow the number to keep changing after every attempt either right or wrong
4. Pring the user score
'''
import random

count = 1

wrong_answer = 0

right_answer = 0

while count <= 10:

	random_guesses_1 = random.randrange(50, 100)
	random_guesses_2 = random.randrange(1, 50)

	print(f"{random_guesses_1} - {random_guesses_2} = ")

	users_answer = int(input(""))

	if users_answer < 0:
		print("You could have inputted a positive number you know!")
		break

	else:

		answer_check = random_guesses_1 - random_guesses_2

		if users_answer == answer_check:
			print("Correct!")
			right_answer+=1
		else:
			print("Wrong!")
			wrong_answer+=1
			count+=1

print(f"You got the answer {right_answer} times, while you missed the answer {wrong_answer} times")
print(f"So you got {right_answer} / {10}")