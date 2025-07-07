def max_gap(numbers):
    numbers = sorted(numbers)
    return max(abs(numbers[i-1] - numbers[i]) for i in range(1, len(numbers)))