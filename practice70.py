def filter_words(text):
    cleaned = ''
    for c in text:
        if c.isalpha() or c == ' ':
            cleaned += c

    words = cleaned.lower().split()
    result = [w for w in words if 4 <= len(w) <= 6]
    return result

text = "This is a simple, short sentence for Python learners!"
print(filter_words(text))