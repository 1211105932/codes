from collections import Counter

def highest_rank(arr):
    counter = Counter(arr)
    return max(k for k, v in counter.items() if v == counter.most_common()[0][1])