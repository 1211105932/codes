def string_merge(string1, string2, letter):
    l1 = list(string1)
    l2 = list(string2)
    
    return "".join(l1[:l1.index(letter)] + l2[l2.index(letter):])