def compress_consonants(text):
    vowels = 'aeiouAEIOU'
    no_vowels = ''

    for char in text:
        if char not in vowels:
            no_vowels += char

    result = ''
    prev_char = ''

    for char in no_vowels:
        if char != prev_char or char == ' ':
            result += char
        prev_char = char

    return result

text = "Soooonnnnerrr orrr laaaater"
print(compress_consonants(text))
