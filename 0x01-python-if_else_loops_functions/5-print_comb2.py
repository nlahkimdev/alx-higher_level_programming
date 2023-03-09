#!/usr/bin/python3
for i in range(0, 100):
    if i < 10:
        print("0{:d}".format(int(i)), end=', ')
    elif i != 99:
        print("{:d}".format(int(i)), end=', ')
    else:
        print(i, end='\n')
