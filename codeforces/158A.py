"""
input:
8 5
10 9 8 7 7 7 5 5

output:
6
"""

def main():
    n, k = input().split()
    participants = list(map(int, input().split()))
    place = participants[int(k)-1]
    advancers = 0

    for participant in participants:
        if participant >= place and participant != 0:
            advancers += 1

    print(advancers)

if __name__ == "__main__":
    main()