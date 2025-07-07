"""
input:
10
YES
yES
yes
Yes
YeS
Noo
orZ
yEz
Yas
XES

output:
YES
YES
YES
YES
YES
NO
NO
NO
NO
NO
"""

def main():
    n = int(input())
    output = ""
    for _ in range(n):
        word = input()
        if word.lower() == "yes":
            output += "YES\n"
        else:
            output += "NO\n"
 
    print(output)

if __name__ == "__main__":
    main()