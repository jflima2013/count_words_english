# import nltk
import re


def words_from_string(text):
    text = text.lower()
    return re.findall(r'\w+', text)
    # return nltk.word_tokenize(text)
