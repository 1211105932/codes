def bingo(ticket,win):
    count = 0
    for i in ticket:
        if i[1] in set(ord(c) for c in i[0]):
            count += 1
    
    return "Winner!" if count >= win else "Loser!"