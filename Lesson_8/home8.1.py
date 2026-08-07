def add_one(some_list):
    number_str = ""
    for digit in some_list:
        number_str += str(digit)
    number = int(number_str)
    number += 1
    result = []
    for digit in str(number):
        result.append(int(digit))
    return result