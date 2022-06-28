#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number < 0:
    digit = (number * -1) % 10
    digit *= -1
else:
    digit = number % 10

msg1 = f"Last digit of {number:d} is {digit:d} and is greater than 5"
msg2 = f"Last digit of {number:d} is {digit:d} and is 0"
msg3 = f"Last digit of {number:d} is {digit:d} and is less than 6 and not 0"

if digit > 5:
    print(msg1)
elif digit == 0:
    print(msg2)
else:
    print(msg3)
