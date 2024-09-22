import unittest
import get_largest

class Testget_largest(unittest.TestCase):
	def test_that_checks_if_get_largest_function_exist(self):
		get_largest.get_largest()
	
	def test_that_function_raises_type_error_with_strings_value(self):
		self.assertRaises(TypeError, get_largest.get_largest()
, "Maleek")