def flatten(lst):
    arr = []
    
    for i in lst:
        if isinstance(i, list):
            arr.extend(i)
        else:
            arr.append(i)
    
    return arr