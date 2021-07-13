import unittest
from python_exercises.add_space_between_words import AddSpaceBetweenWords as AS

class TestListProduct(unittest.TestCase):
    def test_empty_list(self):
        list = []
        expected = []
        actual = AS().add_space(list)
        self.assertEqual(expected,actual)

    def test_list_5_entries(self):
        list = ['gfgBest', 'forGeeks', 'andComputerScienceStudents']
        expected = ['gfg Best', 'for Geeks', 'and Computer Science Students']
        actual = AS().add_space(list)
        self.assertEqual(expected, actual)

    def test_one_entry(self):
        list =  ['ComputerScienceStudentsLoveGfg']
        expected = ['Computer Science Students Love Gfg']
        actual = AS().add_space(list)
        self.assertEqual(expected, actual)
