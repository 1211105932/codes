"""
input:
5
8 7
8 1
6 10
999999733 999999732
999999733 999999733

output:
2
8
1
999999733
1
"""

from math import sqrt

def main():
    n = int(input())
    a = []
    for _ in range(n):
        a.append(input().split())

    output = []
    for i in a:

        if int(i[0])/int(i[1]) <= 1:
            output.append("1")
        else:
            for j in range(2, int(sqrt(int(i[0])) + 1)):
                if int(i[0]) % j == 0:
                    output.append(int(i[0])//int(i[1])+1)
            output.append(i[0])


    print(output)

if __name__ == "__main__":
    main()