#!/usr/bin/python3
if __name__ == "__main__":
    from inspect import getmembers, isfunction
    import hidden_4 as mod
    ln = len(getmembers(mod))
    mem = getmembers(mod)
    for a in range(0, ln):
        if isfunction(mem[a][1]):
            if mem[a][0][0] != '_' and mem[a][0][1] != '_':
                print(mem[a][0])
