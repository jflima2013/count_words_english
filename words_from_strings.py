import nltk


def words_from_string(text):
    text = text.lower()
    return nltk.word_tokenize(text)


# str = "hello seattle what have you got"
# str += "But I didn't inhale, he said (emphatically)"
# str += "I wouldn't've done that."
# print(words_from_string(str))
