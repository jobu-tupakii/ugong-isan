def roggugeo2(text):
    words = text.split()
    reversed_words = [word[::-1] for word in words]
    return ' '.join(reversed_words)

print(roggugeo2("Python is fun"))