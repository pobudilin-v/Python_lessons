numbers = [0, 1, 7, 2, 4, 8]
if len(numbers) == 0:
    total = 0
else:
    totalsum = 0
    for even_numbers in range(0, len(numbers), 2):
        totalsum += numbers[even_numbers]
        total = totalsum * numbers[-1]
print(total)

###

# numbers = [0, 1, 7, 2, 4, 8]
# if len(numbers) == 0:
# #     total = 0
# else:
#     total = (sum(numbers[::2])*(numbers[-1]))
# print(totalsum)
