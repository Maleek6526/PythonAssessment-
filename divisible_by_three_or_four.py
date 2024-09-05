counter = 0
count = 100
for count in range(100,200):
	if count % 3 == 0 or count % 4 == 0:
		print(f"{count}",end = " ")
		count+=1
		counter+=1

	if counter % 10 == 0:
		print(" ")








