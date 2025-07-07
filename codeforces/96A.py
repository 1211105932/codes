"""
input:
001001

output:
NO
"""

def main():
    players = list(input())
    last_player = None
    team = 0
    
    for player in players:
        if last_player != player:
            last_player = player
            team = 0
        team += 1

        if team >= 7:
            print("YES")
            break

    if team < 7:
        print("NO")

if __name__ == "__main__":
    main()