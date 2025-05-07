def sum_killer(text):
    num = []

    for c in text:
        if c.isnumeric():
            num.append(int(c))

    return sum(num)

print(sum_killer("a1b2c3"))