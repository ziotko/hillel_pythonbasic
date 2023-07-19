# 1. Дано два кортежі, напишіть функцію яка з'єднає їх в один dict:
#
#   Input:
#
#     coin = ('Bitcoin', 'Ether', 'Ripple', 'Litecoin')
#     code = ('BTC', 'ETH', 'XRP', 'LTC')
# Output:
#
# {'Bitcoin': 'BTC', 'Ether': 'ETH', 'Ripple': 'XRP', 'Litecoin': 'LTC'}
def merge_to_dict(keys, values):
    if len(keys) != len(values):
        raise ValueError("Длина кортежей не совпадает")

    return dict(zip(keys, values))


coin = ('Bitcoin', 'Ether', 'Ripple', 'Litecoin')
code = ('BTC', 'ETH', 'XRP', 'LTC')

result_dict = merge_to_dict(coin, code)
print(result_dict)
