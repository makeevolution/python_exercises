import unittest

class SortDictionary():
    def sort_dictionary_by_age(self,lis):
        return sorted(lis, key = lambda i:i["age"])
    def sort_dictionary_by_name(self,lis): #Ascending
        return sorted(lis, key = lambda i:i["name"], reverse = True)

class TestSortDictionary(unittest.TestCase):
    def test_sort_by_age(self):
        lis = [{"name": "Nandini", "age": 20},
               {"name": "Manjeet", "age": 20},
               {"name": "Nikhil", "age": 19}]
        expected = [{'age': 19, 'name': 'Nikhil'},
                    {'age': 20, 'name': 'Nandini'},
                    {'age': 20, 'name': 'Manjeet'}]
        actual = SortDictionary().sort_dictionary_by_age(lis)
        self.assertEqual(expected,actual)

    def test_sort_by_name(self):
        lis = [{"name": "Nandini", "age": 20},
               {"name": "Manjeet", "age": 20},
               {"name": "Nikhil", "age": 19}]
        expected = [{'age': 19, 'name': 'Nikhil'},
                    {'age': 20, 'name': 'Nandini'},
                    {'age': 20, 'name': 'Manjeet'}]
        actual = SortDictionary().sort_dictionary_by_name(lis)
        self.assertEqual(expected, actual)