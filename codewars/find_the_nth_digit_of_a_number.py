def find_digit(num, nth):
    if nth <= 0:
        return -1
    
    num = list(str(abs(num)))
    
    if len(num) >= nth:
        return int(num[::-1][nth - 1])
    else:
        return 0