counter = 0
sum_of_even_only = 0
count = 0
average = 0
for score in range(1, 11):
	score = int(input("Enter your score: "))
	if score % 2 == 0:
		sum_of_even_only += score
	count +=1
average = sum_of_even_only / count
print(average)

