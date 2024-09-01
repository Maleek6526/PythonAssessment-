def main():
	successful_delivery_count = int(input("Enter the number of your successful delivery:"))		
	wages = successful_delivery(successful_delivery_count)

	print(f"Your wages: {wages}")

	



def successful_delivery(successful_delivery):
		
	wages = 0;
	base_pay = 5000
		
	if successful_delivery <= 50:

		amountPerParcel = 160;
		wages = successful_delivery * amountPerParcel + base_pay;	
			

	elif successful_delivery > 50 and successful_delivery <= 59:

		amountPerParcel = 200;

		wages = successfulDelivery * amountPerParcel + base_pay;


	
	elif successful_delivery >= 60 and successful_delivery <= 69:
				
		amountPerParcel = 250;

		wages = successful_delivery * amountPerParcel + base_pay;

			
	elif successful_delivery >= 70:

		amountPerParcel = 500;

		wages = successful_delivery * amountPerParcel + base_pay;

	
	
	return wages;

main()