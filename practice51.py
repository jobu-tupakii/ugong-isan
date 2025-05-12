def sum_master(text):
    num=[]

    for i in text:
        if i.isnumeric():
            num.append(int(i))

    return sum(num)

print(sum_master("a1b2c3"))