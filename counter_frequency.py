class Counter(dict):
    def __missing__(self, key):
        return 0


word_list = ['ola', 'ola', 'boa', 'boa', 'bondadade', 'amor', 'diginidade',
             'amor', 'boa']

counts = Counter()
for word in word_list:
    counts[word] += 1

print(counts)

# word = 'felicidade'
# counts[word] += 1
# print(counts)
