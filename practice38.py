def length_killer(text) :
    result = []
    word = text.split()

    for ap in word :
        result.append(len(ap))
        #틀린 이유
        #ap = result.append(len(word))라고 씀
        #일단 ap=~ 형식 자체가 안 되고, len(word)는 영원히 4

    return result

print(length_killer("This is a pen"))