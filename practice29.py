def duplication_killer(text) :
    seen = set()
    result = []

    for c in text:
        if c not in seen:
            seen.add(c)
            result.append(c)

    return ''.join(result)

print(duplication_killer("banana"))