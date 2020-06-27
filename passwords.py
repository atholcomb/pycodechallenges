#!/usr/bin/python3.7
# written by: atholcomb
# passwords.py

import random

lower = 'abcdefghijklmnopqrstuvwxyz'
upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '0123456789'
special = '!@#$%^&*?'

#requirement = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*?'

# Checks the user's password and display information about it
def check_password(password):
    low = 0
    up = 0
    nums = 0
    spec = 0
    for p in password:
        if p in lower:
            low += 1
        elif p in upper:
            up += 1
        elif p in numbers:
            nums += 1
        elif p in special:
            spec += 1
    return f"{low} lowercase, {up} uppercase, {nums} number(s), {spec} special character(s)"

# Generates a password specified for the length entered 
def gen_password(length):
    result = ''
    for l in range(length):
        password = random.choice(lower+upper+numbers)
        result += password
    return result

# loop that runs to ask for user input
while True:
    ask = input("Check password [check], generate pasword [generate], or [exit]: ")
    if ask == 'check':
        password = input("Enter a password: ")
        print(check_password(password))
    elif ask == 'generate':
        length = int(input("Enter password length [1-100]: "))
        print(gen_password(length))
    else:
        print("Quitting...")
        break
        

