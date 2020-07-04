#!/usr/bin/python3.7
# written by: atholcomb
# count_uppercase.py
# Given random string, return how many uppercase letters there are in a list of various words

def count_uppercase(string):
    uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    result = 0

    for word in string:
        for letter in word:
            if letter in uppercase: 
                result += 1

    return result

print(count_uppercase(["SOLO", "hello", "Tea", "wHat"])) # should be 6
print(count_uppercase(["little", "lower", "down"])) # should be 0 
print(count_uppercase(["EDAbit", "Educate", "Coding"])) # should be 5
