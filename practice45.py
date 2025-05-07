def four_killer(text):
    words = text.split()
    result = []

    for c in words:
        if len(c) >= 4:
            result.append(c)

    return result

print(four_killer("this is a simple python test"))
