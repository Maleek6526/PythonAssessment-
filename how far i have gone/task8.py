count = 0
counter = 0
while True:
	user_input = int(input("Enter score: "))
	if user_input >= 0 and user_input <= 100:
		counter += user_input
		count += 1

	if count == 10:
		print(counter) 
		break





		
		
	

