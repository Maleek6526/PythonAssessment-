import math
data = 153
data1 = str(data)
data_list = list(data1)
data_list.reverse()
total = 0
for count in list(data_list):
	num = int(count)
	total += math.pow(num,2)
	
print(data_list,total)
