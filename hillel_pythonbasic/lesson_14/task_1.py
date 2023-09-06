# 1. Формат українських номерів: ВН1010НС чи АА1010АА
#
#   На введення програма отримує рядок, у відповідь має повернути чи є рядок автомобільним номером чи ні.
#
# Повинна повернути регіон (має знати регіони 2004 та 2013 рр.)
#
#       Повинна однаково сприймати AI – англійський та АІ – український варіанти.
#
#       (Для BI, AI, IA і т.д.)

import re


def is_car_number(input_str):
    input_str = input_str.replace('А', 'A').replace('І', 'I')
    pattern = r'^[A-Z]{2}\d{4}[A-Z]{2}$'

    if not re.match(pattern, input_str):
        return "Це не є автомобільним номером"
    else:
        region = input_str[2:4]
        if region in ['01', '02', '03', '04', '05']:
            return f"Автомобільний номер {input_str} є дійсним номером з 2004 року"
        elif region in ['AI', 'BI', 'IA', 'II']:
            return f"Автомобільний номер {input_str} є дійсним номером з 2013 року"
        else:
            return "Автомобільний номер відповідає формату, але регіон не відомий"


input_str = input("Введіть автомобільний номер: ")
result = is_car_number(input_str)
print(result)
