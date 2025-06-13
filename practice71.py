def char_index_finder(text, char):
    text = text.lower()
    char = char.lower()
    return [i for i, c in enumerate(text) if c == char]

text = "Python is pretty powerful!"
char = "p"
print(char_index_finder(text, char))