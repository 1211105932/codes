def main():
    n = 100
    sum_ = sum_of_squares = 0
    for i in range(n+1):
        sum_ += i
        sum_of_squares += i * i

    return abs(sum_of_squares - sum_ * sum_)

if __name__ == "__main__":
    output = main()
    print(output)