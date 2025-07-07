import os
import re

__location__ = os.path.join(os.path.dirname(__file__), "input")
with open(__location__, "r") as f:
    lines = f.readlines()

enabled = True
total1 = total2 = 0
for line in lines:
    valid = re.findall(r"mul\([0-9]{1,3},[0-9]{1,3}\)|do\(\)|don't\(\)", line)

    for i in valid:
        if i == "do()":
            enabled = True
        elif i == "don't()":
            enabled = False
        else:
            l, r = map(int, i.replace("mul(", "").replace(")", "").split(","))
            prod = l * r
            total1 += prod
            if enabled:
                total2 += prod

print(total1)
print(total2)