from collections import Counter

def comp(array1, array2):
    if array1 is not None and array2 is not None:
        counter1 = Counter(x * x for x in array1)
        counter2 = Counter(array2)
        return counter1 == counter2
    return False