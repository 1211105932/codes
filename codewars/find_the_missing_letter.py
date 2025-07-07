def find_missing_letter(chars):
    chars = [ord(c) for c in chars]
    for x in range(chars[0], chars[-1]):
        if x not in chars:
            return chr(x)