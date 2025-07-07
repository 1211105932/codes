import math

def persistence(n):
    ans = 0
    while len(str(n)) > 1:
        n = [int(x) for x in str(n)]
        n = math.prod(n)
        ans += 1
    return ans