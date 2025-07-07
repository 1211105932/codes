def isprime(n):
    if n <= 1:
        return False
    
    for i in range(2, int(n**0.5) + 1):
        if not n % i:
            return False
    return True


def main():
    n = 600851475143
    prime_factors = []

    for i in range(2, int(n ** 0.5) + 1):
        if not n % i:
            if isprime(i):
                prime_factors.append(i)
            elif isprime(n//i):
                prime_factors.append(n//i)

    return prime_factors[-1]

if __name__ == "__main__":
    output = main()
    print(output)