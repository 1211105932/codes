"""
input:
R
s;;upimrrfod;pbr

output:
allyouneedislove
"""

def main():
    layout = "qwertyuiopasdfghjkl;zxcvbnm,./"
    direction = input()
    word = input()
    output = ""

    if direction == "L":
        for char in word:
            output += layout[layout.index(char)+1]
    elif direction == "R":
        for char in word:
            output += layout[layout.index(char)-1]

    print(output)

if __name__ == "__main__":
    main()