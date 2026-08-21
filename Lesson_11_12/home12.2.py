def generate_cube_numbers(end):
    number = 2
    while True:
        cube = number ** 3
        if cube > end:
            return
        yield cube
        number += 1