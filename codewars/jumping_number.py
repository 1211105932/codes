def jumping_number(number):
    number = list(str(number))
    for i, j in enumerate(number):
        if i > 0:
            if abs(int(j) - int(number[i - 1])) != 1:
                return "Not!!"
    
    return "Jumping!!"