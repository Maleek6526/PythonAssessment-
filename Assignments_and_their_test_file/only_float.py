'''
step 1: write a function called only_float
step 2: the function should take in two parameters
step 3: the function should check if the 2 parameters are of type float 
step 4: if the 2 parameters are of type float then the function should return 2
step 5: if 1 of the  parameters is of type float then the function should return 1
step 6: if none of the parameters are of type float then the function should return 0

'''


def only_float(num , decimal):
	if isinstance(num , float) and isinstance(decimal, float):
		return 2
	elif isinstance(num , float) or isinstance(decimal, float):
		return 1
	else:	return 0