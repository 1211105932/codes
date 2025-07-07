def dashatize(n):
    res = []
    n = str(abs(n))
    
    for k, v in enumerate(list(n)):
        if int(v) % 2:
            if k != 0 and res[-1] != "-":
                res.append("-")
            res.append(v)
            if k != len(n) - 1 and res[-1] != "-":
                res.append("-")
        else:
            res.append(v)
    
    return "".join(res)