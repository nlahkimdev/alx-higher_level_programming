#!/usr/bin/python3
def multiple_returns(sentence):
    c = ()
    result = []
    if sentence:
        result.append(len(sentence))
        result.append(sentence[0])
    elif not sentence:
        result.append(None)
        result.append(0)
    c = tuple(result)
    return c
