def dick_funks_ver2(text):
    my_dict = {}
    cleaned = ''

    for c in text:
        if c.isalpha() or c == ' ':
            cleaned += c

    words = cleaned.split()

    for i in words:
        if len(i) in my_dict:
            my_dict[len(i)] += 1
        else:
            my_dict[len(i)] = 1

    return my_dict

print(dick_funks_ver2("This is a test. This test is easy!"))