from collections import Counter

def find_uniq(arr):
    counter = Counter(arr)
    for i, j in counter.items():
        if j == 1:
            return i