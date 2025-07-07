def arithmetic_sequence_elements(a, d, n):
    return ", ".join(str(a + i * d) for i in range(n))