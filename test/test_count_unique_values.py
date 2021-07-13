import unittest
from python_exercises.count_unique_values import count_unique_values as cnt

class TestCountUniqueValues(unittest.TestCase):
    def test_one_element(self):
        testList = [1]
        expected = 1
        actual = cnt().count_unique_values(testList)
        self.assertEqual(actual, expected)

    def test_five_elements(self):
        testList = [1,1,1,1,1]
        expected = 1
        actual = cnt().count_unique_values(testList)
        self.assertEqual(actual, expected)

    def test_four_unique_elements(self):
        testList = [1,3,2,4,1]
        expected = 4
        actual = cnt().count_unique_values(testList)
        self.assertEqual(actual, expected)

    def test_empty_array(self):
        testList = []
        expected = 0
        actual = cnt().count_unique_values_using_counter(testList)
        self.assertEqual(actual, expected)

    def test_one_element_Counter(self):
        testList = [1]
        expected = 1
        actual = cnt().count_unique_values_using_counter(testList)
        self.assertEqual(actual, expected)

    def test_five_elements_Counter(self):
        testList = [1,1,1,1,1]
        expected = 1
        actual = cnt().count_unique_values_using_counter(testList)
        self.assertEqual(actual, expected)

    def test_four_unique_elements_Counter(self):
        testList = [1,3,2,4,1]
        expected = 4
        actual = cnt().count_unique_values_using_counter(testList)
        self.assertEqual(actual, expected)

    def test_empty_array_Counter(self):
        testList = []
        expected = 0
        actual = cnt().count_unique_values_using_counter(testList)
        self.assertEqual(actual, expected)