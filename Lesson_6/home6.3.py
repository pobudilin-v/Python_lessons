number = int(input("Введите число: "))
while number > 9:
    result = 1
    for num in str(number):
        result *= int(num)
    number = result
print(number)