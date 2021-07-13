import unittest
from python_exercises.list_product_excluding_duplicates import ListProductExcludingDup as LP

class TestListProduct(unittest.TestCase):
    def test_empty_list(self):
        list = []
        expected = 0
        actual = LP().list_product_exc_dup(list)
        self.assertEqual(actual,expected)

    def test_list_one_entry(self):
        list = [4]
        expected = 4
        actual = LP().list_product_exc_dup(list)
        self.assertEqual(actual, expected)

    def test_multiple_entries(self):
        list = [2,4,5,4,5]
        expected = 40
        actual = LP().list_product_exc_dup(list)
        self.assertEqual(actual, expected)
