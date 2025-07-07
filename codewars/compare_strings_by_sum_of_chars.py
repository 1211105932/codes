def compare(s1, s2):
    c1 = c2 = 0

    if s1 and s1.isalpha():
        c1 += sum(ord(i.upper()) for i in s1)
    
    if s2 and s2.isalpha():
        c2 += sum(ord(i.upper()) for i in s2)
    
    return c1 == c2