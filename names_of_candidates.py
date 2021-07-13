import unittest
from collections import *
votes = ["john", "johnny", "jackie",
                    "johnny", "john", "jackie",
                    "jamie", "jamie", "john",
                    "johnny", "jamie", "johnny",
                    "john"]

class Votes(object):
    def get_most_no_of_votes(self,votes):
        votes_dict = Counter(votes)
        most_voted = [filter(lambda i : i[1] == max(votes_dict), votes_dict)]
        if len(most_voted) > 1:
            pass

class TestVotes(unittest.TestCase):
    def test_get_most_no_of_votes(self):
        expected = "john"
        actual = Votes().get_most_no_of_votes(votes)
        self.assertEqual(expected,actual)