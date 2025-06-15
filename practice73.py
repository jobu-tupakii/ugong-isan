def sum_numbers(text):
    num = ''
    total = 0

    for c in text:
        if c.isdigit():
            num += c
        else:
            if num:
                total += int(num)
                num = ''

    if num:
        total += int(num)

    return total


text = "There are 12 apples, 30 bananas, and 7 mangoes."
print(sum_numbers(text))