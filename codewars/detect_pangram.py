def is_pangram(st):
    return len(list(set(x for x in st.lower() if x.isalpha()))) == 26