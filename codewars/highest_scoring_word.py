def score(word):
    cs = "abcdefghijklmnopqrstuvwxyz"
    sum = 0
    for c in word:
        sum += cs.index(c)+1
    return sum

def high(x):
    x = x.split()
    arr = [score(y) for y in x]
    return x[arr.index(max(arr))]