def even_odd_master(nums):
    even = []
    odd = []

    for c in nums:
        if c % 2 == 0:
            even.append(c)
        else:
            odd.append(c)

    even.sort()
    odd.sort(reverse=True)

    return even, odd

print(even_odd_master([5, 3, 2, 8, 1, 4]))