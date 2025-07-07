"""
input:
2
5 7

output:
2 5
"""

def main():
    n = int(input())
    bidders = list(map(int, input().split()))

    bidder = bidders.index(max(bidders))
    bidders.pop(bidder)
    price = max(bidders)

    print(f"{bidder + 1} {price}")

if __name__ == "__main__":
    main()