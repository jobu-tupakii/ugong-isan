def upper_lower_monster(text):
    up = []
    lo = []

    for i in text:
        if i.isupper():
            up.append(i)
        elif i.islower():
            lo.append(i)
        else:
            pass

    return len(up), len(lo)

upper, lower = upper_lower_monster("Hello World!")
print("대문자: %d\n소문자: %d" %(upper, lower))