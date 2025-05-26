def alphaking(text):
    cleaned = []
    result = []
    lil_result = []

    for c in text:
        if c.isalpha():
            cleaned += c

    for i in cleaned:
        if i.isupper():
            result += i.lower()
        elif i.islower():
            result += i.upper()

    lil_result = sorted(result)

    return ''.join(lil_result)

print(alphaking("PyThon 3.9 IS AmaZing!"))