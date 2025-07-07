def incrementer(nums):
    return [(j + i) % 10 for i, j in enumerate(nums, 1)]