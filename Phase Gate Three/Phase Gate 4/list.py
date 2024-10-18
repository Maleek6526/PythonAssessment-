userInput = int(input("Enter the number of rows: "))
userInput2 = int(input("Enter the number of column: "))
list = [[0] * userInput] * userInput2

for row in range(len(list)):
	for column in range(len(list[row])):
		print(list[row][column], end = ' ')
	print()