def round_(n):
    if n < 0:
        return 0
    elif n > 255:
        return 255
    else:
        return n

def rgb(r, g, b):
    return "".join(f"{hex(round_(i)).upper()[2:]:0>2}" for i in (r, g, b))