#!/usr/bin/python3
for i in range(0, 10):
    for j in range(i, 10):
        if i != j and not (i == 8 and j == 9):
            print("{:d}{:d}".format(int(i), int(j)), end=', ')
        if i == 8 and j == 9:
            print("{:d}{:d}".format(int(i), int(j)), end='\n')
