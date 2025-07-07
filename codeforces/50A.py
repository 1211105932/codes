"""
input:
2 4

output:
4
"""

import math

def main():
    m, n = input().split()
    squares = int(m) * int(n)
    dominoes = math.floor(squares / 2)
    print(dominoes)

if __name__ == "__main__":
    main()