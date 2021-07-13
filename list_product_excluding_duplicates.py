from collections import *

class ListProductExcludingDup(object):
    def list_product_exc_dup(self,lst):
        unique = [i for i in Counter(lst).keys()]
        if not unique:
            return 0
        result = 1
        for i in unique:
            result = result * i
        return result