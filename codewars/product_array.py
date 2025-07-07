from math import prod

def product_array(numbers):
    sum_ = prod(numbers)
    return [sum_ / i for i in numbers]