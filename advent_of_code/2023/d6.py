import os

__location__ = os.path.join(os.path.dirname(__file__), "input")
with open(__location__, "r") as f:
    lines = f.readlines()

time, distance = ((int(i) for i in line[9:].split()) for line in lines)

total = 1
for t, d in zip(time, distance):
    count = 0
    for i in range(1, t):
        if i * (t - i) > d:
            count += 1
    
    total *= count

print(total)



count = 0
t, d = (int("".join(line[9:].split())) for line in lines)
for i in range(1, t):
    if i * (t - i) > d:
        count += 1

print(count)