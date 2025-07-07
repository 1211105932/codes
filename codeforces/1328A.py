def main():
    n = int(input())
    nums = []
    for _ in range(n):
        nums.append(list(map(int, input().split())))
    for num in nums:
        if num[0] % num[1]:
            print(num[1] - num[0] % num[1])
        else:
            print(0)

if __name__ == "__main__":
    main()