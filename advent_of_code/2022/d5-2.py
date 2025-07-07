def main():
    with open("adventofcode2022/day5.txt") as f:
        lines = f.readlines()
        stacks = [
        [],
        ["B", "W", "N"],
        ["L", "Z", "S", "P", "T", "D", "M", "B"],
        ["Q", "H", "Z", "W", "R"],
        ["W", "D", "V", "J", "Z", "R"],
        ["S", "H", "M", "B"],
        ["L", "G", "N", "J", "H", "V", "P", "B"],
        ["J", "Q", "Z", "F", "H", "D", "L", "S"],
        ["W", "S", "F", "J", "G", "Q", "B"],
        ["Z", "W", "M", "S", "C", "D", "J"]
        ]
        for line in lines[10:]:
            num, pos, pos2 = [int(s) for s in line.split() if s.isdigit()]
            stacks[pos2].extend(stacks[pos][-num:])
            del stacks[pos][-num:]
        print(*[stack[-1] for stack in stacks[1:]], sep="")
        
        stacks = [
        [],
        ["B", "W", "N"],
        ["L", "Z", "S", "P", "T", "D", "M", "B"],
        ["Q", "H", "Z", "W", "R"],
        ["W", "D", "V", "J", "Z", "R"],
        ["S", "H", "M", "B"],
        ["L", "G", "N", "J", "H", "V", "P", "B"],
        ["J", "Q", "Z", "F", "H", "D", "L", "S"],
        ["W", "S", "F", "J", "G", "Q", "B"],
        ["Z", "W", "M", "S", "C", "D", "J"]
        ]
        for line in lines[10:]:
            num, pos, pos2 = [int(s) for s in line.split() if s.isdigit()]
            for _ in range(num):
                stacks[pos2].append(stacks[pos].pop())
        print(*[stack[-1] for stack in stacks[1:]], sep="")

if __name__ == "__main__":
    main()