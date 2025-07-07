def cube_odd(arr):
    res = 0
    
    for i in arr:
        if isinstance(i, bool) or not isinstance(i, int):
            return None
        if i % 2:
            res += i ** 3
    
    return res