def evaporator(content, evap_per_day, threshold):
    evap_per_day = 1 - evap_per_day / 100
    threshold = content * threshold / 100
    
    count = 0
    while content > threshold:
        content *= evap_per_day
        count += 1
        
    return count