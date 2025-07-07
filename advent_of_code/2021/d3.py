def main():
    with open("adventofcode/2021/day3.txt") as f:
        lines = f.readlines()
        gamma_rate = ""
        for i in range(len(lines[0].strip())):
            num0, num1 = 0, 0
            for line in lines:
                if line[i] == "0":
                    num0 += 1
                elif line[i] == "1":
                    num1 += 1
            gamma_rate += ("0" if num0 > num1 else "1")
        epsilon_rate = "".join("0" if char == "1" else "1" for char in gamma_rate)
        gamma_rate = int(gamma_rate, 2)
        epsilon_rate = int(epsilon_rate, 2)
        print(gamma_rate * epsilon_rate)

if __name__ == "__main__":
    main()