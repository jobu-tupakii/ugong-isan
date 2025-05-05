def digit_killer(text) :
    nums =[]
    for c in text:
        if c.isdigit():
            nums.append(int(c))
    return sum(nums)

print(digit_killer("a1b2c3"))