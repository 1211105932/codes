"""
5
2 3
10 10
2 4
7 4
9 3

1
0
2
2
1
"""

def main():
    n = int(input())
    nums = []
    for _ in range(n):
        nums.append(list(map(int, input().split())))
    
    output = []
    for num in nums:
        count = 0
        if num[0] != num[1]:
            if num[0] > num[1]:
                if (num[0]-num[1]) % 2 == 0:
                    count += 1
                else:
                    count += 2
            else:
                if (num[1]-num[0]) % 2 != 0:
                    count += 1
                else:
                    count += 2

        output.append(count)
    
    for i in output:
        print(i)

if __name__ == "__main__":
    main()