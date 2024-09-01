import math

def get_slices_per_box(pizza_type):
	match pizza_type:
		case 1: return 4
		case 2: return 6
		case 3: return 8
		case 4: return 12
		case _: return 0

def get_price_per_box(pizza_type):
	match pizza_type:
		case 1: return 2000
		case 2: return 2400
		case 3: return 3000
		case 4: return 4200
		case _: return 0


def calculate_number_of_boxes(number_of_people, slices_per_box):
	division = number_of_people / slices_per_box
	return math.ceil(division)


def calculate_left_over_slices(number_of_people, slices_per_box, number_of_boxes):
	total_slices = number_of_boxes * slices_per_box
	return total_slices - number_of_people


def calculate_total_price(number_of_boxes, price_per_box):
        return number_of_boxes * price_per_box


def display_results(number_of_boxes, left_over_slices, total_price):
	print(f"Number of boxes to buy = {number_of_boxes} boxes")
	print(f"Number of Leftover slices = {left_over_slices} slices")
	print(f"Total price = {total_price}")

number_of_people = int(input("Enter the number of people: "))
pizza_type = int(input("Enter the pizza type (1 -> Sapa size, 2 -> Small Money,3 -> Big boys, 4 -> Odogwu): "))
slices_per_box = get_slices_per_box(pizza_type)
price_per_box = get_price_per_box(pizza_type)
number_of_boxes = calculate_number_of_boxes(number_of_people, slices_per_box)
left_over_slices = calculate_left_over_slices(number_of_people, slices_per_box, number_of_boxes)
total_price = calculate_total_price(number_of_boxes, price_per_box)
display_results(number_of_boxes, left_over_slices, total_price)

