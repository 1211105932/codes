"""
input:
5 3
-6 0 35 -2 4

output:
8
"""

def main():
    n, m = input().split()
    n, m = int(n), int(m)
    sets = list(map(int, input().split()))
    sets = sorted(sets)
    print(-sum(i for i in sets[:m] if i < 0))

if __name__ == "__main__":
    main()