"""
input:
8

output:
YES
"""

def main():
    n = int(input())
    print("YES") if n % 2 == 0 and n != 2 else print("NO")

if __name__ == "__main__":
    main()