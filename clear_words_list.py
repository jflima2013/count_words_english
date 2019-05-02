import string
from itertools import chain


punctuations = tuple(string.punctuation)
digits = tuple(string.digits)

key_words = (
    "False", "await", "else", "import", "pass", "None", "break",
    "except", "in", "raise", "True", "class", "finally", "is",
    "return", "and", "continue", "for", "lambda", "try", "as",
    "def", "from", "nonlocal", "while", "assert", "del",
    "global", "not", "with", "async", "elif", "if", "or",
    "yield", "def"
    )

unwanted_words = ("www")
words_already_known = ('python')


words_not_allowed = set(chain(
    punctuations,
    digits,
    key_words,
    unwanted_words,
    words_already_known
    ))


def clear_word_list(words_list):
    for word in words_list:
        size_criteria = len(word) > 1
        if word not in words_not_allowed and size_criteria:
            yield word
