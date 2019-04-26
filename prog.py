from counter_frequency import cont_frequency

text = "But I didn't inhale, he said (emphatically)"

word_list = ['ola', 'ola', 'boa', 'boa', 'bondadade', 'amor', 'diginidade',
             'amor', 'boa', 'justiça', 'liberdade', 'paciência', 'paciência']

counts = cont_frequency(word_list)

for word in sorted(counts, key=counts.get, reverse=True):
    k, v = word, counts[word]
    print("%s: %s" % (v, k))
