import string
import keyword

variable_name = input("Введите наименование переменной для проверки:")
is_valid = True
if len(variable_name) == 0:
    is_valid = False
elif variable_name[0].isdigit():
    is_valid = False
elif variable_name in string.ascii_uppercase:
    is_valid = False
elif variable_name in keyword.kwlist:
    is_valid = False
elif "__" in variable_name:
    is_valid = False
else:
    for symbol in variable_name:
        if symbol.isupper():
            is_valid = False
            break
        elif symbol == " ":
            is_valid = False
            break
        elif symbol in string.punctuation and symbol != "_":
            is_valid = False
print(f"{variable_name} - {is_valid}")
