#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    sum = 0
    ln = len(sys.argv)
    if ln == 1:
        print("{}".format(0))
    elif ln == 2:
        print("{}".format(sys.argv[1]))
    else:
        for i in range(1, ln):
            sum = sum + int(sys.argv[i])
        print("{:d}".format(sum))
