"""
input:
1
++X

output:
1
"""

def main():
    operations = []
    n = int(input())
    for _ in range(n):
        operations.append(input())
    value = 0

    for operation in operations:
        if operation in ("++X", "X++"):
            value += 1
        elif operation in ("--X", "X--"):
            value -= 1
    
    print(value)

if __name__ == "__main__":
    main()