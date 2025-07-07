def sum_of_integers_in_string(s):
    arr = []
    digits = ""
    
    for i in s:
        if i.isdigit():
            digits += i
        else:
            if digits:
                arr.append(int(digits))
            digits = ""

    if digits:
        arr.append(int(digits))
    
    return sum(arr)