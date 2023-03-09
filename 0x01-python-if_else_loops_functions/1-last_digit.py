#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
numToStr = str(number)
last = numToStr[-1]
if number < 0:
    last = int(last) * -1
else:
    last = int(last)

print(f"{number} {last}")

if last == 0:
    result = "and is zero"
elif last > 5:
    result = "and is greater than 5"
elif last < 6:
    result = "and is less than 6 and not 0"

print(f"Last digit of {number} is {last} {result}")
