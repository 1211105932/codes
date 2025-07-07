import os
from math import prod

__location__ = os.path.join(os.path.dirname(__file__), "input")
with open(__location__, "r") as f:
    lines = f.readlines()

arr = []
movement = [(1,1),(3,1),(5,1),(7,1),(1,2)]

for i in movement:
    x = y = 0
    count = 0
    while y + i[1] < len(lines):
        x += i[0]
        x %= 31
        y += i[1]
        
        if lines[y][x] == "#":
            count += 1

    arr.append(count)    

print(prod(arr))