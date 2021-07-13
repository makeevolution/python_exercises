import unittest
from python_exercises.change_first_last_element import swap_first_last

class test_change_first_last(unittest.TestCase):
    def test_one_element(self):
        self.assertEqual([1], swap_first_last().swap_first_last([1]))

    def test_two_elements(self):
        self.assertEqual([2, 1], swap_first_last().swap_first_last([1, 2]))

