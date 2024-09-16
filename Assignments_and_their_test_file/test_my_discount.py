import unittest
import my_discount

class Testmy_discount(unittest.TestCase):
	def test_that_my_discount_function_exist(self):
		my_discount.my_discount(10, 5)

	def test_that_my_discount_function_returns_result(self):
		self.assertEqual(my_discount.my_discount(150, 15), 127.5)

	def test_that_function_raises_type_error_with_strings_value(self):
		self.assertRaises(TypeError, my_discount.my_discount, "Maleek")


