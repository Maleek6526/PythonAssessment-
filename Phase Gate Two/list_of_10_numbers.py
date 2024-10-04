'''
1. Write a python program that create a list of 10 numbers between 1 and 50
2. Get length of a list without using len function
3. Sum up all the element at even positions
4. Sum up all the elements at odd positions
5. Multiply all element at every third positions
6. calculate the average of all elements in the list


'''


import random

first = random.randrange(1, 50)
second = random.randrange(1, 50)
third = random.randrange(1, 50)
fourth = random.randrange(1, 50)
fifth = random.randrange(1, 50)
sixth = random.randrange(1, 50)
seventh = random.randrange(1, 50)
eight = random.randrange(1, 50)
nineth = random.randrange(1, 50)
tenth = random.randrange(1, 50)

array = [first, second, third, fourth, fifth, sixth, seventh, eight, nineth, tenth]
print(array)

addition = 0
for i in range(10):
	addition += array[i]


count = i + 1
average = addition / count
	
print("The average is ",average)
