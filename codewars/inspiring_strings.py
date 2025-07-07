def longest_word(string_of_words):
    return sorted(string_of_words.split(), key=len)[-1]