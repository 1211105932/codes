def find_even_index(arr):
    l, r = 0, sum(arr)
    
    for i, j in enumerate(arr):
        r -= j
        if l == r:
            return i
        l += j
            
    return -1