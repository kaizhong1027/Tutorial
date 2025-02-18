def first_letter(word):
    if not word or not isinstance(word, str):
        raise ValueError("Input must be a non-empty string")
    return word[0]