import unittest
import divide_or_square

class Testdivide_or_square(unittest.TestCase):
	def test_that_divide_or_square_function_exist(self):
		divide_or_square.divide_or_square(10)

	def test_that_divide_or_square_function_returns_result(self):
		self.assertEqual(divide_or_square.divide_or_square(25), 5)
		self.assertEqual(divide_or_square.divide_or_square(30), 5.48)

	def test_not_divisible_by_5(self):
		self.assertEqual(divide_or_square.divide_or_square(7), 2)
		self.assertEqual(divide_or_square.divide_or_square(8), 3)

	def test_that_divide_or_square_function_raises_error_with_negative_number(self):
		self.assertRaises(ValueError, divide_or_square.divide_or_square, -1)



	def test_that_function_raises_type_error_with_strings_value(self):
		self.assertRaises(TypeError, divide_or_square.divide_or_square, "Maleek")