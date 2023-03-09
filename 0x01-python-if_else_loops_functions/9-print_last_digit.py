#!/usr/bin/python3
def print_last_digit(number):
    numToStr = str(number)
    last = numToStr[-1]
    if number < 0:
        result = int(last) * -1
    else:
        result = int(last)
    print("{:d}".format(result), end='')
    return result
