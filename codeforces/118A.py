"""
input:
tour

output:
.t.r
"""

def main():
    word = input().lower()
    output = ""
    
    for char in word:
        if char not in ("aeiouy"):
            output += f".{char}"

    print(output)

if __name__ == "__main__":
    main()