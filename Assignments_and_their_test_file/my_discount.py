'''
step 1: write a unction called my_discount
step 2: the function should take in 2 parameters
step 3: the function should calculate the discount nd store in a varriable called final_price
step 4: return final_price
'''


def my_discount(price, discount):
	final_price = price - ((discount / 100) * price)
	return final_price