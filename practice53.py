def five_star(text):
    result = []
    words = text.split()

    for c in words:
        if len(c) >= 5:
            result.append(c)

    return result

print(five_star("This is a simple python challenge for beginners"))