number = 5
for count in range(1, number+1):
	
	for counter in range(1, count):
		if counter % 2 == 0:
			print("*", end = ' ')
		else:
			print(counter, end = ' ')
	print(" ")

number = 5
for count in range(number+1, 1, -1):
	
	for counter in range(1, count):
		if counter % 2 == 0:
			print("*", end = ' ')
		else:
			print(counter, end = ' ')
	print(" ")