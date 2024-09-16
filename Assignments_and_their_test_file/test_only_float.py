import unittest
import only_float

class Testonly_float(unittest.TestCase):
	def test_that_only_float_function_exist(self):
		only_float.only_float(10, 10)

	def test_that_only_float_function_returns_result(self):
		self.assertEqual(only_float.only_float(12.1, 23.4), 2)
		self.assertEqual(only_float.only_float(12.1, 23), 1)
		self.assertEqual(only_float.only_float(12, 23), 0)
	
	def test_that_function_raises_type_error_with_strings_value(self):
		self.assertRaises(TypeError, only_float.only_float, "Maleek")
