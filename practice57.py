def dick_funks(text):
    my_dict = {}
    cleaned = ''

    for c in text:
        if c.isalpha() or c == ' ':
            cleaned += c

    words = cleaned.split()

    for i in words:
        if i in my_dict:
            my_dict[i] += 1
        else:
            my_dict[i] = 1

    return my_dict

print(dick_funks("This is a test. This test is easy!"))