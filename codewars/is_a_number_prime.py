from math import isqrt

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, isqrt(num) + 1):
        if not num % i:
            return False
    return True