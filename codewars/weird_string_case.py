def to_weird_case(words):
    res = []
    for word in words.split():
        w = []
        for i, j in enumerate(word):
            if i % 2:
                w.append(j.lower())
            else:
                w.append(j.upper())
        res.append("".join(w))        
    return " ".join(res)