from math import factorial

def strong_num(number):
    sum = 0
    for i in str(number):
        sum += factorial(int(i))
    
    return "STRONG!!!!" if sum == number else "Not Strong !!"