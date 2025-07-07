def digital_root(n):
    while not n < 10:
        n = sum(int(x) for x in list(str(n)))
    return n