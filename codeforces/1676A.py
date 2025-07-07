"""
input:
5
213132
973894
045207
000000
055776

output:
YES
NO
YES
YES
NO
"""

def main():
    n = int(input())
    output = ""

    for _ in range(n):
        digits = list(map(int, input()))
        if sum(digits[:3]) == sum(digits[3:]):
            output += "YES\n"
        else:
            output += "NO\n"

    print(output)

if __name__ == "__main__":
    main()