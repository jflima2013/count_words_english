from counter_frequency import cont_frequency

text = "But I didn't inhale, he said (emphatically)"

word_list = ['ola', 'ola', 'boa', 'boa', 'bondadade', 'amor', 'diginidade',
             'amor', 'boa', 'justiça', 'liberdade', 'paciência', 'paciência']

counts = cont_frequency(word_list)

for k, v in counts.items():
    k, v = v, k
    print("%s: %s" % (k, v))
