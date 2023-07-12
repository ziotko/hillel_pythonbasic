def compare_lists(list1, list2):
    intersection = set(list1) & set(list2)
    only_in_first = set(list1) - set(list2)
    unique_numbers = set(list1 + list2)

    print("Числа в первом и во втором списке:")
    print(intersection)

    print("Числа в первом списке, в втором их нет:")
    print(only_in_first)

    print("Только уникальные числа для первого и второго списка:")
    print(unique_numbers)


list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
compare_lists(list1, list2)
