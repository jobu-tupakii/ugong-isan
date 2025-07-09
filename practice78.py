def sort_unique_words(text):
    cleaned = ''
    for c in text:
        if c.isalpha() or c == ' ':
            cleaned += c

    words = cleaned.lower().split()
    unique = sorted(set(words))
    return unique

text = "Hello, Python world! Hello coding."
print(sort_unique_words(text))