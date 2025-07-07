with open("input", "r") as f:
    lines = f.readlines()


def safe_check(arr):
    if arr[0] == min(arr):
        if arr != sorted(arr):
            return False
    elif arr[0] == max(arr):
        if arr != sorted(arr, reverse=True):
            return False
    else:
        return False
    
    for i in range(1, len(arr)):
        diff = abs(arr[i] - arr[i - 1])
        if diff < 1 or diff > 3:
            return False

    return True


count1 = count2 = 0
for line in lines:
    data = list(map(int, line.split()))
    datas = [data[:i] + data[i + 1:] for i in range(len(data))]

    if safe_check(data):
        count1 += 1

    if any(safe_check(i) for i in datas):
        count2 += 1

print(f"count1: {count1}")
print(f"count2: {count2}")