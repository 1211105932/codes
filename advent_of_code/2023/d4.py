import os
import re

__location__ = os.path.join(os.path.dirname(__file__), "input")
with open(__location__, "r") as f:
    lines = f.readlines()

total = 0
for line in lines:
    count = 0
    lhs, rhs = line.split("|")
    lhs = set(lhs[10:].split())
    rhs = rhs.split()
    for i in rhs:
        if i in lhs:
            count += 1

    if count:
        total += 2 ** (count - 1)
    
print(total)