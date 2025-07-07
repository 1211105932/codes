def main():
    with open("adventofcode/2022/day4.txt") as f:
        lines = f.readlines()
        res, res2 = 0, 0
        for line in lines:
            line = line.strip().split(",")
            l1, h1 = map(int, line[0].split("-"))
            l2, h2 = map(int, line[1].split("-"))
            if l1 >= l2 and h1 <= h2 or l1 <= l2 and h1 >= h2:
                res += 1
            if not (l1 > h2 or h1 < l2):
                res2 += 1
        print(res)
        print(res2)

if __name__ == "__main__":
    main()