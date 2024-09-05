def christmas_song_menu():

	print(""" 

		++++++++++++++++++++++++++++++++		
		Welcome to My Christmas Song App

		please press 1 to 12 to continue...
		+++++++++++++++++++++++++++++++

		""")

	users_choice = int(input("Type in me: "))
	
	match users_choice:
		case 1: day_one()
		case 2: day_two()
		case 3: day_three()
		case 4: day_four()
		case 5: day_five()
		case 6: day_six()
		case 7: day_seven()
		case 8: day_eight()
		case 9: day_nine()
		case 10: day_ten()
		case 11: day_eleven()
		case 12: day_twelve()
		case 0: exit()
		case _: print("Oga Get Sense Abeggi!!!")


def day_one():
	print("""
		On the first day of Christmas, my true love gave to me

			1.	A partridge in a pear tree.

			0.	To go back
				
		""")

	users_choice = int(input("Type in me: "))

	match users_choice:
		case 0: christmas_song_menu()
		case _: print("Oga Get Sense Abeggi!!!")



def day_two():
	print("""

		On the second day of Christmas,my true love gave to me

			2.	Two turtle doves,

			1.	And a partridge in a pear tree.

			0.	To go back

				
		""")

	users_choice = int(input("Type in me: "))

	match users_choice:
		case 0: christmas_song_menu()
		case _: print("Oga Get Sense Abeggi!!!")



def day_three():
	print("""
		On the third day of Christmas,my true love gave to me

			3.	Three French hens,

			2. 	Two turtle doves,

			1.	And a partridge in a pear tree.

			0.	To go back

			""")

	users_choice = int(input("Type in me: "))

	match users_choice:
		case 0: christmas_song_menu()
		case _: print("Oga Get Sense Abeggi!!!")



def day_four():
	print("""
		On the fourth day of Christmas,my true love gave to me

			4.	Four calling birds,

			3.	Three French hens,

			2.	Two turtle doves,

			1.	And a partridge in a pear tree.

			0.	To go back

			""")

	users_choice = int(input("Type in me: "))

	match users_choice:
		case 0: christmas_song_menu()
		case _: print("Oga Get Sense Abeggi!!!")




def day_five():
	print("""
		On the fifth day of Christmas,my true love gave to me

			5.	Five golden rings,

			4.	Four calling birds,

			3.	Three French hens,

			2.	Two turtle doves,

			1.	And a partridge in a pear tree.

			0.	To go back


			""")

	users_choice = int(input("Type in me: "))

	match users_choice:
		case 0: christmas_song_menu()
		case _: print("Oga Get Sense Abeggi!!!")


def day_six():
	print("""
		
		On the sixth day of Christmas,my true love gave to me

			6.	Six geese a-laying,

			5.	Five golden rings,

			4.	Four calling birds,

			3.	Three French hens,

			2.	Two turtle doves,

			1.	And a partridge in a pear tree.

			0.	To go back

			""")

	users_choice = int(input("Type in me: "))

	match users_choice:
		case 0: christmas_song_menu()
		case _: print("Oga Get Sense Abeggi!!!")


def day_seven():
	print("""
		On the seventh day of Christmas,my true love gave to me
			
			7.	Seven swans a-swimming,
			
			6.	Six geese a-laying,

			5.	Five golden rings,

			4.	Four calling birds,

			3.	Three French hens,

			2.	Two turtle doves,

			1.	And a partridge in a pear tree.

			0.	To go back

				""")

	users_choice = int(input("Type in me: "))

	match users_choice:
		case 0: christmas_song_menu()
		case _: print("Oga Get Sense Abeggi!!!")



def day_eight():
	print(""" 

		On the eighth day of Christmas,my true love gave to me

			8.	Eight maids a-milking,

			7.	Seven swans a-swimming,

			6.	Six geese a-laying,

			5.	Five golden rings,

			4.	Four calling birds,

			3.	Three French hens,

			2.	Two turtle doves,

			1.	And a partridge in a pear tree.

			0.	To go back

			""")
	users_choice = int(input("Type in me: "))

	match users_choice:
		case 0: christmas_song_menu()
		case _: print("Oga Get Sense Abeggi!!!")


def day_nine():
	print(""" 

		On the ninth day of Christmas,my true love gave to me

			9.	Nine ladies dancing,

			8.	Eight maids a-milking,

			7.	Seven swans a-swimming,

			6.	Six geese a-laying,

			5.	Five golden rings,

			4.	Four calling birds,

			3.	Three French hens,

			2.	Two turtle doves,

			1.	And a partridge in a pear tree.

			0.	To go back

			""")
	users_choice = int(input("Type in me: "))

	match users_choice:
		case 0: christmas_song_menu()
		case _: print("Oga Get Sense Abeggi!!!")



def day_ten():
	print(""" 

		On the tenth day of Christmas,my true love gave to me

			10.	Ten lords a-leaping,

			9.	Nine ladies dancing,

			8.	Eight maids a-milking,

			7.	Seven swans a-swimming,

			6.	Six geese a-laying,

			5.	Five golden rings,

			4.	Four calling birds,

			3.	Three French hens,

			2.	Two turtle doves,

			1.	And a partridge in a pear tree.

			0.	To go back

			""")
	users_choice = int(input("Type in me: "))

	match users_choice:
		case 0: christmas_song_menu()
		case _: print("Oga Get Sense Abeggi!!!")



def day_eleven():
	print(""" 

		On the eleventh day of Christmas,my true love gave to me

			11.	Eleven pipers piping,

			10.	Ten lords a-leaping,

			9.	Nine ladies dancing,

			8.	Eight maids a-milking,

			7.	Seven swans a-swimming,

			6.	Six geese a-laying,

			5.	Five golden rings,

			4.	Four calling birds,

			3.	Three French hens,

			2.	Two turtle doves,

			1.	And a partridge in a pear tree.

			0.	To go back


			""")
	users_choice = int(input("Type in me: "))

	match users_choice:
		case 0: christmas_song_menu()
		case _: print("Oga Get Sense Abeggi!!!")

def day_twelve():
	print(""" 

		On the twelfth day of Christmas,my true love gave to me

			12.	Twelve drummers drumming,

			11.	Eleven pipers piping,

			10.	Ten lords a-leaping,

			9.	Nine ladies dancing,

			8.	Eight maids a-milking,

			7.	Seven swans a-swimming,

			6.	Six geese a-laying,

			5.	Five golden rings,

			4.	Four calling birds,

			3.	Three French hens,

			2.	Two turtle doves,

			1.	And a partridge in a pear tree!

			0.	To go back

			""")
	users_choice = int(input("Type in me: "))

	match users_choice:
		case 0: christmas_song_menu()
		case _: print("Oga Get Sense Abeggi!!!")


def exit():
	print("""
			 +++++++++++++++++++++++++++++++++++++++++++++++++++

					Exiting the App.....

				Thank You For Choosing My App.

			+++++++++++++++++++++++++++++++++++++++++++++++++++
""")





christmas_song_menu()