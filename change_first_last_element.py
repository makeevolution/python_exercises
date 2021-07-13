#https://www.geeksforgeeks.org/python-program-to-interchange-first-and-last-elements-in-a-list/

class swap_first_last():
    def swap_first_last(self,lst):
        lst[-1],lst[0] = lst[0], lst[-1]
        return lst
