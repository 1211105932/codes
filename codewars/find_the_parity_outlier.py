def find_outlier(integers):
    odd = []
    even = []
    for x in integers:
        if x % 2:
            odd.append(x)
        else:
            even.append(x)
        
    if len(odd) == 1:
        return odd[0]
    else:
        return even[0]