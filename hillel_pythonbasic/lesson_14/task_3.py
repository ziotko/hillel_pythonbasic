import re


def is_valid_password(password):
    lowercase_pattern = r'[a-z]'
    uppercase_pattern = r'[A-Z]'
    digit_pattern = r'[0-9]'
    special_char_pattern = r'[$#@+=-]'

    if len(password) < 8:
        return "Пароль занадто короткий. Мінімум 8 символів."

    if (re.search(lowercase_pattern, password) and
            re.search(uppercase_pattern, password) and
            re.search(digit_pattern, password) and
            re.search(special_char_pattern, password)):
        return "Пароль коректний"
    else:
        return "Пароль не відповідає вимогам"


password = input("Введіть пароль: ")
result = is_valid_password(password)
print(result)
