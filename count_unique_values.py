#https://www.geeksforgeeks.org/how-to-count-unique-values-inside-a-list/
from collections import Counter
# [1,3,2,4,1]

class count_unique_values():
    def count_unique_values(self, lst):
        for i in lst:
            while lst.count(i) > 1:
                lst.remove(i)
        return len(lst)

    def count_unique_values_using_counter(self,lst):
        return len(Counter(lst).keys())
