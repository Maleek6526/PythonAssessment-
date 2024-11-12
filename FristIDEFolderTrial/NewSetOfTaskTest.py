import unittest
import NewSetOfTask


class NewSetOfTaskTest(unittest.TestCase):
    def test_that_list_of_integers_function_exists(self):
        list = []
        NewSetOfTask.list_of_integers(list)

    def test_that_list_of_integers_function_returns_result(self):
        list = []
        self.assertEqual(NewSetOfTask.list_of_integers(list), [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])

    def test_that_duplicateElements_function_returns_correct_result(self):
        list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
        self.assertEqual(NewSetOfTask.duplicateElements(list), [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])


    def test_that_addition_of_every_third_elements_function_returns_correct_result(self):
        list = [1,2,3,4,5,6,7,8]
        another_list = [-1,-2,-3,-4,-5,-6,-7,-8]
        self.assertEqual(NewSetOfTask.addition_of_every_third_elements(list), 16)
        self.assertEqual(NewSetOfTask.addition_of_every_third_elements(another_list), -16)
