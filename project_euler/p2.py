def main():
    arr = [1, 1]
    sum_ = 0
    while arr[-1] <= 4000000:
        fib = arr[-2] + arr[-1]

        if not fib % 2:
            sum_ += fib
        
        arr.append(fib)

    return sum_

if __name__ == "__main__":
    output = main()
    print(output)