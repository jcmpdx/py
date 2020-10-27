def pig_latin(text):
    say = []
    # Separate the text into words
    words = text.split()
    for word in words:
        # Create the pig latin word and add it to the list
        word = '{}{}ay'.format(word[1:], word[0])
        say.append(word)
        # Turn the list back into a phrase
    return ' '.join(say)