def expanded_form(num):
    num = str(num)
    return " + ".join(j + "0" * (len(num)-i-1) for i, j in enumerate(num) if j != "0")