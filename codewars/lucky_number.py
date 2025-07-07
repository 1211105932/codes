def is_lucky(n):
    return not sum(map(int, list(str(n)))) % 9