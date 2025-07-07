import os
from math import prod
import time

__location__ = os.path.join(os.path.dirname(__file__), "input")
with open(__location__, "r") as f:
    lines = f.readlines()

# for line in lines:
#     id, info = line.split(":")
#     id = int(id.split()[-1])
#     info = [i.split(",") for i in info.split(";")]


# def p1():
#     limit = {"red": 12, "green": 13, "blue": 14}
#     total = 0

#     possible = True
#     for i in info:
#         for j in i:
#             num, color = j.split()
#             if int(num) > limit[color]:
#                 possible = False
#                 break

#     if possible:
#         total += id

#     print(total)


# 74804
def p2():
    total = 0
    for line in lines:
        id, info = line.split(":")
        id = int(id.split()[-1])
        info = [i.split(",") for i in info.split(";")]
        for i in info:
            max_ = {"red": 0, "green": 0, "blue": 0}
            for j in i:
                num, color = j.split()
                # print(max_)
                # print(f"a{color}a")
                max_[color] = max(max_[color], int(num))
                print(max_)
        
            total += prod(max_.values())

        print(f"max_: {max_}, prod: {prod(max_.values())}, total: {total}")
        # time.sleep(1)

    print(total)

p2()