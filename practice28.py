def alphareversemachine(text) :
    letter = [c for c in text if c.isalpha()]
    result = []

    for c in text:
        if c.isalpha():
            result.append(letter.pop())
        else:
            result.append(c)

    return ''.join(result)

print(alphareversemachine("a1b2c3d4!"))