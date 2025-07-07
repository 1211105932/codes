"""
input:
5
2 4 7 8 10

output:
3
"""

def main():
    n = int(input())
    numbers = list(map(int, input().split()))
    odd, even = 0, 0

    for number in numbers[:3]:
        if number % 2 != 0:
            odd += 1
        else:
            even += 1

    if odd > 1:
        print(*[pos+1 for pos,number in enumerate(numbers) if number % 2 == 0])
    else:
        print(*[pos+1 for pos,number in enumerate(numbers) if number % 2 != 0])

if __name__ == "__main__":
    main()