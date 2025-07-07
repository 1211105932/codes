"""
5
100 50 200 150 200

2
"""

def main():
    n = int(input())
    points = list(map(int, input().split()))

    lowest = points[0]
    highest = points[0]
    count = 0

    for point in points:
        if point < lowest:
            lowest = point
            count += 1
        elif point > highest:
            highest = point
            count += 1
    
    print(count)

if __name__ == "__main__":
    main()