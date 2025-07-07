def main():
    def game_manager(opponent, player):
        score = 0
        if player == "rock":
            score += 1
        elif player == "paper":
            score += 2
        elif player == "scissors":
            score += 3
        if player == opponent:
            score += 3
        elif player == "rock" and opponent == "scissors" or player == "paper" and opponent == "rock" or player == "scissors" and opponent == "paper":
            score += 6
        else:
            score += 0
        return score

    def read(s):
        rock = "A"
        paper = "B"
        scissors = "C"
        if s in rock:
            return "rock"
        elif s in paper:
            return "paper"
        elif s in scissors:
            return "scissors"
        if s == "X":
            do = 0
        elif s == "Y":
            do = 1
        elif s == "Z":
            do = 2
        return do

    def pick(opponent, code):
        if code == 1:
            return opponent
        elif code == 0 and opponent == "paper" or code == 2 and opponent == "scissors":
            return "rock"
        elif code == 0 and opponent == "scissors" or code == 2 and opponent == "rock":
            return "paper"
        elif code == 0 and opponent == "rock" or code == 2 and opponent == "paper":
            return "scissors"

    with open("adventofcode2022/day2.txt") as f:
        lines = f.readlines()
        res = 0
        for line in lines:
            line = line.strip()
            res += game_manager(read(line[0]), pick(read(line[0]), read(line[-1])))
        print(res)

if __name__ == "__main__":
    main()