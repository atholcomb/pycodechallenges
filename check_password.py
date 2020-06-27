#!/usr/bin/python3.7
# written by: atholcomb
# check_password.py

import random

lower = 'abcdefghijklmnopqrstuvwxyz'
upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '0123456789'
special = '!@#$%^&*?'

#requirement = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*?'

password = input("Enter a password: " )

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
    

print(check_password(password))

