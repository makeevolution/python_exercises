# Given an Integer list, perform join with the delimiter, avoiding the extra delimiter at the end.
# Input : test_list = [4, 7, 8, 3, 2, 1, 9], delim = “*” 
# Output : 4*7*8*3*2*1*9 

def list_to_string_with_delimiter(input, delimiter):
    string = "*".join(list([*map(lambda x:str(x), input)]))

if __name__=="__main__":
    test_list = [4, 7, 8, 3, 2, 1, 9]
    list_to_string_with_delimiter(test_list,"*")