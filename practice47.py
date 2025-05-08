def reverse_master(text):
    result = []

    for c in text:
        if c.isupper():
            result.append(c.lower())
        else:
            result.append(c.upper())

    return ''.join(result)


print(reverse_master("HeLLo WoRLD"))
