def prime_generator(end):
    for number in range(2, end + 1):
        for num in range(2, number):
            if number % num == 0:
                break
        else:
            yield number