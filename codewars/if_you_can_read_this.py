from preloaded import NATO # NATO['A'] == 'Alfa', etc

def to_nato(words : str) -> str:
    res = []
    for w in words.replace(" ", "").upper():
        for c in w:
            if c.isalpha():
                res.append(NATO[c])
            else:
                res.append(c)
    
    return " ".join(res)