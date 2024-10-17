import unittest
import esther_task

class Testswapping(unittest.TestCase):
	def test_that_swapping_function_exist(self):
		esther_task.get_swapped([2, 1, 4, 3, 6, 5])

	def test_that_function_returns_result(self):

		lists = [1, 2, 3, 4, 5, 6]
		result = [2, 1, 4, 3, 6, 5]
		self.assertEqual(esther_task.get_swapped(lists), result)