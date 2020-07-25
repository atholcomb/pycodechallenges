#!/usr/bin/python3.7
# written by: atholcomb
# vowels.py
# Write a function that recursively returns the number of vowels in a string.
# If it wasn't clear enough already, you should use recursion in your solution.

def vowels(string):
    vowels = 'aeiou'
    count = 0

    for vowel in vowels:
        for item in string:
            if vowel in item:
                count += 1

    return count

print(vowels("apple"))
print(vowels("cheesecake"))
print(vowels("bbb"))
print(vowels(""))
