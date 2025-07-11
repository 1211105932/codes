def fold_to(distance):
    if distance < 0:
        return None
    
    thickness = 0.0001
    count = 0
    
    while thickness < distance:
        thickness *= 2
        count += 1

    return count