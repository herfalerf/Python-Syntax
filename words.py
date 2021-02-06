def print_upper_words(words, must_start_with):
    """turn a set of words to uppercase, will only print words that start with letters in a provided set"""

    
    for word in words:
        for letter in must_start_with:
            if word.startswith(letter):
                print (word.upper())