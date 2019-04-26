from collections import defaultdict


def cont_frequency(word_list):
    counts = defaultdict(int)
    for word in word_list:
        counts[word] += 1
    return counts
