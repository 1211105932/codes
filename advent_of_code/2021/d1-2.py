def main():
    with open("adventofcode/2021/day1.txt") as f:
        lines = f.readlines()
        lines = list(map(int, (line for line in lines)))
        a, b, c = 0, 1, 2
        res = 0
        for _ in range(len(lines)-3):
            if lines[a+1] + lines[b+1] + lines[c+1] > lines[a] + lines[b] + lines[c]:
                res += 1
            a += 1
            b += 1
            c += 1
        print(res)

if __name__ == "__main__":
    main()