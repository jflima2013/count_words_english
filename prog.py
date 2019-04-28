import string
from counter_frequency import cont_frequency
from words_from_strings import words_from_string


file_name = '/home/jfk/pickaxe/tut_containers/word_freq/books/\
programming_ruby.txt'

with open(file_name, 'r') as reader:
    text = reader.read()

text = text.translate(str.maketrans('', '', string.punctuation))
text = text.translate(str.maketrans('', '', string.digits))
# apenas letras
# palavras chave python
# letras sozinhas
# palavras que eu ja conheço

word_list = words_from_string(text)
counts = cont_frequency(word_list)

quantity_items_left = 100
count = 0
for word in sorted(counts, key=counts.get, reverse=True):
    print("%s: %s" % (word, counts[word]))
    if count == quantity_items_left:
        break
    count += 1
