#!/usr/bin/python3.7
# written by: atholcomb
# count_letters.py

def count_letters(text):
    result = {}
    text = text.lower()
    text = text.replace(' ', '')
    
    if '!' in text:
        t1 = text.index('!')
        text = text[:t1]
    elif '.' in text:
        t2 = text.index('.')
        text = text[:t2]
    
    for letter in text:
        if letter in text:
            result[letter] = text.count(letter)
    
    return result


print(count_letters("AaBbCc"))
# Should be {'a': 2, 'b': 2, 'c': 2}

print(count_letters("Math is fun! 2+2=4"))
# Should be {'m': 1, 'a': 1, 't': 1, 'h': 1, 'i': 1, 's': 1, 'f': 1, 'u': 1, 'n': 1}

print(count_letters("This is a sentence."))
# Should be {'t': 2, 'h': 1, 'i': 2, 's': 3, 'a': 1, 'e': 3, 'n': 2, 'c': 1}
