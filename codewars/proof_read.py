def proofread(st):
    return ". ".join(s.strip().lower().replace("ie", "ei").capitalize() for s in st.split(". "))