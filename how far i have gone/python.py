import random
user_input = int(input("Enter a number: "))
arr = []
print(arr)
for i in range(user_input):
	arr.append(random.randint(1, 1000))
print(arr)