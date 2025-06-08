def sort_words_by_length(text):
    words = text.split()
    sorted_words = sorted(words, key=lambda x: (len(x), x.lower()))
    return sorted_words

text = "banana apple kiwi grape plum"
print(sort_words_by_length(text))