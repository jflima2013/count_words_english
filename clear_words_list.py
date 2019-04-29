import string


punctuations = list(string.punctuation)
digits = list(string.digits)

key_words = [
    "False", "await", "else", "import", "pass", "None", "break",
    "except", "in", "raise", "True", "class", "finally", "is",
    "return", "and", "continue", "for", "lambda", "try", "as",
    "def", "from", "nonlocal", "while", "assert", "del",
    "global", "not", "with", "async", "elif", "if", "or",
    "yield", "def"
    ]

unwanted_words = ["’"]
words_already_known = []


words_not_allowed = punctuations + digits + key_words + unwanted_words + \
                     words_already_known


def clear_word_list(words_list):
    words_list_clear = []
    for word in words_list:
        if word not in words_not_allowed and len(word) <= 4:
            words_list_clear.append(word)
    return words_list_clear
