def is_palindrome(x):
    return x == x[::-1]

def main():
    n = 999
    max_ = 0

    for i in range(n, 1, -1):
        for j in range(n, 1, -1):
            if is_palindrome(str(i * j)):
                max_ = max(max_, i * j)
    
    return max_

if __name__ == "__main__":
    output = main()
    print(output)