def xbonacci(signature, n):
    l = len(signature)
    
    for i in range(l, n):
        signature.append(sum(signature[i-l:i]))
    
    return signature[:n]