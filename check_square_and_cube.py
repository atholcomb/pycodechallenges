#!/usr/bin/python3.7
# written by: atholcomb
# check_square_and_cube.py
# Create a function that takes a list of two numbers and checks if the square root 
# of the first number is equal to the cube root of the second number.

import math

def check_square_and_cube(lst):

    square = math.sqrt(lst[0])
    cube = lst[1] ** (1./3.)

    if square == cube:
        return True
    return False

print(check_square_and_cube([4, 8]))
print(check_square_and_cube([16, 48]))
print(check_square_and_cube([9, 27]))
