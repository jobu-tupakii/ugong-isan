def numeric_detective(s):
    digit = []
    for char in s:
        if char.isnumeric():
            digit.append(char)
    return int(''.join(digit))

input = "a1b2c3d45e"
print(numeric_detective(input))
