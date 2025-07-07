def main():
    n = int(input())
    p = list(map(int, input().split()))[1:]
    q = list(map(int, input().split()))[1:]
    level = [i for i in range(1, n+1) if i not in p and i not in q]

    if len(level) == 0:
        print("I become the guy.")
    else:
        print("Oh, my keyboard!")

if __name__ == "__main__":
    main()