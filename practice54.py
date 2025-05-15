def even_star(nums):
    result = []

    for i in nums:
        if i % 2 == 0:
            result.append(i)

    return result

print(even_star([1, 2, 3, 4, 5, 6]))