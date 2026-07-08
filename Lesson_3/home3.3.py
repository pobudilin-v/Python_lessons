numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
if len(numbers) == 0 and len(numbers) == 1:
    numbers_coppy = numbers.copy()
    listcopy = [numbers, numbers_coppy]
    print(listcopy)
else:
    half = (len(numbers)+1) // 2
    leftnums = numbers[:half]
    rightnums = numbers[half:]
    halflist2 = [leftnums, rightnums]
    print(halflist2)



