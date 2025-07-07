import os

__location__ = os.path.join(os.path.dirname(__file__), "input")
with open(__location__, "r") as f:
    lines = f.readlines()

d = dict()
for line in lines[:1176]:
    before, after = map(int, line.strip().split("|"))
    d.setdefault(after, set()).add(before)

total = 0
for line in lines[1177:]:
    arr = list(map(int, line.strip().split(",")))
    valid = True
    for i, j in enumerate(arr):
        for x, y in enumerate(arr):
            if i<x and y in d[j]:
                valid = False

    if valid: total += arr[len(arr)//2]

print(total)