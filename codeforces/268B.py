"""
input:
2

output:
3
"""

def main():
    n = int(input())
    sum = n

    for i in range(1,n):
        sum += i*(n-i)

    print(sum)

if __name__ == "__main__":
    main()