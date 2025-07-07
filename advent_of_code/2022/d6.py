def main():
    with open("adventofcode/2022/day6.txt") as f:
        line = f.readline()
        p1 = 4
        p2 = 14
        done = False
        while True:
            if len(set(line[p1-4:p1])) == 4 and not done:
                done = True
                print(p1)
            if len(set(line[p2-14:p2])) == 14:
                print(p2)
                break
            p1 += 1
            p2 += 1

if __name__ == "__main__":
    main()