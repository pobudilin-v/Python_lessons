### ДЗ 3.1. Найпростіший калькулятор

number_1=int(input("Введите первое число:"))
user_select=input("Выберите действие (+, -, *, /):")
number_2=int(input("Введите второе число:"))

match user_select:
    case "+":
        addition=number_1+number_2
        print(addition)
    case "-":
        subtraction=number_1-number_2
        print(subtraction)
    case "*":
        multiplication=number_1*number_2
        print(multiplication)
    case "/":
        if number_2 == 0:
            print("Ошибка, на ноль делить нельзя!")
        else:
            division=number_1/number_2
            print(division)
    case _:
        print("Ошибка, выберите действие")


################ Первый вариант:

# number_1=int(input("Введите первое число:"))
# number_2=int(input("Введите второе число:"))
# user_select=int(input("1. +\n2. -\n3. *\n4. /\nВыберите действие:"))
#
# match user_select:
#     case 1:
#         addition=number_1+number_2
#         print(addition)
#     case 2:
#         subtraction=number_1-number_2
#         print(subtraction)
#     case 3:
#         multiplication=number_1*number_2
#         print(multiplication)
#     case 4:
#         if number_2 == 0:
#             print("Ошибка, на ноль делить нельзя!")
#         else:
#             division=number_1/number_2
#             print(division)
#     case _:
#         print("Ошибка, выберите действие")