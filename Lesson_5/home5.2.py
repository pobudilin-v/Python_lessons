import sys
while True:
    number_1=int(input("Введите первое число:"))
    user_select=input("Выберите действие (+, -, *, /):")

    match user_select:
        case "+":
            number_2 = int(input("Введите второе число:"))
            addition=number_1+number_2
            print(addition)
        case "-":
            number_2 = int(input("Введите второе число:"))
            subtraction=number_1-number_2
            print(subtraction)
        case "*":
            number_2 = int(input("Введите второе число:"))
            multiplication=number_1*number_2
            print(multiplication)
        case "/":
            number_2 = int(input("Введите второе число:"))
            if number_2 == 0:
                print("Ошибка, на ноль делить нельзя!")
            else:
                division=number_1/number_2
                print(division)
        case _:
            print("Ошибка, выберите действие")
    while True:
        nextorquit = input("Продолжить? (y/n)").lower().strip()
        if nextorquit == "y":
            break
        elif nextorquit == "n":
            sys.exit()
        else:
            print("Введите y (yes) / n (no):")
