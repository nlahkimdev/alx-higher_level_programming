#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    result = []
    ln = len(my_list)
    for i in range(0, ln):
        result.append(my_list[i])
    if idx < 0:
        return result
    elif idx > len(my_list) - 1:
        return result
    else:
        result[idx] = element
        return result
