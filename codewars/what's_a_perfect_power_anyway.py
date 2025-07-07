from math import log2

def isPP(n):
    for i in range(2, int(log2(n)) + 1):
        m = round(n ** (1 / i))
        
        if m ** i == n:
            return [m, i]
    
    return None