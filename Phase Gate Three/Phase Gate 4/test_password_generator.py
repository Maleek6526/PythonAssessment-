import unittest
import string
import password_generator

class Testpassword_generator(unittest.TestCase):
	def test_that_divide_or_square_function_exist(self):
		password_generator.generated_password()


	def test_that_password_generator_length_exist(self):
		password_generator.generated_password()
		self.assertEqual(len(password_generator.generated_password()),16)


	def test_that_password_generator_has_uppercase(self):
		password = password_generator.generated_password()
		self.assertTrue(any(c for c in password if c in string.ascii_uppercase))


	def test_that_password_generator_has_lowercase(self):
		password = password_generator.generated_password()
		self.assertTrue(any(c for c in password if c in string.ascii_lowercase))


	def test_that_password_generator_has_digits(self):
		
		password = password_generator.generated_password()
		self.assertTrue(any(c for c in password if c in string.digits))


	def test_that_password_generator_has_symbols(self):
		
		password = password_generator.generated_password()
		self.assertTrue(any(c for c in password if c in string.punctuation))