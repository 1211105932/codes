fib = [1, 1]

for i in range(2, 4782):
    fib.append(fib[i-2] + fib[i-1])

print(len(str(fib[-1])))