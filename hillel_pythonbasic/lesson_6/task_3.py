# 3. Дано перелік значень. Повернути словник, де кожен ключ - це індекс листа,
#
#   а значення листа – це значення ключа:
#
#   Input:
#
#     ['a', 'b', 'c', 'd', 'e']
#   Output
#
#   {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e'}

def list_to_dict(lst):
    result_dict = {}
    for index, value in enumerate(lst):
        result_dict[index] = value
    return result_dict


input_list = ['a', 'b', 'c', 'd', 'e']
output_dict = list_to_dict(input_list)
print(output_dict)
