#!/usr/bin/python3
def multiple_returns(sentence):
    c = ()
    result = []
    result.append(len(sentence))
    if len(sentence) != 0:
        result.append(sentence[0])
    else:
        result.append("")
    c = tuple(result)
    return c
