"""
ahhellllloou

YES
"""

def main():
    word = input()
    hello = "hello"
    count = 0
    
    for char in word:
        if count == 5:
            break
        if char == hello[count]:
            count += 1
        
    if count==5:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    main()