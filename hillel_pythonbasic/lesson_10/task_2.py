# 2. Написати функцію, яка визначить, чи є введений текст паліндромом (той який читається однаково з будь-якого боку), приклад:

# Шалаш, зараз, Дід, Піп, 13231
# Паліндром — і ні морд, ні лап

def is_palindrome(text):
    text = ''.join(filter(str.isalpha, text))

    text = text.lower()

    return text == text[::-1]


user_input = input("Введите текст: ")

if is_palindrome(user_input):
    print("Это палиндром!")
else:
    print("Это не палиндром.")
