import os
from collections import Counter

__location__ = os.path.join(os.path.dirname(__file__), "input")
with open(__location__, "r") as f:
    lines = f.readlines()

total1 = total2 = 0
for line in lines:
    policy, password = [i.strip() for i in line.split(":")]
    num, char = policy.split()
    lower, upper = map(int, num.split("-"))
    counter = Counter(password)

    if lower <= counter[char] <= upper:
        total1 += 1

    if (password[lower-1] == char) ^ (password[upper-1] == char):
        total2 += 1

print(total1)
print(total2)