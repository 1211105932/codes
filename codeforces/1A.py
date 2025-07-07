"""
input:
6 6 4

output:
4
"""

import math

def main():
    n, m, a = input().split()
    n, m, a = int(n), int(m), int(a)
    print(math.ceil(n/a) * math.ceil(m/a))

if __name__ == "__main__":
    main()