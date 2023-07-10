# 7. Написати програму, яка знайде факторіал введеного користувачем числа.
#
# Наприклад, факторіал числа 5 дорівнює добутку 1*2*3*4*5 = 120.
#
# Формула знаходження факторіалу:
#
#  n! = 1 * 2 * ... * n, де n - введене користувачем число.

number = int(input("Введіть число: "))

factorial: int = 1

if number < 0:
    print("Факторіал визначений лише для невід'ємних чисел.")
elif number == 0:
    print("Факторіал числа 0 дорівнює 1.")
else:
    for i in range(1, number + 1):
        factorial *= i

    print("Факторіал числа", number, "дорівнює", factorial)