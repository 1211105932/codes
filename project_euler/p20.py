from math import factorial

def main():
    n = 100
    return sum(map(int, str(factorial(n))))

if __name__ == "__main__":
    output = main()
    print(output)