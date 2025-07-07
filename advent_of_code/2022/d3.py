def main():
    s = "_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    with open("adventofcode/2022/day3.txt") as f:
        lines = f.readlines()
        res = 0
        for line in lines:
            line = line.strip()
            lst1 = line[:len(line)//2]
            lst2 = line[len(line)//2:]
            dup = list(set(lst1).intersection(lst2))
            res += s.index(dup[0])
        print(res)

if __name__ == "__main__":
    main()