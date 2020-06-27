#!/usr/bin/python3.7
# written by: atholcomb
# fizzbuzz.py

def fizz_buzz(number):
    if number % 3 == 0 and number % 5 == 0:
        return number, "FizzBuzz"
    elif number % 3 == 0:
        return number, "Fizz"
    elif number % 5 == 0:
        return number, "Buzz"
    else:
        return number, "number not divisible by 3 or 5"

print(fizz_buzz(3))
print(fizz_buzz(5))
print(fizz_buzz(15))
print(fizz_buzz(4))
