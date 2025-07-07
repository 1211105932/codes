def rank(st, we, n):
    if not st:
        return "No participants"
    
    st = st.split(",")

    if n > len(st):
        return "Not enough participants"
    
    d = dict()
    for i, j in enumerate(st):
        d[j] = (len(j) + sum(map(lambda x: ord(x) - ord("a") + 1, j.lower()))) * we[i]
    
    return sorted(d.items(), key=lambda x: (-x[1], x[0]))[n - 1][0]