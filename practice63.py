def ditto_finder(text1, text2):
    return bool(text1 == text2[::-1])

text1 = "hello"
text2 = "olleh"

print(ditto_finder(text1, text2))