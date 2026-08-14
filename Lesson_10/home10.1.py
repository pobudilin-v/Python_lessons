def some_gen(begin, end, func):
    yield begin
    for i in range(end - 1):
        begin = func(begin)
        yield begin