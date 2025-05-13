def longest_detector(text):
    longest = ""
    words = text.split()

    for c in words:
        if len(c) > len(longest):
            longest = c

        elif len(c) == len(longest):
            if c > longest:
                longest = longest
            elif c < longest:
                longest = c

    return longest

print(longest_detector("apple banana pear watermelon mango housekeeping"))