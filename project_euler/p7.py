def isprime(n):
    if n <= 1:
        return False
    
    for i in range(2, int(n**0.5) + 1):
        if not n % i:
            return False

    return True

def main():
    primes = []
    num = 2

    while len(primes) < 10001:
        if isprime(num):
            primes.append(num)
        num += 1

    return primes[-1]

if __name__ == "__main__":
    output = main()
    print(output)