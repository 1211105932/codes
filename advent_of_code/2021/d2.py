def main():
    with open("adventofcode/2021/day2.txt") as f:
        lines = f.readlines()
        lines = list(line.strip().split() for line in lines)
        hori = 0
        depth = 0
        for line in lines:
            if line[0][0] == "f":
                hori += int(line[1])
            elif line[0][0] == "d":
                depth += int(line[1])
            elif line[0][0] == "u":
                depth -= int(line[1])
        print(hori * depth)

if __name__ == "__main__":
    main()