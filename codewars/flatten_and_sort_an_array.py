from itertools import chain

def flatten_and_sort(array):
    return sorted(list(chain(*array)))