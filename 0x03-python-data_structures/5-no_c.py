#!/usr/bin/python3
def no_c(my_string):
    for i in my_string:
        if i != 'c' and i != 'C':
            print("{}".format(i), end="")
