def frequent_killer(nums):
    freq = {}

    for num in nums:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1

    max_count = max(freq.values())
    result = None

    for num in freq:
        if freq[num] == max_count:
            if result is None or num < result:
                result = num

    return result

print(frequent_killer([1, 3, 1, 3, 2, 1]))