user_input = int(input("Enter a number: "))

count = 1
counter = 1

while count<=10:
	counter = user_input * count
	print(f" {user_input} {'*'} {count} {'='} {counter}")
	count+=1