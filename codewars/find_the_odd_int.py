from collections import Counter

def find_it(seq):
    counter = Counter(seq)
    return [x for x in counter if counter[x] % 2 == 1][0]