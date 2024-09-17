counter = 0
even_number = 0
for score in range(1, 11):
	score = int(input("Enter your score: "))
	counter+=1
	if counter % 2 == 0:
		even_number += score
print(even_number)