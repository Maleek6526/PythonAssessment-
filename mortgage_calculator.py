"""
import math to able to access the method math.pow
prompt the user to enter the principal amount and save as principal
prompt the user to enter the annual interest rate and save as annual interest rate
prompt the user to enter the duration in years and save as duration in years
multiply the duration in years by number of months which is 12 and save it in a variable called duration
divide the annual interest rate by percentage and save in a variable called annual interest
divide the annual interest rate by number of months which is 12 and save in a variable called monthly interest rate
add 1 plus the monthly interest rate and save in a variable called monthly payment 1
do monthly payment 1 to be raise to power duration and save in a variable called monthly payment 2
multiply monthly interest rate and monthly payment 2 and save in a variable called monthly payment 3
do the difference between monthly payment 2 and 1 and save in a variable called monthly payment 4
divide monthly payment 3 by monthly payment 4 and save in a variable called division result
multiply the principal by division result and save in a variable called multiplication
round the variable multiply to 2 decimal places and save in a variable rounded number
print out the random number


"""


import math

principal = float(input("Enter the Principal Amount: "))
annual_interest_rate = float(input("Enter the Annual Interest Rate: "))
duration_in_years = float(input("Enter the Duration In years: "))


duration = duration_in_years * 12
annual_interest =  annual_interest_rate / 100
monthly_interest_rate = annual_interest /12

monthly_payment_1 = (1 + monthly_interest_rate)
monthly_payment_2 = math.pow(monthly_payment_1, duration)
monthly_payment_3 = monthly_interest_rate * monthly_payment_2

monthly_payment_4 = monthly_payment_2 - 1
division_result = monthly_payment_3 / monthly_payment_4
multiplication = principal * division_result 
number = multiplication
rounded_number = round(number,2)

print(f"Your monthly payment is ${rounded_number}")