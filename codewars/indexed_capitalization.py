def capitalize(s, ind):
    res = []
    for i, j in enumerate(s):
        res.append(j.upper() if i in ind else j)
    return "".join(res)