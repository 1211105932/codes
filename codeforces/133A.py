"""
input:
HI!

output:
YES
"""
def main():
    p = list(input())
    output = False

    for character in p:
        if character in ("HQ9"):
            output = True
            break

    if output:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    main()