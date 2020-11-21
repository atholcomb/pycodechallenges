#!/usr/bin/python3.7
# written by: atholcomb
# make_tags.py

def make_tags(tag, word):
    return f"<{tag}>{word}</{tag}>"


print(make_tags('i', 'Yay'))
print(make_tags('i', 'Hello'))
print(make_tags('cite', 'Yay'))
