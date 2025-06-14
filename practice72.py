def vowel_picker(text):
    vowels = "aeiou"
    result = set()

    for c in text.lower():
        if c in vowels:
            result.add(c)

    return sorted(result)

text = "Beautiful Day in the Neighborhood!"
print(vowel_picker(text))
