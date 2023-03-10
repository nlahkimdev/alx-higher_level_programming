#!/usr/bin/python3
if __name__ == "__main__":
    from acalculator_1 import add
    from acalculator_1 import sub
    from acalculator_1 import mul
    from acalculator_1 import div
    a = 10
    b = 5
    print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
    print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))
    print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))
    print("{:d} / {:d} = {:d}".format(a, b, div(a, b)))
