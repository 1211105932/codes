def vowel_2_index(string):
    return "".join(str(i) if j in set("aeiouAEIOU") else j for i, j in enumerate(string, 1))