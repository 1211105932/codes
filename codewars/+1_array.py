def up_array(arr):
    if not arr:
        return None
    
    for i in arr:
        if i < 0 or i > 9:
            return None

    res = "".join(map(str, arr))
    res = int(res) + 1
    res = list(map(int, str(res)))
    
    if not arr[0] and len(arr) > 1:
        res.insert(0, 0)
    
    return res