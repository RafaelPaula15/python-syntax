def upper_words(words):
    """This function will change str to uppercase 
    and word must start with e or h"""
    
    for word in words:
        if word[0] != "e" and word[0] != "h":
            return "WORDS MUST START WITH E OR H"
        print(word.upper())

