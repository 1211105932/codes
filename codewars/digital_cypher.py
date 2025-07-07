def encode(message, key):
    key = str(key)
    return [ord(j) - ord("a") + 1 + int(key[i % len(key)]) for i, j in enumerate(message)]