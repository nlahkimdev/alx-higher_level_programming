#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    ln = len(sys.argv)
    if ln != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    elif ln == 4:
        a = int(sys.argv[1])
        op = str(sys.argv[2])
        b = int(sys.argv[3])
        match op:
            case '+':
                result = add(a, b)
            case '-':
                result = sub(a, b)
            case "*":
                result = mul(a, b)
            case '/':
                result = div(a, b)
            case default:
                print("Unknown operator. Available operators: +, -, * and /")
                sys.exit(1)
        if op == '+' or op == '-' or op == '*' or op == '/':
            print("{} {} {} = {}".format(a, op, b, result))
