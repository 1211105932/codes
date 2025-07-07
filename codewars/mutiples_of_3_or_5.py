def solution(number):
    return max(0, sum(n for n in range(number) if not n % 3 or not n % 5) )