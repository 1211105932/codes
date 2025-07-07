def delete_nth(order,max_e):
    dict = {}
    res = []
    
    for i in order:
        dict[i] = dict.get(i, 0) + 1
        
        if dict[i] <= max_e:
            res.append(i)
        
    return res