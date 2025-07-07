def printer_error(s):
    bad = 0
    for c in s:
        if ord(c) > ord("m"):
            bad += 1
    return f"{bad}/{len(s)}"