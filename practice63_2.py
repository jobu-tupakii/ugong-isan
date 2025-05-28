def ditto_finder2(text1, text2):
    if len(text1) != len(text2):
        return False
    return text2 in (text1 + text2)

text1 = "hello"
text2 = "olleh"

print(ditto_finder2(text1, text2))