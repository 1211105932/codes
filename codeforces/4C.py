"""
input:
4
abacaba
acaba
abacaba
acab

output:
OK
OK
abacaba1
OK
"""

def main():
    names = {}
    output = ""
    n = int(input())
    
    for _ in range(n):
        name = input()
        if name in names.keys():
            names[name] += 1
            output += f"{name}{names[name]}\n"
        else:
            names[name] = 0
            output += "OK\n"

    print(output)

if __name__ == "__main__":
    main()