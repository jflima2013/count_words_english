import string
from counter_frequency import cont_frequency
from words_from_strings import words_from_string
from clear_words_list import clear_word_list


file_name = 'tutorial.txt'

with open(file_name, 'r') as reader:
    text = reader.read()

# text = text.translate(str.maketrans('', '', string.punctuation))
# text = text.translate(str.maketrans('', '', string.digits))

word_list = words_from_string(text)
clear_word_list = clear_word_list(word_list)
counts = cont_frequency(clear_word_list)

quantity_items_left = 20
count = 0
for word in sorted(counts, key=counts.get, reverse=True):
    print("%s: %s" % (word, counts[word]))
    if count == quantity_items_left:
        break
    count += 1
