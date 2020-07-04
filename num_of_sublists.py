#!/usr/bin/python3.7
# written by: atholcomb
# try.py
# Return the total number of lists inside a given list.

def num_of_sublists(some_list):
    result = 0

    for item in some_list:
        if item == 1 or item == 2 or item == 3:
            result = 0
        else:
            result += 1

    return result


print(num_of_sublists([[1, 2, 3]]))
print(num_of_sublists([[1, 2, 3], [1, 2, 3], [1, 2, 3]]))
print(num_of_sublists([[1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3]]))
print(num_of_sublists([1, 2, 3]))
