def find_smallest(numbers, to_return):
    x = min(numbers)
    return x if to_return == "value" else numbers.index(x)