def paint_letterboxes(start, finish):
    arr = [0] * 10
    
    for i in range(start, finish + 1):
        for j in str(i):
            arr[int(j)] += 1
    
    return arr