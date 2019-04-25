class Counter(dict):
    def __missing__(self, key):
        return 0


word_list = ['ola', 'ola', 'boa', 'boa', 'bondadade', 'amor', 'diginidade',
             'amor', 'boa', 'justiça', 'liberdade', 'paciência', 'paciência']


def cont_frequency(word_list):
    counts = Counter()
    for word in word_list:
        counts[word] += 1
    return counts


counts = cont_frequency(word_list)
print(counts)
