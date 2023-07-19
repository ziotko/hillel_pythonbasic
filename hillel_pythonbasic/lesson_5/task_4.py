#4. Даний перелік випадкових цілих чисел. Замініть усі непарні числа списку нулями. І виведете їхню кількість.
def replace_odd_with_zeros(numbers):
    count = 0
    for i in range(len(numbers)):
        if numbers[i] % 2 != 0:
            numbers[i] = 0
            count += 1
    return count


random_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd_count = replace_odd_with_zeros(random_numbers)
print("Количество замененных нечетных чисел:", odd_count)
print("Измененный список чисел:", random_numbers)
