from functools import reduce

def logical_calc(array, op):
    match op:
        case "AND":
            return all(array)
        case "OR":
            return any(array)
        case "XOR":
            return reduce(lambda x, y: x ^ y, array)