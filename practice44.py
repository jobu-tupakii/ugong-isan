def sort_killer(text):
    words = text.split()
    words.sort(key=lambda x: (len(x),x))
    return ' '.join(words)

print(sort_killer("banana apple cat dog egg"))