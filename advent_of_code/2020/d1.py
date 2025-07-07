import os

__location__ = os.path.join(os.path.dirname(__file__), "input")
with open(__location__, "r") as f:
    lines = f.readlines()

s = set()
for line in lines:
    if line not in s:
        s.add(int(line))

s = sorted(s)

for i, j in enumerate(s):
    
    l, r = i + 1, len(s) - 1
    while l < r:
        sum_ = j + s[l] + s[r]

        if sum_ > 2020:
            r -= 1
        elif sum_ < 2020:
            l += 1
        else:
            print(j * s[l] * s[r])
            break