# 3. Написати функцію яка зрушить отриманий список на N елементів вправо або вліво, аргументи, що приймаються - список і натуральне число(якщо негативне зрушуємо вліво, позитивне - вправо).

def shift_list(lst, n):

    length = len(lst)

    n = n % length

    if n >= 0:
        shifted_list = lst[-n:] + lst[:-n]
    else:
        shifted_list = lst[-n:] + lst[:-n]

    return shifted_list


input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

n = int(input("Введите смещение: "))

shifted_result = shift_list(input_list, n)
print("Результат сдвига:", shifted_result)
