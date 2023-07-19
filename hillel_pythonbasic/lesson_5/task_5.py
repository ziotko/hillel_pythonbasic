#5. Написати функцію square, що приймає 1 аргумент - сторону квадрата, і повертає 3 значення (за допомогою кортежу): периметр квадрата, площа квадрата та діагональ квадрата.

import math


def square(side):
    perimeter = 4 * side
    area = side ** 2
    diagonal = math.sqrt(2) * side

    return perimeter, area, diagonal


side_length = 5
result = square(side_length)
print("Периметр квадрата:", result[0])
print("Площадь квадрата:", result[1])
print("Диагональ квадрата:", result[2])
