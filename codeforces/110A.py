"""
input:
40047

output:
NO
"""

def main():
    n = input()
    count = 0
    for char in n:
        if char in ("47"):
            count += 1
    
    if count == 4 or count == 7:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    main()