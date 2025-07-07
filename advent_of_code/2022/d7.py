def main():
    with open("adventofcode/2022/testt.txt") as f:
        lines = f.readlines()
        system = {}
        path = []
        for line in lines:
            line = line.split()
            if line[0] == "$":
                if line[1] == "cd":
                    if line[2] == "..":
                        path.pop()
                    elif line[2] == "/":
                        path = []
                    else:
                        path.append(line[2])
            else:
                if line[0] == "dir":
                    continue
                try:
                    for i in range(len(path)+1):
                        system[("/".join(path[:i]))] += int(line[0])
                except:
                    system[("/".join(path))] = 0
                    for i in range(len(path)+1):
                        system[("/".join(path[:i]))] += int(line[0])
        res = 0
        for value in system.values():
            if value <= 100000:
                res += value
        print(res)
    
if __name__ == "__main__":
    main()