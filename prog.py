from counter_frequency import cont_frequency
from words_from_strings import words_from_string

text = "But I didn't inhale, he said (emphatically)"

file_name = '/home/jfk/pickaxe/tut_containers/word_freq/books/\
programming_ruby.txt'

with open(file_name, 'r') as reader:
    text = reader.read()

word_list = words_from_string(text)

counts = cont_frequency(word_list)

for word in sorted(counts, key=counts.get, reverse=True):
    k, v = word, counts[word]
    # print("%s: %s" % (v, k))
