def longest_dragon(text) :
    sp = text.split()
    longest = ''

    for word in sp:
        if len(word) > len(longest):
            longest = word
        elif len(word) == len(longest) and word < longest:
            longest = word

    return longest

print(longest_dragon("cat elephant dog"))