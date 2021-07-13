from collections import *

class ReverseStringsInList(object):
    def reverse_strings(self,lst):
        return list(map(lambda x:x[::-1],lst))