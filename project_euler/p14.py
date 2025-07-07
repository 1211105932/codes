max_ = 0
best = 0

for i in range(1, 1000001):
    count = 0
    n = i
    while n > 1:
        # print(count)
        # print(n)
        if n % 2:
            n = 3 * n + 1
        else:
            n //= 2
        count += 1
    
    if count > max_:
        max_ = count
        best = i

print(best)