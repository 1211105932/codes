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
        rock = "AX"
        paper = "BY"
        scissors = "CZ"
        if s in rock:
            return "rock"
        elif s in paper:
            return "paper"
        elif s in scissors:
            return "scissors"

    with open("adventofcode/2022/day2.txt") as f:
        lines = f.readlines()
        res = 0
        for line in lines:
            line = line.strip()
            res += game_manager(read(line[0]), read(line[-1]))
        print(res)

if __name__ == "__main__":
    main()