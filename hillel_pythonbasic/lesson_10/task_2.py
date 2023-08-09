def is_palindrome(text):
    text = ''.join(filter(str.isalpha, text))

    text = text.lower()

    return text == text[::-1]


user_input = input("Введите текст: ")

if is_palindrome(user_input):
    print("Это палиндром!")
else:
    print("Это не палиндром.")
