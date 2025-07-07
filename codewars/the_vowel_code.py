vowels = "aeiou"

def encode(st):
    return "".join(str(vowels.index(c) + 1) if c in vowels else c for c in list(st))
    
def decode(st):
    return "".join(vowels[int(c) - 1] if c.isdigit() else c for c in list(st))