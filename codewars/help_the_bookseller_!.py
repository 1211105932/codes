def stock_list(list_of_art, list_of_cat):
    if not list_of_art or not list_of_cat:
        return ""
    
    dict = {}
    for i in list_of_art:
        code, quantity = i.split()
        dict[code[0]] = dict.get(code[0], 0) + int(quantity)
    
    return " - ".join(f"({i} : {dict.get(i, 0)})" for i in list_of_cat)