def solve(s):
    vowels = set("aeiou")
    res = []
    
    current = 0
    for i, j in enumerate(s):
        if j in vowels:
            res.append(current)
            current = 0
        else:
            current += ord(j) - ord("a") + 1
            if i == len(s) - 1:
                res.append(current)
        
    return max(res)