#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    ln = len(sys.argv)
    if ln == 1:
        print("{} arguments.".format(ln - 1))
    else:
        print("{} arguments:".format(ln - 1))
        for i in range(1, ln):
            print("{}: {}".format(i, sys.argv[i]))
