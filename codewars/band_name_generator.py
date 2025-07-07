def band_name_generator(name):
    if name[0] == name[-1]:
        return f"{name.capitalize()}{name[1:]}"
    return f"The {name.capitalize()}"