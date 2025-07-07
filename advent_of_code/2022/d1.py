def main():
    with open("adventofcode/2022/day1.txt") as f:
        lines = f.readlines()
        res, res2, res3 = 0, 0, 0
        cur_sum = 0
        for line in lines:
            line = line.strip()
            if line != "":
                cur_sum += int(line)
            else:
                if cur_sum > res:
                    res3 = res2
                    res2 = res
                    res = cur_sum  
                elif cur_sum > res2:
                    res3 = res2
                    res2 = cur_sum
                elif cur_sum > res3:
                    res3 = cur_sum
                cur_sum = 0
        print(res)
        print(res+res2+res3)

if __name__ == "__main__":
    main()