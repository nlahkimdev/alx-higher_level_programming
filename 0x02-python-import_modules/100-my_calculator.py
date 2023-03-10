#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv
    if argv != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        a = int(argv[1])
        op = argv[2]
        b = int(argv[3])
        if op == '+':
            result = add(a, b)
        if op == '-':
            result = sub(a, b)
        elif op == "*":
            result = mul(a, b)
        elif op == "/":
            result = div(a, b)
        elif op != '+' and op != '-' and op != '*' and op != '/':
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)
        if op == '+' or op == '-' or op == '*' or op == '/':
            print("{} {} {} = {}".format(a, op, b, result))
