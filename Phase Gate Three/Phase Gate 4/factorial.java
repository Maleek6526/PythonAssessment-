def factorial(data):
	numbers = 1
	for count in range(data):
		numbers = numbers * (data - count)
		collections = numbers		
	return numbers

number = 5
print(factorial(number))
