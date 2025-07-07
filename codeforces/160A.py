"""
2
3 3

2
"""

def main():
    n = int(input())
    nums = sorted(list(map(int, input().split())), reverse=True)
    coins = sum(nums)//2
    total = 0
    count = 0

    for i in nums:
        if total <= coins:
            total += i
            count += 1
        
    print(count)

if __name__ == "__main__":
    main()