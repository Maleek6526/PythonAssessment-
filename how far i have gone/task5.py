counter = 0
sum_of_even_only = 0
for score in range(1, 11):
	score = int(input("Enter your score: "))
	if score % 2 == 0:
		sum_of_even_only += score
print(sum_of_even_only)