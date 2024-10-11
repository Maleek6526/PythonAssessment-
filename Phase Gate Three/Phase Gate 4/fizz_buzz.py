for counter in range(1, 51):
	displayer = ""
	if counter % 3 == 0:
		displayer = "fizz"
		print(displayer, end = ' ')
		continue
	if counter % 5 == 0:
		displayer = "buzz"
		print(displayer, end = ' ')
		continue
	if counter % 3 == 0 and counter % 5 == 0:
		displayer = "FizzBuzz"
		print(displayer, end = ' ')
		continue
	print(counter, end = ' ')