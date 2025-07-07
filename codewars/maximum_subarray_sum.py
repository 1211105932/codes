def max_sequence(arr):
    res = 0
    current = 0
    for i in range(len(arr)):
        current = max(current + arr[i], arr[i])
        res = max(res, current)
    return res