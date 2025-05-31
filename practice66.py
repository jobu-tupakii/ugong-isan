def char_distance(text, target):
    n = len(text)
    result = [0] * n
    p = 1000

    for i in range(n):
        if text[i] == target:
            p = 0
        else:
            p += 1
        result[i] = p

    p = 1000
    for i in range(n - 1, -1, -1):
        if text[i] == target:
            p = 0
        else:
            p += 1
        result[i] = min(result[i], p)

    return result

text = "teachermode"
target = "e"
print(char_distance(text, target))