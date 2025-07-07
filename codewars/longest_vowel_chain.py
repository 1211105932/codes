def solve(s):
    count = max_count = 0

    for i in s:
        if i in set("aeiou"):
            count += 1
            max_count = max(max_count, count)
        else:
            count = 0
            
    return max_count