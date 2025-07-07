def main():
    with open("adventofcode/2021/day1.txt") as f:
        lines = f.readlines()
        prev = int(lines[0].strip())
        res = 0
        for line in lines:
            line = int(line.strip())
            if line > prev:
                res += 1
            prev = line
        print(res)

if __name__ == "__main__":
    main()