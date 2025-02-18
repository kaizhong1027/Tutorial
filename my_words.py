def first_letter(word):
    if not word or not isinstance(word, str):
        raise ValueError("Input must be a non-empty string")
    return word[0]

def mid_letter(word):
    if not isinstance(word, str) or not word:
        raise ValueError("Input must be a non-empty string")

    length = len(word)
    mid_index = length // 2

    if length % 2 == 0:  # Even length, return two middle characters
        print("Middle letters:", word[mid_index - 1: mid_index + 1])
    else:  # Odd length, return one middle character
        print("Middle letter:", word[mid_index])