#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    lna = len(tuple_a)
    lnb = len(tuple_b)
    a = list(tuple_a)
    b = list(tuple_b)
    result = ()
    c = []
    if lna == 0:
        a.appedn(0)
        a.appedn(0)
    if lnb == 0:
        b.append(0)
        b.append(0)
    if lna == 1:
        a.append(0)
    if lnb == 1:
        b.append(0)

    c.append(a[0] + b[0])
    c.append(a[1] + b[1])
    result = tuple(c)
    return result
