#!/usr/bin/python3
import add_0
add = __import__('add_0').add
a = 1
b = 2
print("{:d} + {:d} = {:d}".format(a, b, add_0.add(a, b)))
