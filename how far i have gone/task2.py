sum_of_scores = 0
counter = 0
for score in range(1, 11):
	score = int(input("Enter your score: "))
	sum_of_scores += score
	counter+=1
average = sum_of_scores / counter
print(average)