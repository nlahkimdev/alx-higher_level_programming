#!/usr/bin/python3
for i in range(90, 64, -1):
    if i % 2 != 0:
        char = chr(i)
    elif i % 2 == 0:
        char = chr(i+32)
    print("{}".format(char), end='')
