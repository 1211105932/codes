import datetime

def unlucky_days(year):
    count = 0
    
    for month in range(1, 13):
        if datetime.date(year, month, 13).weekday() == 4:
            count += 1
            
    return count