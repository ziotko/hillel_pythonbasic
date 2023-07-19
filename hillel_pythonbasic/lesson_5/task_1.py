#1. Написати функцію `is_prime`, що приймає 1 аргумент - число від 0 до 1000, і повертає `True`, якщо воно просте, і `False` - інакше.

#(Прості числа - ті які діляться без залишку тільки на себе або 1, наприклад 2, 3, 5, 7, 11 ...)

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


for number in range(1001):
    if is_prime(number):
        print(number)
