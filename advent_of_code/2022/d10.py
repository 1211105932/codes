import os

__location__ = os.path.join(os.path.dirname(__file__), "input")
with open(__location__, "r") as f:
    lines = f.readlines()

cycle = res = 0
value = 1
for line in lines:
    if cycle in (20,60,100,140,180,220):
        print(f"cycle: {cycle}, value: {value}")
        res += cycle * value

    if line.strip() != "noop":
        value += int(line.split()[-1])
        cycle += 1
    
    if cycle in (20,60,100,140,180,220):
        print(f"cycle: {cycle}, value: {value}")
        res += cycle * value

    cycle += 1

print(value)
print(res)


(20 * 21)+(60 * 19)+(100 * 31)+(140 * 21)+(180 * 19)+(220 * 19)