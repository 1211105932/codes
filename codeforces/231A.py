"""
input:
3
1 1 0
1 1 1
1 0 0

output:
2
"""

def main():
    problems = []
    solution = 0
    n = int(input())
    for _ in range(n):
        problems.append(list(map(int, input().split())))

    for problem in problems:
        if sum(problem) > 1:
            solution += 1

    print(solution)

if __name__ == "__main__":
    main()