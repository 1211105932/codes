def title_case(title, minor_words=''):
    minor_words = [x.lower() for x in minor_words.split()]
    return " ".join(j if i != 0 and j in minor_words else j.title() for i, j in enumerate(title.lower().split()))