#!/usr/bin/python3.7
# written by: atholcomb
# mobilenumber.py

import random
import time

""" Mobile number function """

def getMobileNumber():
    count = 0
    div = '-'
    number = ""
    lnum = []
    while count < 10: 
        rnumber = random.choice('0123456789')
        count += 1
        number += rnumber
    
    time.sleep(1)
    return f"Formatted: {number[0:3]}{div}{number[3:6]}{div}{number[6:]}", "Non-Formatted:", number            

# Ask user for number of mobile numbers
ask = int(input("How many mobile numbers would you like generated?: "))
print("Generating mobile numbers.....")
for a in range(ask):
    print(getMobileNumber())
