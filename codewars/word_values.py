def name_value(my_list):
    arr = []
    for i, j in enumerate(my_list):
        value = 0
        for c in j:
            if c.isalpha():
                value += ord(c) - ord("a") + 1
        arr.append(value * (i + 1))
    
    return arr