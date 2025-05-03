def extract_even_index_digits(s):
    result = ''
    for i in range(0, len(s), 2) :
        result += s[i]
    return result

print(extract_even_index_digits("1234567"))