#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number[-1] == 0:
    result = "and is zero"
elif number[-1] > 5:
    result = "and is greater than 5"
elif number[-1] < 6:
    result = "and is less than 6 and not 0"
print(f"Last digit of {number} is {number[-1]} {result}")
