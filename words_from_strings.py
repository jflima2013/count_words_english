import re


def words_from_string(string):
    string = string.lower()
    return re.split(r"\w'+", string)


str = "But I didn't inhale, he said (emphatically)"
print(words_from_string(str))
