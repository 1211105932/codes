from heapq import nlargest

def largest(n, xs):
    return sorted(nlargest(n, xs))