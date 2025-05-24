def ditto_letters(text1, text2):
    clean1 = set(c for c in text1.lower() if c.isalpha())
    clean2 = set(c for c in text2.lower() if c.isalpha())

    ditto = sorted(clean1 & clean2)

    return ditto

text1 = "Hello, World!"
text2 = "Hold the door."

print(ditto_letters(text1, text2))