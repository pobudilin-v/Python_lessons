def find_unique_value(some_list):
    for number in some_list:
        repeats = 0
        for other_number in some_list:
            if number == other_number:
                repeats += 1
        if repeats == 1:
            return number