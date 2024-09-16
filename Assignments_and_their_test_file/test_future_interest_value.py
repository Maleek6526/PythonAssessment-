import unittest
import future_interest_value

class Testfuture_interest_value(unittest.TestCase):
	def test_that_checks_if_future_interest_value_function_exist(self):
		future_interest_value.future_interest_value(10, 10, 10)

	def test_that_checks_if_future_interest_value_function_returns_result(self):
		self.assertEqual(future_interest_value.future_interest_value(1000.56, 4.25, 1), 438687013077.32)
	
	def test_that_function_raises_type_error_with_strings_value(self):
		self.assertRaises(TypeError, future_interest_value.future_interest_value, "Maleek")