def isprime(n):
    if n <= 1:
        return False
    
    for i in range(2, int(n**0.5) + 1):
        if not n % i:
            return False

    return True

def main():
    primes = [2]
    num = 3

    while primes[-1] < 2000000:
        if isprime(num):
            primes.append(num)
        num += 1
    
    print(primes)
    return sum(primes)

if __name__ == "__main__":
    output = main()
    print(output)