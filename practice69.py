def vowel_words(text):
    vowels = 'aeiou'
    words = text.split()
    result = []

    for word in words:
        w = word.lower()
        if w[0] in vowels and w[-1] in vowels:
            result.append(word)

    return result

text = "Apple is an umbrella or idea but not every egg"
print(vowel_words(text))
