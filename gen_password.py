#!/usr/bin/python3.7
# written by: atholcomb
# gen_password.py

import random

lower = 'abcdefghijklmnopqrstuvwxyz'
upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '0123456789'

def gen_password(length):
    result = ''
    for l in range(length):
        password = random.choice(lower+upper+numbers)
        result += password
    return result


length = int(input("Enter password length: "))
for i in range(5):
    print(gen_password(length))
