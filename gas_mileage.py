number_of_trips = int(input("Enter number of trips: "))
total_miles = 0
total_gallons = 0
count = 1
while count<= number_of_trips:
	miles_driven = int(input("Enter the miles driven: "))
	
	total_miles = total_miles + miles_driven
	
	gallon_used = int(input("Enter the gallon used: "))
	
	total_gallons = total_gallons + gallon_used
	
	average = miles_driven // gallon_used

	total_average = total_miles // total_gallons

	count+=1
	
	print(total_average)