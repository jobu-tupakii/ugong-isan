def count_letters(text):
    from collections import defaultdict

    text = text.lower()
    counter = defaultdict(int)

    for c in text:
        if c.isalpha():
            counter[c] += 1

    return dict(sorted(counter.items()))

text = "Programming in Python is fun!"
print(count_letters(text))