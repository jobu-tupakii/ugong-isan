def duplication_hunter(nums) :
    result = []
    for i in nums:
        if i not in result:
            result.append(i)
    return result

print(duplication_hunter([1, 2, 2, 3, 1, 4]))