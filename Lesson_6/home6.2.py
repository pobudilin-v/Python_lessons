seconds = input("Введите количество секунд: ")
seconds = int(seconds)
if seconds < 0 or seconds >= 8640000:
    print("Ошибка, есть ограничение в количестве секунд: >= 0 и < 8640000")
else:
    days = seconds // 86400
    rem = seconds % 86400
    hours = rem // 3600
    rem = rem % 3600
    min = rem // 60
    sec = rem % 60
    if 11 <= days % 100 <= 14:
        day_word = "дней"
    elif days % 10 == 1:
        day_word = "день"
    elif 2 <= days % 10 <= 4:
        day_word = "дня"
    else:
        day_word = "дней"
    hours_str = str(hours).zfill(2)
    min_str = str(min).zfill(2)
    sec_str = str(sec).zfill(2)
    print(f"{days} {day_word}, {hours_str}:{min_str}:{sec_str}")