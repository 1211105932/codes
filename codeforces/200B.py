"""
input:
3
50 50 100

output:
66.666666666667
"""

def main():
    n = input()
    drinks = list(map(int, input().split()))
    print(format(sum(drinks)/len(drinks), ".12f"))

if __name__ == "__main__":
    main()