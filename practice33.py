def even_square_machine(lst) :
    result = []
    for i in range(len(lst)):
        if lst[i] % 2 == 0:
            result.append(lst[i] * lst[i])
    return result

print(even_square_machine([1, 2, 3, 4, 5]))