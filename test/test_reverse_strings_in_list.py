import unittest
from python_exercises.reverse_strings_in_list import ReverseStringsInList as RS

class TestListProduct(unittest.TestCase):
    def test_empty_list(self):
        list = []
        expected = []
        actual = RS().reverse_strings(list)
        self.assertEqual(expected,actual)

    def test_list_5_entries(self):
        list = ['geeks', 'for', 'geeks', 'is', 'best']
        expected = ['skeeg', 'rof', 'skeeg', 'si', 'tseb']
        actual = RS().reverse_strings(list)
        self.assertEqual(expected, actual)

    def test_number_strings(self):
        list = ['2','5','5']
        expected = list
        actual = RS().reverse_strings(list)
        self.assertEqual(expected, actual)
