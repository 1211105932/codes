def sort_array(source_array):
    odd = sorted(i for i in source_array if i % 2)
    x = 0
    
    res = []
    for i in source_array:
        if i % 2:
            res.append(odd[x])
            x += 1
        else:
            res.append(i)
            
    return res