#!/usr/bin/python3
import sys
import os

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)
if __name__ == "__main__":
    import add_0
    a = 1
    b = 2
    print("{:d} + {:d} = {:d}".format(a, b, add_0.add(a, b)))
