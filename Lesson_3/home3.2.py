numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
if len(numbers) == 0 or len(numbers) == 1:
    print(numbers)
else:
    lastnumber = len(numbers)
    numbers.insert(0, lastnumber)
    numbers.pop(lastnumber)
    print(numbers)
