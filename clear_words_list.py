import string


key_words = ["False", "await", "else", "import", "pass", "None", "break",
"except", "in", "raise", "True", "class", "finally", "is", "return", "and",
"continue", "for", "lambda", "try", "as", "def", "from", "nonlocal", "while",
"assert", "del", "global", "not", "with", "async", "elif", "if", "or", "yield",
"def"]


clear_word_list(words_list):
    words_list_clear = []
    for word in words_list:
        if word not in (list(string.punctuation)
                    and not in list(string.digits))
                    and not in key_words:
            words_list_clear.append(word)

