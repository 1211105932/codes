def calculate(num1, operation, num2): 
    try:
        return eval(f"{num1}{operation}{num2}")
    except (ZeroDivisionError, SyntaxError):
        return None