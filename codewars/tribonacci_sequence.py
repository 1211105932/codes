def tribonacci(signature, n):
    arr = signature
    for i in range(2, n-1):
        arr.append(arr[i-2] + arr[i-1] + arr[i])
    return arr[:n]