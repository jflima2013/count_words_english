class Counter(dict):
    def __missing__(self, key):
        return 0


def cont_frequency(word_list):
    counts = Counter()
    for word in word_list:
        counts[word] += 1
    return counts
