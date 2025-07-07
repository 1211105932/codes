import os
from collections import Counter

__location__ = os.path.join(os.path.dirname(__file__), "input")
with open(__location__, "r") as f:
    lines = f.readlines()

arr = []
for line in lines:
    hand, bid = line.split()
    counter = Counter(hand)
    arr.append(counter)


arr2 = sorted(arr)

for i in range(10):
    print(f"a1: {arr[i]}")
    print(f"a2: {arr2[i]}")
    print()