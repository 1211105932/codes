def solve(a,b):
    arr = []
    for i in a:
        if i not in b:
            arr.append(i)
    
    for i in b:
        if i not in a:
            arr.append(i)
    
    return "".join(arr)