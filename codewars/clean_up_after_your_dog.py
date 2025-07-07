def crap(garden, bags, cap):
    cap *= bags
    
    for i in garden:
        for j in i:
            if j == "D":
                return "Dog!!"
            elif j == "@":
                cap -= 1
    
    return "Cr@p" if cap < 0 else "Clean"