# 7. ** дод. Написати функцію `is_date`, що приймає 3 аргументи - день, місяць і рік.
#
# Повернути `True`, якщо дата коректна (треба враховувати число місяця. Наприклад 30.02 - дата не коректна, так само 31.06 або 32.07 тощо), та `False` інакше.
#
#
#
# (можна використовувати модуль datetime)

import datetime


def is_date(day, month, year):
    try:
        datetime.datetime(year, month, day)
        return True
    except ValueError:
        return False


day = 30
month = 2
year = 2023
valid = is_date(day, month, year)
print(valid)
