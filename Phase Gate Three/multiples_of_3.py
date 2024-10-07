'''
1. Display "hello" on the console
2. Allow input from the console 
3. Save the number
4. If the number is multiples of 3, print "bye"
'''

print("hello")

numbers = int(input("Enter number: "))
multiple_number = 3
if numbers % multiple_number == 0:
	print("bye")
