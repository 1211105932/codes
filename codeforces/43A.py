"""
input:
1
ABC

output:
ABC
"""

def main():
    team = {}
    n = int(input())

    for _ in range(n):
        goal = input()
        if goal in team.keys():
            team[goal] += 1
        else:
            team[goal] = 0

    print(max(team, key=team.get))

if __name__ == "__main__":
    main()