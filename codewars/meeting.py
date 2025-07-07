def meeting(s):
    s = s.upper().split(";")
    
    res = []
    for w in s:
        first, last = w.split(":")
        res.append((last, first))
    
    return "".join(f"({last}, {first})" for last, first in sorted(res))