def two_decimal_places(number):
    x, y = str(number).split(".")
    return float(f"{x}.{y[:2]}")