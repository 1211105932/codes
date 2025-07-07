def encrypt_this(text):
    res = []
    
    for i in text.split():
        i = list(i)
        i[0] = str(ord(i[0]))
        
        if len(i) > 2:
            i[1], i[-1] = i[-1], i[1]
        
        res.append("".join(i))
        
    return " ".join(res)