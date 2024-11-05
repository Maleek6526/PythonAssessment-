list = [2, 4, 1, 5, 6, 7]
list_two = [3, 8, 7, 2, 5, 1]
array = []
array_two = []

for i in range(1, len(list), 2):
	array.append(list[i-1] + list[i])

	array_two.append(list_two[i-1] + list_two[i])


print(array)
print(array_two)
