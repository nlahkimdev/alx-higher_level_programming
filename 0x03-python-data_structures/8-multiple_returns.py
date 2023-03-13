#!/usr/bin/python3
def multiple_returns(sentence):
    c = ()
    result = []
    result.append(len(sentence))
    result.append(sentence[0])
    c = tuple(result)
    return c
