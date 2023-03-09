#!/usr/bin/python3
def print_last_digit(number):
    last = str(number)[-1]
    if number > 0:
        print("{:d}".format(number % 10), end='')
    else:
        print("{}".format(last), end='')
    return last
