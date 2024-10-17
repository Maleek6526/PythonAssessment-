def get_swapped(number):
	for i in range(1, len(number)+1):
		if i % 2 != 0:
			temp = number[i]
			number[i] = number[i-1]
			number[i-1] = temp
	return number 