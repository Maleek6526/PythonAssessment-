try:
	userInput = int(input("Enter the number of rows: "))
	userInput2 = int(input("Enter the number of column: "))

	if userInput > 0 and userInput2 > 0:
		list = [[0] * userInput] * userInput2

		for row in range(len(list)):
			for column in range(len(list[row])):
				list[row][column] = row * column
				print(f"{list[row][column]} \t", end = ' ')
			print()

	else:
		print("Input a valid number")
except:
	print("Invalid input")