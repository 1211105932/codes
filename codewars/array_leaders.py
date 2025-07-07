def array_leaders(numbers):
    s = sum(numbers)
    res = []
    
    for number in numbers:
        s -= number
        if number > s:
            res.append(number)
    
    return res