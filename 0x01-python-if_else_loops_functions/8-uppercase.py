#!/usr/bin/python3
def uppercase(c):
    for i in c:
        if ord(i) >= 97 and ord(i) <= 122:
            n = chr(ord(i) - 32)
        else:
            n = i
        print(n, end='')
    print("", end='\n')
