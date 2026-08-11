def difference(*args):
    if len(args) == 0:
        return 0
    maxnum = args[0]
    minnum = args[0]
    for num in args:
        if num > maxnum:
            maxnum = num
        if num < minnum:
            minnum = num
    return round(maxnum - minnum, 2)