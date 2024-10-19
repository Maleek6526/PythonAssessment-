'''
def ascending_order(list):
	for count in range(1, len(list)):
		for counter in range(1, len(list)):
			if list[counter-1] > list[counter]:
				temp = list[counter-1]
				list[counter-1] = list[counter]
				list[counter] = temp

	return list

def decending_order(list):
	for count in range(1, len(list)):
		for counter in range(1, len(list)):
			if list[counter-1] < list[counter]:
				temp = list[counter-1]
				list[counter-1] = list[counter]
				list[counter] = temp

	return list
'''
def get_product(list):
	pro = 1
	for count in range(2, len(list), 3):
		print(count)
		pro *= list[count]
	return pro


list = [5, 2, 7, 1, 8, 2]

#print(ascending_order(list))

#print(decending_order(list))

print(get_product(list))	