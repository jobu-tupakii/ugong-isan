def dick_funks_ver3(text):
    my_dict = {}
    cleaned = ''
    first = text.lower()

    for c in first:
        if c.isalpha() or c == ' ':
            cleaned += c

    words = cleaned.split()

    for i in words:
        if i in my_dict:
            my_dict[i] += 1
        else:
            my_dict[i] = 1

    sorted_dict = dict(sorted(my_dict.items(), key=lambda x: (-x[1], x[0])))

    return sorted_dict

text = "This is a test. This test is only a test!"
print(dick_funks_ver3(text))