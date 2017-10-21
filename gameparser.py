"""File that breaks down input to core components for commands and removes punctuation from  battle input and raps."""


import string

# List of "unimportant" words (feel free to add more)
skip_words = ['a', 'about', 'all', 'an', 'another', 'any', 'around', 'at',
              'bad', 'beautiful', 'been', 'better', 'big', 'can', 'every', 'for',
              'from', 'good', 'have', 'her', 'here', 'hers', 'his', 'how',
              'i', 'if', 'in', 'into', 'is', 'it', 'its', 'large', 'later',
              'like', 'little', 'main', 'me', 'mine', 'more', 'my', 'now',
              'of', 'off', 'oh', 'on', 'please', 'small', 'some', 'soon',
              'that', 'the', 'then', 'this', 'those', 'through', 'till', 'to',
              'towards', 'until', 'us', 'want', 'we', 'what', 'when', 'why',
              'wish', 'with', 'would']


def filter_words(words, skip_words):
    """Removes unnessesary words via the skip works list."""
    filtered_input = []
    for item in words:
        if item not in skip_words:
            filtered_input.append(item)
        else:
            pass
    return filtered_input


def remove_punct(text):
    """Removes the punctuation from a string."""
    no_punct = ""
    for char in text:
        if not (char in string.punctuation):
            no_punct = no_punct + char
    return no_punct


def remove_spaces(text):
    """This function is used to remove leading and trailing spaces from a string."""
    text = text.lstrip()
    text = text.rstrip()
    return text


def normalise_input(user_input, is_rap):
    """The main function for standardising input. If a rap, the code."""
    # Remove punctuation and convert to lower case
    no_punct = remove_punct(user_input).lower()
    no_punct = remove_spaces(no_punct)
    if is_rap == True:
        no_punct = filter_words(no_punct.split(), [])
    else:
        no_punct = filter_words(no_punct.split(), skip_words)

    return no_punct
