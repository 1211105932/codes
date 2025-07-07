"""
.-.--

012
"""

def main():
    code = input()
    code += "dummy"

    decoded = ""

    for i in range(len(code)):
        if code[i] == ".":
            decoded += "0"
        else:
            if code[i] != "-":
                break
            if code[i+1] == ".":
                decoded += "1"
            else:
                decoded += "2"
            i += 1
        
    print(decoded)

if __name__ == "__main__":
    main()