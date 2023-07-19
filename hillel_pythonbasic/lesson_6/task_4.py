# 4. Написати функцію, яка повертає поточний час. І обернути її у декоратор
#
#   який відрахує 3 секунди.
#
#   Приклад:
#
#   >>> what_time_is_it_now()
#   3
#   2
#   1
#   '16:21'
#   Повернути час допоможе метод time.strftime з аргументом '%H:%M'

import time


def three_seconds_delay(func):
    def wrapper(*args, **kwargs):
        for i in range(3, 0, -1):
            print(i)
            time.sleep(1)
        return func(*args, **kwargs)

    return wrapper


@three_seconds_delay
def what_time_is_it_now():
    current_time = time.strftime('%H:%M')
    return current_time


result = what_time_is_it_now()
print(result)
