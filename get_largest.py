def get_largest():
	users_choice = int(input("Enter how many numbers you want to input: "))
	numbers_of_arrays = [0] * users_choice

	for count in range(users_choice):
		numbers_of_arrays[count] = int(input(f"Enter number for position {count + 1}: "))

	largest = numbers_of_arrays[0]

	for count in range(users_choice):
		if numbers_of_arrays[count] > largest:
			largest = numbers_of_arrays[count]
	print(largest)

get_largest()
