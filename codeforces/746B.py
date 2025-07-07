"""
input:
5
logva

output:
volga
"""

def main():
    n = int(input())
    word = input()

    decoded = ""
    for i in range(n):
        if len(word) % 2 != 0:
            if i % 2 != 0:
                decoded = (word[i]) + decoded
            else:
                decoded = decoded + (word[i])
        else:
            if i % 2 == 0:
                decoded = (word[i]) + decoded
            else:
                decoded = decoded + (word[i])
    
    print(decoded)

if __name__ == "__main__":
    main()