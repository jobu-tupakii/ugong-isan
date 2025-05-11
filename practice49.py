def palindrome_finder(text):
    cleaned = ''

    for c in text:
        if c.isalpha():
            cleaned += c.lower()

    return cleaned == cleaned[::-1]

print(palindrome_finder("A man, a plan, a canal: Panama"))