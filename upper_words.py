def upper_words(words):
    """This function will change str to uppercase 
    and word must start with h or e"""
    for word in words:
        if word[0] == "h" or word[0] == "e":
            print(word.upper())