def common_elements():
    list3 = set(i for i in range(100) if i % 3 == 0)
    list5 = set(i for i in range(100) if i % 5 == 0)
    return list3 & list5