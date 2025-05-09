def word_hunter(text, word) :
    text = text.lower()
    word = word.lower()
    words = text.split()
    count = 0

    for c in words:
        if c == word:
            count += 1

    return count

print(word_hunter("Python is fun. python is powerful. PYTHON is easy to learn.", "python"))
