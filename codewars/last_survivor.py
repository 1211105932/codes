def last_survivor(letters, coords):
    letters = list(letters)
    for i in range(len(coords)):
        letters.pop(coords[i])
    
    return "".join(letters)