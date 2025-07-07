"""
input:
4
word
localization
internationalization
pneumonoultramicroscopicsilicovolcanoconiosis

output:
word
l10n
i18n
p43s
"""

def main():
    words = []
    n = int(input())
    for _ in range(n):
        words.append(input())

    for word in words:
        if len(word) > 10:
            print(f"{word[0]}{len(word)-2}{word[-1]}")
        else:
            print(word)

if __name__ == "__main__":
    main()