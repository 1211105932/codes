def main():
    n, m = list(map(int, input().split()))
    right = True
    for i in range(n):
        if i % 2 == 0:
            print("#"*m)
        elif right:
            print("."*(m-1) + "#")
            right = False
        elif not right:
            print("#" + "."*(m-1))
            right = True

if __name__ == "__main__":
    main()