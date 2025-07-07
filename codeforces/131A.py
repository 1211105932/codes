"""
cAPS

Caps
"""

def main():
    word = input()
    if word[1:].isupper() or len(word) == 1:
        print(word.capitalize())
    else:
        print(word)

if __name__ == "__main__":
    main()