from collections import Counter

from words_from_strings import words_from_string
from clear_words_list import clear_word_list


file_name = 'tutorial.txt'

with open(file_name, 'r') as reader:
    text = reader.read()


word_list = words_from_string(text)
clear_word_list = clear_word_list(word_list)
counts = Counter(clear_word_list)
top_words = counts.most_common(100)


for word, count in top_words:
    print("{}: {}".format(count, word))
