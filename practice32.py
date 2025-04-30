def palindrome(text) :
    cleaned = ''
    for c in text.lower():
        if 'a' <= c <= 'z':
            cleaned += c

    n = len(cleaned)
    for i in range(n // 2) :
        if cleaned[i] != cleaned[-(i+1)]:
            return False
    return True

print(palindrome("Never odd or even"))
print(palindrome("Hello"))