def vowel_killer(text):
    text = text.lower()
    vowel = 'aeiou'
    result = 0

    for i in range(len(text)):
        if text[i] in vowel:
            result += 1

    return result

print(vowel_killer("Python is Awesome"))