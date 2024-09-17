count = 0
counter = 0
while True:
	user_input = int(input("Enter score: "))
	if user_input >= 0 or user_input <= 100:
		count+=1
		counter += user_input

	if count == 10:
		print(counter) 
		break


