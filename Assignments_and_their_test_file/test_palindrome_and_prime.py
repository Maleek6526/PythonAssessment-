import unittest
import palindrome_and_prime

class Testpalindrome_and_prime(unittest.TestCase):
	def test_that_palindrome_and_prime_function_exist(self):
		palindrome_and_prime.palindrome(10)

	def test_that_palindrome_function_returns_result(self):
		self.assertEqual(palindrome_and_prime.palindrome(123), "its not a palindrome")

	def test_that_prime_function_returns_result(self):
		self.assertEqual(palindrome_and_prime.prime(23), True)

	def test_that_palindrome_prime_function_returns_result(self):
		self.assertEqual(palindrome_and_prime.palindrome_prime(2), True)

	def test_that_function_raises_type_error_with_strings_value(self):
		self.assertRaises(TypeError, palindrome_and_prime.palindrome, "Maleek")

		self.assertRaises(TypeError, palindrome_and_prime.prime, "Maleek")
		self.assertRaises(TypeError, palindrome_and_prime.palindrome_prime, "Maleek")

		self.assertRaises(TypeError, palindrome_and_prime.palindrome_prime, "Maleek")


	