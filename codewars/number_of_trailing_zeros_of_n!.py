def zeros(n):
    res = 0
    while n >= 5:
        n //= 5
        res += n
    return res