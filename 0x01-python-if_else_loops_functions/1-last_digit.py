#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

digit = number % 10
msg = "and is less than 6 and not 0"

if number > 0:
    if digit > 5:
        print(f"Last digit of {number: d} is {digit: d} and is greater than 5")
    elif (digit < 6 and (digit != 0)):
        print(f"Last digit of {number: d} is {digit: d} {msg:s}")
    else:
        print(f"Last digit of {number: d} is {digit: d} and is 0")
elif number < 0:
    digit *= -1
    if digit == 0:
        print(f"Last digit of {number: d} is {digit: d} and is 0")
    else:
        print(f"Last digit of {number: d} is {digit: d} {msg:s}")
else:
    print(f"Last digit of {number: d} is {digit: d} and is 0")
