def sum_of_differences(arr):
    arr = sorted(arr, reverse=True)
    
    res = 0
    for i in range(1, len(arr)):
        res += arr[i - 1] - arr[i]
    
    return res