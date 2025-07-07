def remove_rotten(bag_of_fruits):
    if not bag_of_fruits:
        return []
    
    return [f[6:].lower() if f.startswith("rotten") else f for f in bag_of_fruits]