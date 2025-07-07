"""
input:
12 3

output:
4 4 4
"""

def main():
    n, m = input().split()
    n, m = int(n), int(m)
    output = []

    if n % m != 0:
        for _ in range(m):
            a = m-(n%m)
            output.append(int(n//m))
        output = output[:a] + [x+1 for x in output[a:]]
    else:
        for _ in range(m):
            output.append(int(n/m))

    print(*output)

if __name__ == "__main__":
    main()