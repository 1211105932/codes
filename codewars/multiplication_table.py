def multiplication_table(size):
    arr = []
    for i in range(1, size+1):
        row = []
        for j in range(1, size+1):
            row.append(i * j)
        arr.append(row)
    return arr