def main():
    s = "_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    with open("adventofcode2022/day3.txt") as f:
        lines = f.readlines()
        res = 0
        line_count = 0
        lst = []
        for line in lines:
            line = line.strip()
            lst.append(line)
            line_count += 1
            if line_count == 3:
                dup = list(set(set(lst[0]).intersection(lst[1])).intersection(lst[2]))
                res += s.index(dup[0])
                lst.clear()
                line_count = 0
        print(res)

if __name__ == "__main__":
    main()