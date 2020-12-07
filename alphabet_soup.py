#!/usr/bin/python3.7
# written by: atholcomb
# alphabet_soup.py
# Create a function that takes a string and returns a string with its letters in alphabetical order.

def alphabet_soup(string):
    return ''.join(sorted(string))


print(alphabet_soup("hello"))       # "ehllo"
print(alphabet_soup("edabit"))      # "abdeit"
print(alphabet_soup("hacker"))      # "acehkr"
print(alphabet_soup("geek"))        # "eegk"
print(alphabet_soup("javascript"))  # "aacijprstv"
