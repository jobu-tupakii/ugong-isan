def max_alpha(text) :
    text = text.lower()
    freq = {}

    for c in text:
        if c.isalpha() :
            if c in freq:
                freq[c] += 1
            else:
                freq[c] = 1

    max_count = max(freq.values())

    result = None
    for char in freq:
        if freq[char] == max_count:
            if result is None or char < result:
                result = char
    return result

print(max_alpha("This is a test sentence"))