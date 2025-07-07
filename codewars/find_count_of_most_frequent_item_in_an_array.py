from collections import Counter

def most_frequent_item_count(collection):
    if not collection:
        return 0
    
    return Counter(collection).most_common()[0][1]