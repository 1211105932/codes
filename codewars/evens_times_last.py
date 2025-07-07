def even_last(numbers): 
    if not numbers:
        return 0
    
    return sum(numbers[i] for i in range(0, len(numbers), 2)) * numbers[-1]