from math import prod
from heapq import nlargest

def max_product(lst, n_largest_elements):
    return prod(nlargest(n_largest_elements, lst))