from collections import Counter

with open("input", "r") as f:
    arr1 = []
    arr2 = []
    lines = f.readlines()
    for line in lines:
        l, r = map(int, line.strip().split())

        arr1.append(l)
        arr2.append(r)

# arr1 = sorted(arr1)
# arr2 = sorted(arr2)

counter = Counter(arr2)

# arr3 = []
# for i in range(len(arr1)):
#     print(arr1[i])
#     print(arr2[i])
#     arr3.append(abs(arr1[i] - arr2[i]))

# print(sum(arr3))
# for i in range()

sum_ = 0
for i in arr1:
    sum_ += i * counter[i]

print(sum_)