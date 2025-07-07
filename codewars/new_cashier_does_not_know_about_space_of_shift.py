def get_order(order):
    menu = [
        "burger",
        "fries",
        "chicken",
        "pizza",
        "sandwich",
        "onionrings",
        "milkshake",
        "coke"
    ]
    
    for i in range(len(menu)):
        order = order.replace(menu[i], str(i))
    
    return " ".join(menu[i].capitalize() for i in sorted(map(int, order)))