def longest_word(text):
    cleaned = ''
    for c in text:
        if c.isalpha() or c == ' ':
            cleaned += c

    words = cleaned.lower().split()
    max_len = max(len(word) for word in words)
    candidates = [w for w in words if len(w) == max_len]
    return min(candidates)

text = "Learning Python is enjoyable and informative!"
print(longest_word(text))