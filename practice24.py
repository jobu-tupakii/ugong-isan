def palindrome_detective(text) :
    letter = []
    for char in text:
        if char.isalpha():
            num = (ord(char.lower()) - ord('a')) % 26
            letter.append(num)

    for i in range(len(letter) // 2):
        if letter[i] != letter[-(i+1)]:
            return False
    return True

print(palindrome_detective("A man a plan a canal Panama"))