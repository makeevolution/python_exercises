#https://www.geeksforgeeks.org/python-program-to-swap-two-elements-in-a-list/

class swap_two_elements():
    def swap_two_elements(self, lst, pos1, pos2):
        lst[pos2], lst[pos1] = lst[pos1], lst[pos2]
        return lst


if __name__ == "__main__":
    print(swap_two_elements().swap_two_elements([1, 2, 3], 2, 1))
