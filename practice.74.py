def remove_vowels(text):
    vowels = "aeiou"
    result = ''

    for c in text.lower():
        if c not in vowels:
            result += c

    return result

text = "Beautiful day in the Neighborhood!"
print(remove_vowels(text))