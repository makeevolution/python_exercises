from collections import *
import re
class AddSpaceBetweenWords(object):
    def add_space(self,lst):
        return [re.sub(r"(\w)([A-Z])",r"\1 \2",i) for i in lst]