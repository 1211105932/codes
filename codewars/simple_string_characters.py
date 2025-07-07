def solve(s):
    upper = lower = number = special = 0
    for i in s:
        if i.isalpha():
            if i.isupper():
                upper += 1
            else:
                lower += 1
        elif i.isdigit():
            number += 1
        else:
            special += 1
        
    return [upper, lower, number, special]