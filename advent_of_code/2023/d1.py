def main():
    with open("day1.txt") as f:
        lines = f.readlines().strip('\n')

        for line in lines:
            for i, c in enumerate(line):
                if c.isDigit



        c = 'abcdefghijklmnopqrstuvwxyz'
        d = 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'
        sum = 0

        for line in lines:
            
            for ds in d:
                line = line.replace(ds, str(d.index(ds)+1))
            print(line)
            line = line.strip().strip(c)
            sum += int((line[0]) + (line[-1]))

        print(sum)

if __name__ == "__main__":
    main()