def unique_strings(words):
    unique_chars = []
    for char in words:
        if char not in unique_chars:
            unique_chars.append(char)
    return unique_chars

