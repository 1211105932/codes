def race(v1, v2, g):
    if v1 >= v2:
        return None
    
    total = g / (v2 - v1) * 3600
    
    h = int(total // 3600)
    m = int((total % 3600) // 60)
    s = int(total % 60)
    
    return [h, m, s]