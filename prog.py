from counter_frequency import cont_frequency
from words_from_strings import words_from_string
import string


text = "But I didn't inhale, he said (emphatically)"

file_name = '/home/jfk/pickaxe/tut_containers/word_freq/books/\
programming_ruby.txt'

with open(file_name, 'r') as reader:
    text = reader.read()

text = text.translate(str.maketrans('', '', string.punctuation))

word_list = words_from_string(text)
counts = cont_frequency(word_list)
print(len(word_list))
print(len(counts))

count = 0
for word in sorted(counts, key=counts.get, reverse=True):
    # print("%s: %s" % (counts[word], word))
    print("%s: %s" % (word, counts[word]))
    if count == 100:
        break
    count += 1

# exchange_counts = exchange_key_value(counts)
# print(len(exchange_counts))
