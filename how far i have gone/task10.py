count = 0
average_counter = 0
average = 0
for counter in range(1, 11):
	score = int(input("Enter Score: "))
	count+=score
average = count / counter
print(average)