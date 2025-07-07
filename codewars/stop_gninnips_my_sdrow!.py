def spin_words(sentence):
    return " ".join(w if len(w) < 5 else w[::-1] for w in sentence.split())