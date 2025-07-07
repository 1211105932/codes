from itertools import groupby

def unique_in_order(sequence):
    return list(k for k, g in groupby(sequence))