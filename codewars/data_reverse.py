from itertools import chain

def data_reverse(data):
    size = 8
    
    chunks = [data[i:i+size] for i in range(0, len(data), size)]
    
    return list(chain(*chunks[::-1]))