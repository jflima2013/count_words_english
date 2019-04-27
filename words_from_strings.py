import nltk


def words_from_string(text):
    text = text.lower()
    return nltk.word_tokenize(text)
