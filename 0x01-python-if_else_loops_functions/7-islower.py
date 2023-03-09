#!/usr/bin/python3
def islower(c):
    if c <= chr(90) and c <= chr(48):
        return False
    elif c >= chr(97) and c <= chr(122):
        return True
