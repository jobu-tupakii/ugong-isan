def title_case_converter(text):
    words = text.split()
    result = []

    for word in words:
        if word:
            first = word[0].upper()
            rest = word[1:].lower()
            result.append(first + rest)
        else:
            result.append('')

    return ' '.join(result)

text = "hELLo, WOrLD! thIS is PYthon."
print(title_case_converter(text))
