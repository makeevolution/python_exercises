import unittest

# Demonstrates that the rules of sorted can be customized
# using key = lambda. The below sorts a list of strings
# based on the second letter in the string

class SortDictionary():
    def sort_dictionary_by_age(self,lis):
        return sorted(lis, key = lambda i:i[2])

class TestSortDictionary(unittest.TestCase):
    def test_sort_by_age(self):
        lis = ["poxox",
               "pocox",
               "ponox"]
        expected = ["pocox",
               "ponox",
               "poxox"]
        actual = SortDictionary().sort_dictionary_by_age(lis)
        self.assertEqual(expected,actual)
