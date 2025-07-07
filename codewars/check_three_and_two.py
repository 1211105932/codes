from collections import Counter

def check_three_and_two(array):
    counter = Counter(array)
    return sorted(counter.values()) == [2, 3]