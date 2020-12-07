#!/usr/bin/python3.7
# written by: atholcomb
# find_odd.py
# Create a function that takes a list and finds the integer which appears an odd number of times.
# There will always only be one integer that appears an odd number of times.

def find_odd(num_list):

    sorted_list = sorted(num_list)
    
    for item in sorted_list:
        if sorted_list.count(item) % 2 == 1:
            return item


print(find_odd([1, 1, 2, -2, 5, 2, 4, 4, -1, -2, 5]))       # -1
print(find_odd([20, 1, 1, 2, 2, 3, 3, 5, 5, 4, 20, 4, 5]))  # 5
print(find_odd([10]))                                       # 10
