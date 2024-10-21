import string
import random

def generated_password():

	my_string = string.ascii_lowercase
	my_string_2 = string.punctuation
	my_string_3 = string.digits
	my_string_4 = string.ascii_uppercase

	list = []

	password = []

	for i in range(4):
		lower_case = random.choice(my_string)
		punctuation = random.choice(my_string_2)
		digits = random.choice(my_string_3)
		upper_case = random.choice(my_string_4)
	
		list.append(punctuation)
		list.append(lower_case)
		list.append(upper_case)
		list.append(digits)
	
	return ''.join(list)


print(generated_password())