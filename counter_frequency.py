class Counter(dict):
    def __missing__(self, key):
        return 0


counter = Counter()
word = 'banana'
counter[word] += 1
print(counter)
